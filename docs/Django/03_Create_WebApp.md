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
    > Đây là cách import thêm class path để định nghĩa các urls và views từ app `home` . Ở đây ta tạo biến `urlpatterns` là một list chứa các path tồn tại trong app `home` . Ta tạo path có đường dẫn trắng và tương ứng gắn hàm `index` từ module `views.py`
- **B3 :** Quay lại folder `PythonWeb`, chỉnh sửa file `urls.py` như sau :
    ```py
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
      path('admin/', admin.site.urls),
      path('home', include('home.urls')),
    ]
    ```
    > Đầu tiên thêm hàm `include` từ thư viện `urls` . Trong list `urlpatterns`, thêm một path có 2 tham số truyền vào : đầu tiên là path của `home`, thứ hai là hàm `include()` chứa tham số là `home.urls` - file `urls.py` trong app `home` .
- **B4 :** Chạy server : `python3 manage.py runserver`
    - Hiện tại web server chỉ có 2 đường dẫn là `/admin` (có sẵn) và `/home` (vừa tạo) . Nếu chỉ vào `localhost:8000` thì sẽ trả về lỗi `404` :

        <img src=https://i.imgur.com/c48xHVy.png>

    - Truy cập địa chỉ : `localhost:8000/admin` :

        <img src=https://i.imgur.com/ZAELYjS.png>
    
    - Truy cập địa chỉ : `localhost:8000/home` :

        <img src=https://i.imgur.com/yQtHLOG.png>

    > Nếu muốn khi truy cập `localhost:8000` sẽ vào thẳng file `views.py` , chỉ cần xóa trắng path của app `home` :
    ```py
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
      path('admin/', admin.site.urls),
      path('', include('home.urls')),
    ]
    ```

> ### Tổng kết nguyên lý hoạt động của **Django** :

<img src=https://i.imgur.com/Xj2Yh8F.png>

## **3) Viết test case đơn giản**
- Trong lập trình , luôn luôn cần kiểm thử phần mềm ( **tester** ) .
- Ta có thể viết một vài test case đơn giản để đưa cho đội ngũ **tester** .
- Thêm các test case vào file `tests.py` trong app :
    ```py
    from django.test import TestCase, SimpleTestCase

    # Create your tests here.
    class SimpleTest(SimpleTestCase):
        def test_home_page_status(self):
            response = self.client.get('/')
            self.assertEquals(response.status_code, 200)
    ```
    > Trong trường hợp này, ta import class `SimpleTestCase` là class con của `TestCase`, sau đó khai báo mới một class `SimpleTest` kế thừa `SimpleTestCase` . Trong class `TestCase` thì các method test mặc định phải đặt tên theo cú pháp "`test_[name]`"
- Thử tắt server ( `Ctrl + C` ) và chạy test :
    ```
    $ python3 manage.py test
    ```
    ```
    System check identified no issues (0 silenced).
    .
    ----------------------------------------------------------------------
    Ran 1 test in 0.002s

    OK
    ```
    => Không có lỗi
    > Nếu có nhiều app và muốn test riêng từng app thì sử dụng lệnh :
        
    ```
    $ python3 manage.py test [app_name]
    ```
