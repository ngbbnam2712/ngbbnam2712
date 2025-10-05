# 📑 Project Report – TaskNest 

## 1. Giới thiệu dự án  

- **Tên**: TaskNest – Ứng dụng Quản lý Công việc  
- **Mục tiêu**:  
  Xây dựng một ứng dụng mô phỏng Trello/Jira để quản lý công việc theo Scrum.  
  Người dùng có thể:  
  - Tạo board, list, card  
  - Phân công thành viên  
  - Theo dõi tiến độ qua sprint  

- **Quy mô**:  
  Bài tập học tập (lab) – mức độ cơ bản nhưng bao quát đầy đủ các luồng chính:  
  - **User**  
  - **Board**  
  - **List**  
  - **Card**  
  - **Membership**  
  - **Sprint**  
## 2. Use Case Diagram

**Mô tả:** Hệ thống có 2 tác nhân chính:

- **User**: thực hiện các thao tác quản lý tài khoản, bảng, danh sách và thẻ.  
- **Admin/Chủ bảng**: ngoài quyền của User, có thêm quyền quản lý thành viên.

**Các Use Case chính:**
- **Quản lý tài khoản**: Đăng ký, Đăng nhập, Cập nhật thông tin, Đăng xuất.  
- **Quản lý bảng**: Tạo, Chỉnh sửa, Xóa, Thêm thành viên.  
- **Quản lý danh sách**: Tạo, Chỉnh sửa, Xóa.  
- **Quản lý thẻ**: Tạo, Chỉnh sửa, Xóa.  

---

## 3. Sequence Diagram

**Mô tả:** Các Sequence Diagram thể hiện luồng tương tác giữa **User ↔ Giao diện ↔ Hệ thống ↔ CSDL** cho từng chức năng chính.

- **Đăng ký**: User nhập thông tin → Hệ thống kiểm tra → Lưu vào CSDL → Trả kết quả.  
- **Đăng nhập**: User nhập email/mật khẩu → Hệ thống xác thực với CSDL → Trả kết quả.  
- **Tạo bảng**: User chọn tạo → Hệ thống lưu vào CSDL → Hiển thị bảng mới.  
- **Tạo danh sách**: User chọn tạo → Hệ thống lưu vào CSDL → Hiển thị danh sách mới.  
- **Tạo thẻ**: User chọn tạo → Hệ thống lưu vào CSDL → Hiển thị thẻ mới.  
- **Thêm thành viên**: Admin nhập email → Hệ thống kiểm tra → Thêm vào bảng nếu hợp lệ → Hiển thị danh sách thành viên mới.  

---

### 4. Mô hình dữ liệu (ERD)

**Thực thể chính:**
- **USERS**: lưu thông tin người dùng *(id, tên, email, mật khẩu, ngày tạo)*.  
- **BOARDS**: lưu bảng công việc *(id, tiêu đề, chủ sở hữu, ngày tạo)*.  
- **MEMBERSHIPS**: quản lý quan hệ giữa **User ↔ Board** với vai trò *(member, admin...)*.  
- **LISTS**: danh sách trong mỗi bảng *(id, tiêu đề, thuộc về board, vị trí, ngày tạo)*.  
- **CARDS**: thẻ công việc trong danh sách *(id, tiêu đề, mô tả, hạn chót, vị trí, người tạo, ngày tạo & cập nhật)*.  

**Quan hệ chính:**
- Một **User** có thể tham gia nhiều **Board** (qua **Memberships**).  
- Một **Board** có thể chứa nhiều **List**.  
- Một **List** có thể chứa nhiều **Card**.  
- Một **User** có thể tạo nhiều **Card**.  
- Mỗi **Board** có một **User** làm chủ sở hữu.  
## 📌 Quy trình Use Case "Tạo Card"

## 5. Code SQL minh họa

```sql
CREATE TABLE `cards` (
  `card_id` INT AUTO_INCREMENT PRIMARY KEY,
  `title` VARCHAR(255) NOT NULL,
  `description` TEXT,
  `due_date` DATETIME NULL,
  `list_id` INT NOT NULL,
  `position` INT DEFAULT 0,
  `created_by` INT NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  INDEX (`list_id`),
  INDEX (`created_by`)
);

-- FOREIGN KEY ví dụ:
ALTER TABLE cards
  ADD CONSTRAINT fk_cards_lists
    FOREIGN KEY (list_id) REFERENCES lists(list_id)
    ON DELETE CASCADE,
  ADD CONSTRAINT fk_cards_users
    FOREIGN KEY (created_by) REFERENCES users(user_id)
    ON DELETE CASCADE;
## 6. Kết quả chạy test

### 6.1 Unit Test (card module)

- Tạo card hợp lệ → trả **201 + cardId**  
- Title rỗng → trả **400** với thông báo lỗi  
- List/User không tồn tại → trả **404**  
- Lỗi DB → trả **500**  

**Ví dụ test case với Jest:**

```javascript
test("Tạo card thành công", async () => {
  req.body = { title: "Task 1", listId: 10, userId: 5 };
  mockDb.query.mockResolvedValueOnce([{ insertId: 101 }]);
  await createCard(req, res);
  expect(res.status).toHaveBeenCalledWith(201);
  expect(res.json).toHaveBeenCalledWith({
    message: "Tạo card thành công",
    cardId: 101
  });
});
```
### 7.2 Integration Test (login form)

- **Kịch bản:**  
  Script Selenium mở browser, nhập **email + password**, bấm **Login**.  
  Chờ tối đa **10 giây** để bắt alert/error box hiển thị.  

- **Kết quả test:**

| Test Case | Mô tả                       | Expected Result              | Status  |
|-----------|-----------------------------|------------------------------|---------|
| TC-LI1    | Login với thông tin hợp lệ  | Chuyển hướng vào dashboard   | Passed  |
| TC-LI2    | Sai mật khẩu                | Hiển thị thông báo lỗi       | Passed  |
| TC-LI3    | Toggle password visibility  | Hiện/ẩn mật khẩu đúng        | Passed  |
| TC-LI4    | Remember & Cancel           | Lưu trạng thái/Thoát form OK | Passed  |

✅ *All UI tests finished successfully.*
## 8. Kết luận & Định hướng mở rộng

### 8.1 Kết luận
- Dự án **TaskNest** đã hoàn thành các bước:  
  Phân tích UML → Thiết kế ERD → Code backend + frontend → Kiểm thử unit & integration.  
- Mô hình dữ liệu **hợp lý, có khả năng mở rộng**.  
- Test bao phủ cả **logic (unit test)** và **giao diện (integration test)**.  
- Đây là phiên bản **v1.0 demo** đủ để kiểm tra các chức năng quản lý card cơ bản.  

### 8.2 Định hướng mở rộng
1. Tích hợp **Google/GitHub OAuth** cho login.  
2. Thêm tính năng **drag & drop card** như Trello.  
3. Quản lý nhiều **workspace** và quyền nâng cao *(owner, admin, member, viewer)*.  
4. Thông báo **realtime** (WebSocket/Socket.io).  
5. **CI/CD pipeline** & test automation.  
6. **Mobile-first UI** tối ưu cho thiết bị di động.  
7. Nâng cao bảo mật (**rate limiting, 2FA**).  
