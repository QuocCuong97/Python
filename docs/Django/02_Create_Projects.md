# Tạo Project với Django
## **1) Tạo Project**
- **B1 :** Nên tạo **virtual environment** trước khi sử dụng **Django** :
    ```sh
    $ virtualenv env_django 
    ```
    > Lệnh trên sẽ tạo ra một folder `env_django` chứa các thành phần cần thiết của **Python** .
- **B2 :** Truy cập **virtual environment** :
    ```sh
    $ source env_django/bin/activate
    (env_django) cuongnq@ubuntu1804:~/new_code$ 
    ```
- **B3 :** Tạo Project Web mới :
    ```sh
    $ django-admin startproject [project_name]
    ```
    - **VD :**
        ```sh
        $ django-admin startproject PythonWeb
        ```
        - Lệnh trên sẽ tạo ra 1 thư mục tên là `PythonWeb` ở trên thư mục hiện hành :
            ```sh
            PythonWeb/
            ├── manage.py
            └── PythonWeb
                ├── __init__.py
                ├── settings.py
                ├── urls.py
                └── wsgi.py

            1 directory, 5 files
            ```
## **2) Cấu trúc Project Django**
- Trong Project Python sẽ có 1 file `manage.py` và 1 folder cùng tên với Project .
- File `manage.py` giúp tương tác với Project qua các command ( như tạo tài khoản admin, tạo database , chạy server ảo,....) => không nên chỉnh sửa .
- Ở folder `PythonWeb` gồm 4 file :
    - `__init__.py` : đây là 1 file cơ bản trong **Python** dùng để biến folder chứa nó thành 1 package ,giúp ta có thể import .
    - `settings.py` : đây là file cấu hình project ( cấu hình database, đặt múi giờ, cài thêm thư viện,....)
    - `urls.py` : đây là file giúp tạo các đường dẫn urls của trang web để liên kết các webpage lại với nhau .
    - `wsgi.py` : đây là file giúp ta deploy project lên server .
## **3) Chạy web trên localhost**
- **B1 :** Di chuyển vào folder Project :
    ```
    $ cd ProjectWeb
    ```
- **B2 :** Sử dụng lệnh sau để khởi động server ảo :
    ```
    $ python manage.py runserver
    ```
    ```
    Watching for file changes with StatReloader
    Performing system checks...

    System check identified no issues (0 silenced).

    You have 17 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
    Run 'python manage.py migrate' to apply them.

    January 02, 2020 - 15:43:18
    Django version 3.0.2, using settings 'PythonWeb.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.
    ```
    - Truy cập địa chỉ `http://127.0.0.1:8000/` trên trình duyệt :

        <img src=https://i.imgur.com/FLQL8mW.png>

> Có thể thay đổi cổng `8000` mặc định của **Django** khi chạy :
```
$ python manage.py runserver [port]
```
- **VD :**
    ```
    $ python manage.py runserver 8080
    ```
    

          

