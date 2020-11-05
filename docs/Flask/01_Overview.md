# Tổng quan về Flask
## **1) Giới thiệu**
## **2) Cài đặt Flask**
- **B1 :** Cài đặt `virtualenv` :
    ```
    # pip3 install virtualenv
    ```
- **B2 :** Tạo env :
    ```
    # mkdir flask_app
    # cd flask_app
    # virtualenv -p /usr/bin/python3.6 env
    # source env/bin/active
    (env) #
    ```
- **B3 :** Cài đặt `flask` :
    ```
    # pip install flask
    ```
- **B4 :** Chạy thử 1 app đơn giản :
    - Tạo 1 file `app.py` trong thư mục `flask_app` :
        ```
        flask_app/
        ├── app.py
        └── env
        ```
    - Tạo nội dung cho file `app.py` :
        ```py
        from flask import Flask
        app = Flask(__name__)


        @app.route('/')
        def hello_world():
            return 'Hello, World!'

        if __name__ == '__main__':
            app.run()
        ```
    - Chạy project :
        ```
        # flask run
        ```
        hoặc 
        ```
        # python app.py
        ```
        Output :
        ```
         * Environment: production
        Use a production WSGI server instead.
        * Debug mode: off
        * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
        ....
        ``` 
    - Truy cập trình duyệt để kiểm tra :
        ```
        http://127.0.0.1:5000/
        ```
        <img src=https://i.imgur.com/iqGa2OT.png>