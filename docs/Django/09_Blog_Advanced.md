# Customize trang Blog
## **1) Liệt kê danh sách bài viết trên trang chủ**
- Truy cập file `views.py` trong app `blog` để chỉnh sửa :
    - **B1 :** Import model `Post` để có thể truy vấn dữ liệu .
    - **B2 :** Tạo hàm `list` để xử lý request yêu cầu liệt kê bài viết .
    - **B3 :** Tạo 1 biến `Data` dạng **dict** , có key là "`Posts`" với giá trị là câu truy vấn lấy toàn bộ bài viết và được sắp xếp theo "`-date`" - có nghĩa là `date` mới nhất sẽ ở đầu tiên .
    - **B4 :** Render sang template `blog.html` , đưa `Data` vào tham số cuối để template dùng dữ liệu tạo giao diện .
        
        <img src=https://i.imgur.com/VRf4MV6.png>

- Tạo mới file `blog.html` theo đường dẫn `template/blog/blog.html` :
    ```html
    {% extends "pages/base.html" %}
    {% block title %}Blog{% endblock %}
    {% block content %}
    {% for post in Posts %}
    <h4>{{post.date|date:"d-m-Y"}}<a href="#">{{post.title}}</a></h4>
    {% endfor %}
    {% endblock %}
    ```
- Tạo path trong file `urls.py` trong app `blog` :
    
    <img src=https://i.imgur.com/HctdEWL.png>

- Tạo path trong file `urls.py` của Project :

    <img src=https://i.imgur.com/pGCysFN.png>

- RunServer và truy cập đường dẫn `localhost:8000/blog` để kiểm chứng :

    <img src=https://i.imgur.com/Rze8DC1.png>
