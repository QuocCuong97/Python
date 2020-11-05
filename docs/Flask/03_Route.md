# Route
- Các web framework hiện đại sử dụng công nghệ routing để giúp user ghi nhớ các URL của app. Điều này sẽ rất hữu ích khi muốn truy cập vào trang mong muốn mà không cần điều hướng từ trang chủ .
- Decorator `route()` trong Flask được sử dụng để bind URL tới function. Ví dụ :
    ```py
    @app.route(‘/hello’)
    def hello_world():
        return ‘hello world’
    ```
- Ở đây URL '`/hello`' sẽ bound đến hàm `hello_world()`. Do đó, khi truy cập `http://localhost:5000/hello`, output của hàm `hello_world()` sẽ được render ra browser .
- Hàm `add_url_rule()` cũng được sử dụng để bind URL giống như trên . Ví dụ :
    ```py
    def hello_world():
        return ‘hello world’
    app.add_url_rule(‘/’, ‘hello’, hello_world)
    ```
### **Các rule trong Flask**
- [Tham khảo](https://www.tutorialspoint.com/flask/flask_variable_rules.htm)