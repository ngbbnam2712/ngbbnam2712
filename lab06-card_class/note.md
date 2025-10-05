# Thiết kế Class Diagram và Package Diagram

## Mục tiêu

Từ Use Case và Sequence Diagram đã phân tích, thiết kế **Class Diagram** để thể hiện chi tiết lớp, thuộc tính, phương thức, và các mối quan hệ.  
Sau đó gom nhóm các lớp theo chức năng thành **Package Diagram** để hình dung kiến trúc tổng thể.

---

## 1. Class Diagram

### 1.1. Nhóm Account (Người dùng & Xác thực)

- **User**
  - `+ userId: int`
  - `+ name: String`
  - `+ email: String`
  - `+ password: String`
  - `+ dangKy(): void`
  - `+ dangNhap(): void`
  - `+ capNhatThongTin(): void`
  - `+ dangXuat(): void`
- **AuthService**
  - `+ dangKy(): void`
  - `+ dangNhap(): void`
  - `+ dangXuat(): void`

**Quan hệ:**  
AuthService tương tác với User và Database để xác thực.

---

### 1.2. Nhóm Board (Quản lý bảng)

- **Board**
  - `+ boardId: int`
  - `+ title: String`
  - `+ ownerId: int`
  - `+ taoBang(): void`
  - `+ chinhSua(): void`
  - `+ xoa(): void`
  - `+ themThanhVien(): void`
- **Membership**
  - `+ userId: int`
  - `+ boardId: int`
  - `+ role: String`

**Quan hệ:**  
- User tham gia nhiều Board thông qua Membership.  
- Một Board có nhiều List.

---

### 1.3. Nhóm List (Danh sách công việc)

- **List**
  - `+ listId: int`
  - `+ title: String`
  - `+ boardId: int`
  - `+ taoDanhSach(): void`
  - `+ chinhSua(): void`
  - `+ xoa(): void`

**Quan hệ:**  
Mỗi Board chứa nhiều List.

---

### 1.4. Nhóm Card (Thẻ công việc)

- **Card**
  - `+ cardId: int`
  - `+ title: String`
  - `+ description: String`
  - `+ dueDate: Date`
  - `+ listId: int`
  - `+ taoThe(): void`
  - `+ chinhSua(): void`
  - `+ xoa(): void`

**Quan hệ:**  
Mỗi List chứa nhiều Card.

---

### 1.5. Nhóm Database

- **Database**
  - `+ luuDuLieu(): void`
  - `+ truyXuatDuLieu(): void`

**Quan hệ:**  
Database lưu trữ dữ liệu cho tất cả các nhóm (Account, Board, List, Card).

---

### 1.6. Sơ đồ Class Diagram

```mermaid
classDiagram
    class User {
        +int userId
        +String name
        +String email
        +String password
        +dangKy()
        +dangNhap()
        +capNhatThongTin()
        +dangXuat()
    }

    class Board {
        +int boardId
        +String title
        +int ownerId
        +taoBang()
        +chinhSua()
        +xoa()
        +themThanhVien()
    }

    class List {
        +int listId
        +String title
        +int boardId
        +taoDanhSach()
        +chinhSua()
        +xoa()
    }

    class Card {
        +int cardId
        +String title
        +String description
        +Date dueDate
        +int listId
        +taoThe()
        +chinhSua()
        +xoa()
    }

    class Membership {
        +int userId
        +int boardId
        +String role
    }

    class AuthService {
        +dangKy()
        +dangNhap()
        +dangXuat()
    }

    class Database {
        +luuDuLieu()
        +truyXuatDuLieu()
    }

    User "1" -- "many" Membership
    Membership "many" -- "1" Board
    Board "1" -- "many" List
    List "1" -- "many" Card
    AuthService --> User
    AuthService --> Database
    Board --> Database
    List --> Database
    Card --> Database
## 2. Package Diagram

### 2.1. Packages

- **Account**  
  Quản lý người dùng và xác thực (*User, AuthService*).

- **Board**  
  Quản lý bảng công việc và thành viên (*Board, Membership*).

- **List**  
  Quản lý danh sách trong bảng (*List*).

- **Card**  
  Quản lý thẻ công việc trong danh sách (*Card*).

- **Database**  
  Lưu trữ và xử lý dữ liệu (*Database*).

---

### 2.2. Quan hệ giữa các Package

- **Account → Database**: xác thực và quản lý người dùng.  
- **Board → Account**: bảng gắn với người dùng.  
- **Board → Database**: lưu trữ bảng và thành viên.  
- **List → Board**: danh sách thuộc bảng.  
- **List → Database**: lưu danh sách.  
- **Card → List**: thẻ thuộc danh sách.  
- **Card → Database**: lưu thẻ.  

---

### 2.3. Sơ đồ Package Diagram

```mermaid
classDiagram
    package "Account" {
        class User
        class AuthService
    }

    package "Board" {
        class Board
        class Membership
    }

    package "List" {
        class List
    }

    package "Card" {
        class Card
    }

    package "Database" {
        class Database
    }

    Account --> Database
    Board --> Database
    List --> Database
    Card --> Database
    Board --> Account
    List --> Board
    Card --> List
