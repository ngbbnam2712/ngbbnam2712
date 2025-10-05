# Use Case Description

Dựa trên sơ đồ use case tổng quát, các ca sử dụng được mô tả chi tiết như sau:

---

## 1. Use Case: Đăng ký  
- **Actor:** User  
- **Mục tiêu:** Người dùng tạo tài khoản mới để sử dụng hệ thống.  
- **Tiền điều kiện:** Người dùng chưa có tài khoản.  
- **Luồng sự kiện chính:**  
  1. User chọn chức năng **Đăng ký**.  
  2. Hệ thống yêu cầu nhập thông tin (họ tên, email, mật khẩu, …).  
  3. User nhập thông tin và xác nhận.  
  4. Hệ thống kiểm tra hợp lệ → lưu vào CSDL.  
  5. Thông báo đăng ký thành công.  
- **Ngoại lệ:** Email đã tồn tại, dữ liệu nhập không hợp lệ → hệ thống yêu cầu nhập lại.  
- **Kết quả:** User có tài khoản hợp lệ.  

---

## 2. Use Case: Đăng nhập  
- **Actor:** User  
- **Mục tiêu:** User truy cập vào hệ thống bằng tài khoản.  
- **Tiền điều kiện:** User đã có tài khoản.  
- **Luồng sự kiện chính:**  
  1. User chọn chức năng **Đăng nhập**.  
  2. Hệ thống yêu cầu nhập email và mật khẩu.  
  3. User nhập thông tin và gửi.  
  4. Hệ thống xác thực.  
  5. Nếu thành công → truy cập vào hệ thống.  
- **Ngoại lệ:** Sai thông tin → hệ thống báo lỗi.  
- **Kết quả:** User đăng nhập thành công.  

---

## 3. Use Case: Đăng xuất  
- **Actor:** User  
- **Mục tiêu:** Kết thúc phiên làm việc an toàn.  
- **Tiền điều kiện:** User đã đăng nhập.  
- **Luồng sự kiện chính:**  
  1. User chọn chức năng **Đăng xuất**.  
  2. Hệ thống hủy phiên đăng nhập.  
  3. Thông báo đăng xuất thành công.  
- **Kết quả:** User thoát khỏi hệ thống.  

---

## 4. Use Case: Quản lý thành viên *(include Đăng nhập)*  
- **Actor:** User (quản trị/nhân viên được phân quyền).  
- **Mục tiêu:** Quản lý danh sách thành viên.  
- **Tiền điều kiện:** User đã đăng nhập.  
- **Luồng sự kiện chính:**  
  1. User chọn **Quản lý thành viên**.  
  2. Hệ thống hiển thị danh sách thành viên.  
  3. User có thể thêm, sửa, xóa, tìm kiếm.  
- **Kết quả:** Danh sách thành viên được cập nhật.  

---

## 5. Use Case: Quản lý thẻ *(include Đăng nhập)*  
- **Actor:** User  
- **Mục tiêu:** Quản lý các thẻ (thẻ thành viên/thẻ dịch vụ).  
- **Tiền điều kiện:** User đã đăng nhập.  
- **Luồng sự kiện chính:**  
  1. User chọn **Quản lý thẻ**.  
  2. Hệ thống hiển thị danh sách thẻ.  
  3. User thêm, sửa, xóa, khóa/mở thẻ.  
- **Kết quả:** Hệ thống cập nhật trạng thái thẻ.  

---

## 6. Use Case: Quản lý danh sách *(include Đăng nhập)*  
- **Actor:** User  
- **Mục tiêu:** Quản lý danh sách dữ liệu (ví dụ: danh sách học viên, danh sách dịch vụ, …).  
- **Tiền điều kiện:** User đã đăng nhập.  
- **Luồng sự kiện chính:**  
  1. User chọn **Quản lý danh sách**.  
  2. Hệ thống hiển thị danh sách.  
  3. User có thể thêm, sửa, xóa.  
- **Kết quả:** Danh sách được cập nhật.  

---

## 7. Use Case: Quản lý bảng *(include Đăng nhập)*  
- **Actor:** User  
- **Mục tiêu:** Quản lý dữ liệu dưới dạng bảng (cấu hình, phân loại, …).  
- **Tiền điều kiện:** User đã đăng nhập.  
- **Luồng sự kiện chính:**  
  1. User chọn **Quản lý bảng**.  
  2. Hệ thống hiển thị bảng dữ liệu.  
  3. User thêm, sửa, xóa các mục.  
- **Kết quả:** Bảng được cập nhật.  
