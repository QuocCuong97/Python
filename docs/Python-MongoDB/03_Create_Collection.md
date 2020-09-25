# Work with Collection
- Một **collection** trong **MongoDB** tương tự với một **table** trong **SQL**
- Để khởi tạo một **collection** trong **MongoDB**, sử dụng database object và chỉ định tên của collection muốn tạo . **MongoDB** sẽ tạo ra **collection** nếu nó chưa tồn tại .
- **VD :**
    ```py
    import pymongo

    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]

    mycol = mydb["customers"]
    ```
    > Tại thời điểm tạo ra collection, database vẫn chưa thực sự được tạo ra . Nó chỉ được tạo ra khi collection chứa content .
    - Ta có thể kiểm tra lại và thấy không có database :
        ```py
        print(myclient.list_database_names())
        ```
        => Output :
        ```
        ['admin', 'config', 'local', 'test']
        ```