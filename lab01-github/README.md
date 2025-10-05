# 🛠️LAB01:  Software Engineering Project – TaskNest

## 📌 Giới thiệu
**TaskNest** là một hệ thống quản lý công việc nhóm theo mô hình **Kanban**, được phát triển trong môn *Nhập môn Công nghệ Phần mềm*.  
Mục tiêu dự án: áp dụng kiến thức **fullstack web** để xây dựng nền tảng hỗ trợ nhóm/doanh nghiệp trong việc **tạo, quản lý, phân loại, kéo-thả và lọc thẻ công việc**.

---

## 👥 Thành viên nhóm

| Thành viên | Vai trò | Liên kết cá nhân |
|-------------|----------|------------------|
| **Huỳnh Minh Hải** | 🧠 Leader · Backend Developer · UI/UX Designer | [🌐 harihuynh2007.github.io](https://harihuynh2007.github.io) |
| **Nguyễn Bá Bảo Nam** | 💻 Frontend Developer | — |



---

## 🎯 Mục tiêu
- Ứng dụng kiến thức fullstack để xây dựng hệ thống quản lý công việc trực tuyến.  
- Tối ưu trải nghiệm người dùng với tính năng **drag & drop**.  
- Đáp ứng nhu cầu quản lý dự án: phân quyền, cộng tác thời gian thực, theo dõi tiến độ.  

---

## 📂 Nội dung chính
- Thiết kế giao diện (UI/UX) trực quan, hỗ trợ kéo–thả danh sách/thẻ.  
- Tích hợp **Authentication & Authorization**: JWT + Google OAuth.  
- Xây dựng **API** quản lý board, danh sách, thẻ, nhãn, thành viên, bình luận.  
- Đảm bảo bảo mật, quản lý session và hiệu năng hệ thống.  

---

## 🎯 Use Case chính
1. **Quản lý người dùng**
   - Đăng ký, đăng nhập, đăng xuất, phân quyền, chỉnh sửa thông tin.
2. **Quản lý bảng công việc (Board)**
   - Tạo, sửa, xoá bảng; chia sẻ và phân quyền thành viên.
3. **Quản lý danh sách (List)**
   - Thêm, sửa, xoá danh sách trong từng bảng.
4. **Quản lý thẻ công việc (Card)**
   - Tạo, chỉnh sửa, xoá thẻ; gán người phụ trách, thêm nhãn, bình luận.
5. **Cộng tác & Thông báo**
   - Thành viên tương tác qua bình luận, nhận thông báo thay đổi.
6. **Báo cáo & Phân tích tiến độ**
   - Thống kê và theo dõi tiến độ dự án theo thời gian thực.


---

## 📐 Thiết kế hệ thống
- **Use Case Diagram**: [Xem chi tiết tại đây](https://github.com/Harihuynh2007/NHAPMONCNPM/blob/main/lab02-usecase/usecaseimage.png)
- **Sequence Diagram**: [Xem chi tiết tại đây](https://github.com/Harihuynh2007/NHAPMONCNPM/blob/main/lab03-uml/readme.md#2-sequence-diagram)
- **ERD (Entity Relationship Diagram)**: [![ERD](https://github.com/Harihuynh2007/NHAPMONCNPM/blob/main/lab03-uml/ERD.png) 

---

## 💻 Công nghệ sử dụng
- **Frontend**: ReactJS / Next.js + Tailwind CSS  
- **Backend**: Django  
- **CSDL**: MongoDB / PostgreSQL  
- **Authentication**: JWT + Google OAuth  
- **Quản lý phiên bản**: Git + GitHub  
- **Mô hình phát triển**: Agile – Scrum  

---

## 🚀 Cài đặt & chạy thử
-Clone repo:
```bash
git clone https://github.com/vancv43/tasknest.git
cd tasknest
```
-Chạy Server
```bash
npm run dev
# hoặc: npm start
```
-Kết quả dự kiến
```bash
Server chạy tại http://localhost:3000
Trang trả về: Hello World
```
## 📊 Kết quả dự kiến
- **Báo cáo**: Quá trình phát triển, phân tích yêu cầu, thiết kế hệ thống (CSDL, API, UI), đánh giá sản phẩm.  
- **Slide thuyết trình**: Mục tiêu, quy trình, demo sản phẩm, kết quả đạt được.  
- **Source code**: Mã nguồn đầy đủ của hệ thống.  
