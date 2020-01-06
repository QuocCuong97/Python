# Tạo WebApp và xử lý khi người dùng yêu cầu truy cập Python Django
- **WebApp** là nơi để tạo ra những trang web nằm trong toàn bộ hệ thống website .
- Trong 1 dự án, cần chia ra nhiều **WebApp** nhằm dễ quản lý và phân chia công việc .
    - **VD :** Tạo ra 1 **app** để quản lý các tác vụ đăng nhập, đăng xuất riêng, 1 **app** quản lý về trang chủ,... => Sau khi hoàn thành các **app**, sẽ có 1 wenbsite hoàn chỉnh .
## **1) Tạo WebApp**
- **B1 :** Để tạo 1 **WebApp** , sử dụng lệnh :
    ```
    $ python3 manage.py startapp [app_name]
    ```
    - **VD :**
        ```
        $ python3 manage.py startapp home
        ```
        - Sau khi tạo app `home` , thư mục `home` sẽ được tạo ra đứng cùng trong thư mục `ProjectWeb` :
            ```
            PythonWeb/
            ├── db.sqlite3
            ├── home
            │   ├── admin.py
            │   ├── apps.py
            │   ├── __init__.py
            │   ├── migrations
            │   │   └── __init__.py
            │   ├── models.py
            │   ├── tests.py
            │   └── views.py
            ├── manage.py
            └── PythonWeb
                ├── __init__.py
                ├── __pycache__
                │   ├── __init__.cpython-36.pyc
                │   ├── settings.cpython-36.pyc
                │   ├── urls.cpython-36.pyc
                │   └── wsgi.cpython-36.pyc
                ├── settings.py
                ├── urls.py
                └── wsgi.py

            4 directories, 17 files
            ```
- **B2 :** Khai báo cho Project biết ta vừa tạo 1 **App** mới ( mục đích chính là nếu sau này **app** có liên quan trong việc thiết kế các bảng trong **database** ) . Trong folder `PythonWeb` , mở file `settings.py` . Ở phần `INSTALLED_APPS` , thêm tên **app** vừa tạo :
    
    <img src=https://i.imgur.com/IY5mJKE.png>

- **B3 :** Cập nhật file `settings.py` :
    ```
    python3 manage.py migrate
    ```
    <img src=https://i.imgur.com/OUraLBC.png>

    > Nếu ta chạy `migrate` project lần đầu thì project **Django** sẽ tạo một số bảng cho chức năng user, admin cho database hiện tại. Bản chất **Django** hỗ trợ cho chúng ta hệ thống user, admin để thuận tiện cho việc phát triển trang web nhanh hơn.
## **2) Cách thức hoạt động của web Django**
### **2.1) Cách thức hoạt động của web**
<img src=https://i.imgur.com/FYQ1TrE.jpg>

- Phía Client chính là máy tính của người dùng, khi người dùng gửi 1 request bằng giao thức HTTP cho phía Server. Sau khi Server nhận được request, server sẽ phân tích xem người dùng yêu cầu thứ gì rồi sẽ response về cho máy người dùng.
### **2.2) Cách thức hoạt động của Django**
- Trước tiên , cần viết ra các hàm để xử lý những request của client gửi đến cho web server của mình .
- **B1 :** Viết một hàm xử lý file `views.py` trong app `home` :
    ```py
    from django.shortcuts import render
    from django.http import HttpResponse
    # Create your views here.
    def index(request):
        response = HttpResponse()
        response.writelines('<h1>Xin chào</h1>')
        response.write('Đây là app home')
        return response
    ```
    > Trong trường hợp này , đầu tiên sẽ import `HttpResponse` từ thư viện, sau đó sẽ viết 1 hàm `index` có tham số `request` - chính là request của người dùng trả về . Trong hàm này, tạo một instance `HttpResponse()` , sử dụng phương thức `writelines()` hay `write()` để viết nội dung html nằm trong response này . Cuối cùng sẽ return response để trả về máy người dùng .
- **B2 :** Xây dựng bộ `urls` để ứng với mỗi `url` trên trang web thì sẽ gọi hàm gì xử lý request đó . Ở app `home`, tạo thêm 1 file `urls.py` có nội dung sau :
    ```py
    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.index)
    ]
    ```




Tiếp theo ta sẽ phải xây dựng bộ urls để ứng với mỗi url trên trang web thì sẽ gọi hàm gì xử lý request đó. Ở app home, ta tạo thêm 1 file urls.py có nội dung như sau: