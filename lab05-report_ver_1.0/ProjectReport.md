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

### 4. Form đăng nhập (Login)

**Thành phần:** chỉ gồm `login.html` và `login.css`, chưa có xử lý backend.  

**Mục đích:** cho phép người dùng nhập email + mật khẩu.  

**Mô tả giao diện:**
- Form với 2 ô input: **Email** và **Password**.  
- Nút **Login** để gửi yêu cầu.  
- Link *"Quên mật khẩu"* hoặc *"Đăng ký tài khoản mới"* (tùy chọn).  

---

### 5. Mô hình dữ liệu (ERD)

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

### 6. Báo cáo
- Tổng hợp artifacts, test case, code.  
- Viết báo cáo **Markdown/PDF**.  

#### 6.1. Phân tích yêu cầu
- **Actors:** User, System.  
- **Use Case:** Tạo card trong danh sách.  
- **Luồng chính:** Nhập thông tin → Validate → Lưu DB → Hiển thị card.  
- **Ngoại lệ:** Title rỗng, List/User không tồn tại.  

#### 6.2. Thiết kế hệ thống
- **ERD:** Bảng `CARDS` liên kết `LISTS`, `USERS`.  
- **Backend:** API `POST /cards` (Express + MySQL).  
- **UI:** Form HTML/CSS nhập *Title, Description, Due Date*.  

#### 6.3. Lập trình & tích hợp
- Viết API tạo card + kết nối DB.  
- Form gửi request tạo card.  
- **Unit test:** validate dữ liệu.  
- **Integration test:** nhập form → hiển thị card.  

#### 6.4. Quản lý source code
- Quản lý với **Git/GitHub**, commit theo giai đoạn *(design, backend, frontend, test)*.  
- Tag version **v1.0**.  

#### 6.5. Kiểm thử
- **Unit test:**  
  - Title rỗng/List sai → *Fail*.  
  - Input hợp lệ → *Success*.  
- **Integration test:** nhập form → card hiển thị.  
## 7. Hướng dẫn push code & tạo tag version

```bash
# Cấu hình lần đầu
git config --global user.name "Tên của bạn"
git config --global user.email "email@example.com"

# Thêm remote
git remote add origin https://github.com/username/repo.git

# Push code
git add .
git commit -m "Hoàn thiện v1.0 - TaskNet"
git push origin main

# Tạo tag v1.0
git tag v1.0
git push origin v1.0
```

---

## 8. Kết luận
Dự án đã hoàn thành đúng yêu cầu Lab: từ phân tích, thiết kế, lập trình, kiểm thử đến báo cáo. Hệ thống có thể mở rộng thêm nhiều chức năng thực tế khác

