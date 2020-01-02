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