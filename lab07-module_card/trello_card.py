"""
trello_card.py
Module mô phỏng tạo Card cho Trello-mini bằng Python + mysql-connector-python.

Cách dùng:
1. Cập nhật cấu hình DB ở phần DB_CONFIG
2. Chạy:
    python trello_card.py

Module sẽ:
- Tạo schema nếu chưa có
- Tạo user/board/list mẫu
- Tạo 1 card bằng hàm create_card
- In ra card_id mới
"""

import mysql.connector
from mysql.connector import errorcode
from datetime import datetime
import sys

# ---------- Cấu hình DB ----------
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "123456",
    "database": "trello_mini"
}

# ---------- SQL tạo bảng ----------
SCHEMA_SQL = """
CREATE DATABASE IF NOT EXISTS trello_mini CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE trello_mini;

CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS boards (
    board_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    owner_id INT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (owner_id) REFERENCES users(user_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS memberships (
    membership_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    board_id INT NOT NULL,
    role VARCHAR(50) DEFAULT 'member',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    UNIQUE KEY (user_id, board_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (board_id) REFERENCES boards(board_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS lists (
    list_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    board_id INT NOT NULL,
    position INT DEFAULT 0,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (board_id) REFERENCES boards(board_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS cards (
    card_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    due_date DATETIME NULL,
    list_id INT NOT NULL,
    position INT DEFAULT 0,
    created_by INT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (list_id) REFERENCES lists(list_id) ON DELETE CASCADE,
    FOREIGN KEY (created_by) REFERENCES users(user_id) ON DELETE SET NULL
);
"""

# ---------- Helper: connect DB ----------
def get_connection(config=DB_CONFIG):
    conn = mysql.connector.connect(
        host=config["host"],
        user=config["user"],
        password=config["password"],
        autocommit=False  # we'll manage transactions
    )
    return conn

# ---------- Khởi tạo schema ----------
def init_schema():
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        for stmt in SCHEMA_SQL.split(';'):
            s = stmt.strip()
            if s:
                cursor.execute(s)
        conn.commit()
        cursor.close()
        print("[init_schema] Done.")
    except mysql.connector.Error as err:
        print("[init_schema] Error:", err)
        if conn:
            conn.rollback()
        raise
    finally:
        if conn:
            conn.close()

# ---------- Kết nối tới database đã chọn ----------
def get_db_connection():
    # Connect trực tiếp tới database (tên db trong DB_CONFIG)
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except mysql.connector.Error as err:
        print("[get_db_connection] Connection error:", err)
        raise

# ---------- CRUD helper: tạo user/board/list mẫu ----------
def create_user(name, email, password_hash="dummyhash"):
    conn = get_db_connection()
    try:
        cur = conn.cursor()
        sql = "INSERT INTO users (name, email, password_hash) VALUES (%s, %s, %s)"
        cur.execute(sql, (name, email, password_hash))
        user_id = cur.lastrowid
        conn.commit()
        return user_id
    finally:
        cur.close()
        conn.close()

def create_board(title, owner_id):
    conn = get_db_connection()
    try:
        cur = conn.cursor()
        sql = "INSERT INTO boards (title, owner_id) VALUES (%s, %s)"
        cur.execute(sql, (title, owner_id))
        board_id = cur.lastrowid
        # add membership: owner
        cur.execute("INSERT INTO memberships (user_id, board_id, role) VALUES (%s, %s, %s)",
                    (owner_id, board_id, 'owner'))
        conn.commit()
        return board_id
    finally:
        cur.close()
        conn.close()

def create_list(title, board_id, position=0):
    conn = get_db_connection()
    try:
        cur = conn.cursor()
        sql = "INSERT INTO lists (title, board_id, position) VALUES (%s, %s, %s)"
        cur.execute(sql, (title, board_id, position))
        list_id = cur.lastrowid
        conn.commit()
        return list_id
    finally:
        cur.close()
        conn.close()

# ---------- Hàm chính: create_card ----------
def create_card(list_id, title, description=None, due_date=None, created_by=None, position=0):
    """
    Tạo card mới an toàn:
    - Kiểm tra list tồn tại
    - Dùng transaction để insert
    - Trả về card_id
    due_date: None hoặc datetime object
    """
    if not title or not title.strip():
        raise ValueError("Title must not be empty")

    conn = get_db_connection()
    try:
        cur = conn.cursor(buffered=True)
        # Kiểm tra list tồn tại
        cur.execute("SELECT list_id, board_id FROM lists WHERE list_id = %s", (list_id,))
        if cur.rowcount == 0:
            raise ValueError(f"List with id={list_id} does not exist")

        # (optional) check user membership if created_by is provided
        if created_by is not None:
            cur.execute("SELECT membership_id FROM memberships WHERE user_id = %s AND board_id = (SELECT board_id FROM lists WHERE list_id = %s)",
                        (created_by, list_id))
            if cur.rowcount == 0:
                raise PermissionError("User is not a member of the board that contains this list")

        # Insert card
        sql = """
            INSERT INTO cards (title, description, due_date, list_id, position, created_by)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        due_val = due_date.strftime("%Y-%m-%d %H:%M:%S") if isinstance(due_date, datetime) else due_date
        cur.execute(sql, (title, description, due_val, list_id, position, created_by))
        card_id = cur.lastrowid
        conn.commit()
        return card_id
    except mysql.connector.Error as err:
        conn.rollback()
        print("[create_card] DB error:", err)
        raise
    finally:
        cur.close()
        conn.close()

# ---------- Utility: lấy card theo id (để kiểm tra) ----------
def get_card(card_id):
    conn = get_db_connection()
    try:
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT * FROM cards WHERE card_id = %s", (card_id,))
        row = cur.fetchone()
        return row
    finally:
        cur.close()
        conn.close()

# ---------- Demo: tạo dữ liệu mẫu và tạo 1 card ----------
def demo():
    print("=== Trello-mini demo: create card ===")
    try:
        init_schema()
    except Exception as e:
        print("init_schema failed:", e)
        # continue in case database exists

    # Tạo user, board, list mẫu
    try:
        user_id = create_user("Nguyen Van A", "a@example.com")
        print("Created user_id =", user_id)
    except mysql.connector.IntegrityError:
        # nếu email đã tồn tại, lấy user_id hiện có
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT user_id FROM users WHERE email=%s", ("a@example.com",))
        row = cur.fetchone()
        cur.close()
        conn.close()
        user_id = row[0]
        print("User already exists, user_id =", user_id)

    # Tạo board
    board_id = create_board("Project A", user_id)
    print("Created board_id =", board_id)

    # Tạo list
    list_id = create_list("Todo", board_id)
    print("Created list_id =", list_id)

    # Tạo card
    due = datetime.now()
    try:
        card_id = create_card(list_id=list_id,
                              title="Thiết kế giao diện chính",
                              description="Hoàn thiện mockup trang chính",
                              due_date=due,
                              created_by=user_id,
                              position=1)
        print("Created card_id =", card_id)
        card = get_card(card_id)
        print("Card detail:", card)
    except Exception as e:
        print("Failed to create card:", e)

if __name__ == "__main__":
    # Trước khi chạy, bạn cần chỉnh DB_CONFIG cho phù hợp
    if DB_CONFIG["password"] == "your_password_here":
        print("⚠️  Please update DB_CONFIG['password'] in the script before running.")
        sys.exit(1)
    demo()
