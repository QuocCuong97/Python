# Hệ thống Admin trong Django
- Thường ở mỗi website , đặc biệt là web bán hàng, blog hay tin tức thì ta cần một hệ thống **admin** để quản lý những vấn đề như thêm sửa xoá dữ liệu. Công việc xây dựng **admin** khá là mất nhiều thời gian và gây ra sự nhàm chán . 
- Ở trong **Django** đã cung cấp sẵn một hệ thống admin rất là tiện lợi mà ta không cần phải viết ra nó .
## **1) Tạo tài khoản admin**
- **B1 :** Sử dụng lệnh sau để tạo 1 tài khoản **admin** truy cập hệ thống :
    ```sh
    $ python3 manage.py createsuperuser
    ```
- **B2 :** Sau khi nhập lệnh, **Django** yêu cầu thông tin tài khoản admin gồm : username, email và password để khởi tạo :

    <img src=https://i.imgur.com/heabP5Z.png>

- **B3 :** Chạy `runserver` lên và vào đường dẫn `localhost:8000/admin` để đăng nhập :

    <img src=https://i.imgur.com/cnqdOdO.png>

- Sau khi đăng nhập thành công, **Admin** mặc định sẽ quản lý 2 bảng là :
    - `User` ( bảng lưu các user trong hệ thống) - bảng "`auth_user`"

        <img src=https://i.imgur.com/pO7WflF.png>
    - `Group` nhằm tạo các nhóm trong user với những quyền có thể thực thi riêng biệt trong hệ thống - bảng "`auth_group`" .
## **2) Đưa model cho Admin quản lý**
