# Working with Database
### **Truy cập Database để làm việc**
- Kết nối không có xác thực :
    ```py
    >>> client = InfluxDBClient(host='localhost', port=8086)
    ```
- Kết nối xác thực :
    ```py
    client = InfluxDBClient(host='mydomain.com', port=8086, username='myuser', password='mypass' ssl=True, verify_ssl=True)
    ```
- Tạo kết nối với database cụ thể :
    ```py
    >>> client = InfluxDBClient(host='192.168.5.30', port=8086, database='telegraf')
    ```
- Kết nối qua UDP :
    ```py
    >>> client = InfluxDBClient(host='192.168.5.30', database='dbname', use_udp=True, udp_port=4444)
    ```
- Đóng kết nối :
    ```py
    >>> client.close()
    ```
- Kiểm tra kết nối (lệnh sẽ trả về version của InfluxDB):
    ```py
    >>> client.ping()
    ```
    ```
    1.8.1
    ```
### **Tạo Database**
- Tạo database :
    ```py
    >>> client.create_database('pyexample')
    ```
### **Xóa Database**
- Xóa database :
    ```py
    >>> client.drop_database('pyexample')
    ```
### **Chuyển đổi Database làm việc**
- Chuyển đổi database làm việc :
    ```py
    >>> client.switch_database(database_name)
    ```
### **Show các Database**
- Show database :
    ```py
    >>> client.get_list_database()
    ```
    ```
    [{'name': '_internal'}, {'name': 'telegraf'}, {'name': 'pyexample'}]
    ```
### **Show các Measurement**
- Show các measurement :
    ```py
    >>> client.get_list_measurements()
    ```
    ```
    [{'name': 'cpu'}, {'name': 'disk'}, {'name': 'diskio'}, {'name': 'kernel'}, {'name': 'mem'}, {'name': 'net'}, {'name': 'processes'}, {'name': 'swap'}, {'name': 'system'}]
    ```
