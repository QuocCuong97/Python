# Working with Database
- Kết nối **MongoDB** :
    ```py
    import pymongo

    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    ```
- Kết nối đến database :
    ```py
    mydb = myclient["mydatabase"]
    ```
    > Lệnh trên sẽ kết nối đến database `mydatabase` hoặc tạo ra và liên kết đến nó nếu nó không tồn tại. Tuy nhiên, một database sẽ không thực sự được tạo ra cho đến khi nó có nội dung. **MongoDB** sẽ chờ cho đến khi người dùng tạo ra các collection (table) với tối thiểu 1 document (record) thì database mới thực sự tồn tại .
- Kiểm tra các database đang có :
    ```py
    myclient.list_database_names()
    ```
    - **VD :**
        ```py
        print(myclient.list_database_names())
        ```
        => Output :
        ```
        ['admin', 'config', 'local', 'test']
        ```
