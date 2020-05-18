# Sử dụng Python truy vấn InfluxDB
- **B1 :** Cài đặt thư viện `influxdb` :
    ```py
    pip install influxdb
    ```
- **B2 :** Import thư viện :
    ```py
    from influxdb import InfluxDBClient
    ```
- **B3 :** Tạo kết nối :
    - Kết nối không có xác thực :
        ```py
        client = InfluxDBClient(host='localhost', port=8086)
        ```
    - Kết nối xác thực :
        ```py
        client = InfluxDBClient(host='mydomain.com', port=8086, username='myuser', password='mypass' ssl=True, verify_ssl=True)
        ```
- **B4 :** Các thao tác :
    - Tạo database :
        ```py
        client.create_database('pyexample')
        ```
    - Show database :
        ```py
        client.get_list_database()
        ```
    - Chuyển database để làm việc :
        ```py