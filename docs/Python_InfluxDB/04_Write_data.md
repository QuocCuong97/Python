# Ghi dữ liệu vào InfluxDB
- Định dạng 1 cấu trúc dữ liệu đầu vào :
    ```py
    data = [
        {
            "measurement": "cpu",            # tên measurements
            "tags": {         
                "cpu": "cpu5",               # tag key-value
                "host": "centos7-03"
            },
            "time": "2009-11-10T23:00:00Z",  # time ISO 8061
            "fields": {                      # field key-value     
                "usage_guest": 0.64,
                "usage_guest_nice": 0,
                "usage_idle": 0,
                "usage_iowait": 0,
                "usage_irq": 0,
                "usage_nice": 0,
                "usage_softirq": 0,
                "usage_steal ": 0,
                "usage_system ": 0,
                "usage_user": 0,
            }
        }
    ]
    ```
- Ghi dữ liệu :
    ```py
    >>> client.write_points(data)
    ```