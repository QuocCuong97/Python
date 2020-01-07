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

    - Giao diện sau khi đăng nhập :

        <img src=https://i.imgur.com/R7B20Ym.png>
- Sau khi đăng nhập thành công, **Admin** mặc định sẽ quản lý 2 bảng là :
    - `User` ( bảng lưu các user trong hệ thống) - bảng "`auth_user`"

        <img src=https://i.imgur.com/ZVcQnTB.png>
    - `Group` nhằm tạo các nhóm trong user với những quyền có thể thực thi riêng biệt trong hệ thống - bảng "`auth_group`" .

        <img src=https://i.imgur.com/enxcBvc.png>

## **2) Đưa model cho Admin quản lý**
- Có thể đưa các **model** vào trang quản lý admin để có thể quản lý số lượng, tên bài viết,.....
- Truy cập file `admin.py` trong app , chỉnh sửa theo mẫu sau để đưa bảng `Posts` vào quản lý :

    <img src=https://i.imgur.com/EQjGSN5.png>

    - Giao diện trang chủ sau khi reload :

        <img src=https://i.imgur.com/A9YZxRl.png>

    - Click vào `Posts` sẽ thấy 2 bài viết đã tạo từ trước :

        <img src=https://i.imgur.com/HZdn5Ag.png>

    > Có thể tạo, chỉnh sửa, xóa bài viết ngay trên giao diện web của **Django** .
## **3) Một số cách tuỳ biến trang Admin**
- **Django** có thể hỗ trợ cho ta tuỳ biến hệ thống Admin .
### **3.1) Thêm các cột hiển thị**
- Mặc định thì trang quản lý `Post` mới cho phép hiển thị một cột `title` đầu tiên của bài viết .
- Khởi tạo 1 class tên `PostAdmin` , kế thừa class `admin.ModelAdmin` để chứa các tùy biến . Khởi tạo biến `list_display` kiểu list chứa 2 field `title` và `date` . Sau đó register `PostAdmin` cùng với `Post` :
    
    <img src=https://i.imgur.com/d558lAs.png>

    - Reload lại trang web để kiểm tra kết quả :

        <img src=https://i.imgur.com/KIlUOeF.png>

### **3.2) Thêm bộ lọc filter để lọc bài viết**
- Thêm biến list `list_filter` chứa giá trị là trường `date` để filter cho trường `date` :

    <img src=https://i.imgur.com/zFTnrME.png>

    - Reload lại trang web để kiểm tra kết quả :

        <img src=https://i.imgur.com/HH8et1U.png>
### **3.3) Thêm thanh tìm kiếm (Search)**
- Thêm biến list `search_fields` chứa giá trị là trường `title` để tìm kiếm theo `title` :

    <img src=https://i.imgur.com/GsAtZGt.png>

    - Reload lại trang web để kiểm tra kết quả :

        <img src=https://i.imgur.com/6K2cFkF.png>
### **3.4) Tạo title**
- Thêm biến `fieldset` theo cấu trúc sau để tạo tiêu đề khi chỉnh sửa bài viết :

    <img src=https://i.imgur.com/XC1CaFV.png>

    - Reload lại trang web để kiểm tra kết quả :

        <img src=https://i.imgur.com/EA5O41y.png>