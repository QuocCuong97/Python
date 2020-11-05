# Application
- Ví dụ với đoạn code trên :
    ```py
    # app.py
    from flask import Flask
    app = Flask(__name__)


    @app.route('/')
    def hello_world():
        return 'Hello, World!'

    if __name__ == '__main__':
        app.run()
    ```
- Import module `flask` là bắt buộc trong project .
- Cấu trúc của 1 app Flask sẽ lấy tên của module `__name__` làm tham số truyền vào
- Hàm `route()` của Flask là một decorator, cho application biết URL nào khi gọi sẽ tương tác với function nào .
    ```
    app.route(rule, options)
    ```
    - `rule` đại diện cho URL dùng cho function
    > Như ở ví dụ trên, URL `/` sẽ map đến hàm `hello_world()`
- Cuối cùng là phương thức `run()` cho phép Flask chạy trên môi trường local :
    ```
    app.run(host, port, debug, options)
    ```
    - Trong đó :
        - `host` : host sẽ listen. Mặc định là `127.0.0.1(localhost)`, có thể set thành `0.0.0.0` để truy cập từ bên ngoài
        - `port` : mặc định là `5000`
        - `debug` : mặc định là false, nếu set là true, khi chạy sẽ được cung cấp thêm thông tin debug
        