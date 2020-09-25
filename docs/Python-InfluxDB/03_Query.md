# Query dữ liệu
- Cú pháp truy vấn dữ liệu dạng thô :
    ```py
    >>> client.query(query)
    ```
    - **VD :**
        ```py
        >>> query = """select usage_nice from "cpu" WHERE "cpu" = 'cpu5'"""
        >>> client.query(query)
        ```
        => Output:
        ```
        [{'time': '2009-11-10T23:00:00Z', 'cpu': 'cpu5', 'host': 'centos7-03', 'usage_guest': 0.64, 'usage_guest_nice': 0.0, 'usage_idle': 0.0, 'usage_iowait': 0.0, 'usage_irq': 0.0, 'usage_nice': 0.0, 'usage_softirq': 0.0, 'usage_steal': None, 'usage_steal ': 0, 'usage_system': None, 'usage_system ': 0, 'usage_user': 0.0}]
        ```
    > Lưu ý : Đối với cách này, các dữ liệu nhạy cảm sẽ bị lộ qua phương thức **SQL Injection**
- Cú pháp truy vấn dữ liệu dạng bind_params :
    ```py
    >>> client.query(query, params=None, bind_params=None, epoch=None, expected_response_code=200, database=None, raise_errors=True, chunked=False, chunk_size=0, method=u’GET’)
    ```
    - **VD :**
        ```py
        >>> query = 'select * from cpu where host=$host;'
        >>> bind_params = {'host': 'centos7-03'}
        result = client.query(query, bind_params=bind_params)
        ```
- Kết quả truy vấn sẽ được trả về ở dạng **`ResultSet`** . Kết quả dạng này sẽ có các phương thức sau :
    - `get_points(measurement=None, tags=None)` : phương thức lọc dữ liệu qua measurement và tags
    - `items()` : trả về một list các tuple các item của **ResultSet**
    - `key()` : trả về một list các tuple các key của **ResultSet**
    - `raw` : trả về dữ liệu json từ InfluxDB
    ```py
    >>> rs = cli.query("SELECT * from cpu")
    ```
    - Lọc theo measurement :
        ```py
        >>> cpu_points = list(rs.get_points(measurement='host'))
        ```
    - Lọc theo tag :
        ```py
        >>> cpu_points = list(rs.get_points(tags={"host_name": "centos7-03"}))
        ```
    - Lọc theo cả measurement và tag :
        ```py
        >>> cpu_points = list(rs.get_points(measurement='cpu', tags={'host_name': 'centos7-03'}))
        ```