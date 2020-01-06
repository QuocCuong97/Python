# File tĩnh và sử dụng Bootstrap
## **1) Giới thiệu**
- Trong việc thiết kế website chúng ta sẽ có những file tĩnh để gắn vào các **template** như các file hình ảnh, **CSS** hay **Javascript** tách riêng ra để giúp chúng ta dễ quản lý hơn .
- **Bootstrap** là một framework của **CSS** để giúp thiết kế website tiện lợi hơn, đặc biệt là dành cho **responsive web** .

    <img src=https://i.imgur.com/QoSnBud.png>

- **Responsive Web** là trang web có thể hiển thị co giãn theo màn hình các thiết bị như máy tính, tablet, điện thoại để có thể thích ứng về layout, giữ tính thẩm mỹ .

    <img src=https://i.imgur.com/lc9EPdF.png>
## **2) Lưu tĩnh thư viện Bootstrap**
- **B1 :** Download **Bootstrap** tại [trang chủ](https://getbootstrap.com/docs/4.4/getting-started/download/) :

    <img src=https://i.imgur.com/IAVcpcI.png>

- **B2 :** Giải nén file zip vừa tải về :
    ```sh
    $ unzip bootstrap-4.4.1-dist.zip
    ```
    ```
    bootstrap-4.4.1-dist
    ├── css
    └── js

    2 directories, 0 files
    ```
- **B3 :** Tạo mới thư mục `static` trong Project , copy 2 thư mục `css` và `js` vào trong :
    ```
    PythonWeb/
    ├── db.sqlite3
    ├── home
    ├── manage.py
    ├── PythonWeb
    └── static
        ├── css
        └── js
    ```
- **B4 :** Kiểm tra đường dẫn thư mục `static` trong file `settings.py` . File `settings.py` đã mặc định rằng muốn lấy các file tĩnh sẽ thông qua url `'/static/'` :
    
    <img src=https://i.imgur.com/p0Z5L8q.png>

- **B5 :** Map đường dẫn thư mục `static` vào trong file `settings.py` ( thêm đoạn code vào cuối file ) :
    ```sh
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "static"),
    ]
    ```
    - Trong đó :
        - `STATICFILES_DIRS` : dict lưu trữ đường dẫn folder chứa các file tĩnh .
        - `BASE_DIR` : tượng trưng cho đường dẫn hiện tại của project , thường được khai báo ở đầu file `settings.py` :
            <img src=https://i.imgur.com/R9nNukp.png>
    
- **B6 :** Có thể kiểm tra xem đã map thành công chưa bằng cách thử truy cập địa chỉ : `http://localhost:8000/static/css/bootstrap.css`

    <img src=https://i.imgur.com/Iko3obX.png>

- **B7 :** Để **template** có thể sử dụng các file tĩnh, gọi câu lệnh sau ở các **template** ( ở file `base.html` ) :
    ```html
    {% load static %}
    ```
    - Lồng file `bootstrap.min.css` :
        ```html
        <link rel="stylesheet" type="text/css" href="{% static 'css/bootstrap.min.css' %}">
        ```
    - Lồng file `bootstrap.min.js` :
        ```html
        <script src="{% static 'js/bootstrap.min.js' %}"></script>
        ```
    - Lồng hình ảnh :
        ```html
        <img src="{% static 'my_app/example.jpg' %}" alt="My image">
        ```
    
        <img src=https://i.imgur.com/IOxaPQm.png>