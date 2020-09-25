# Insert document into Collection
- Một **document** trong **MongoDB** tương tự với một **table** trong **SQL** 
- Để insert một documentation, ta sử dụng phương thức `insert_one()` . Tham số đầu tiên của phương thức `insert_one()` sẽ là một dict chứa name và value của mỗi field trong document .
- **VD :**
    ```py
    import pymongo

    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]
    mycol = mydb["customers"]

    mydict = { "name": "John", "address": "Highway 37" }

    x = mycol.insert_one(mydict)
    ```
    - Lúc này, database `mydatabase` mới thực sự được tạo ra :
        ```
        ['admin', 'config', 'local', 'mydatabase', 'test']
        ```
### **Trả về ID của document**
- Khi insert document, nếu không chỉ định `_id` thì một `_id` duy nhất sẽ được tạo ra cho mỗi document .
- Như trên ví dụ trên, ta không chèn ID vào trong `mydict`, vì vậy **MongoDB** sẽ gán một `_id` duy nhất cho document .
- Cách kiểm tra `_id` của document khi tạo :
    ```py
    mydict = { "name": "Peter", "address": "Lowstreet 27" }

    x = mycol.insert_one(mydict)

    print(x.inserted_id)
    ```
    => Output :
    ```
    5f6dad3e52a6ceb0af11a99f
    ```
    > Phương thức `insert_one()` trả về **InsertOneResultObject** có các thuộc tính, trong đó `inserted_id` nắm giữ ID của document .
### **Insert nhiều document** 
- Để insert nhiều document cùng một lúc vào collection trong **MongoDB**, sử dụng phương thức `insert_many()` . Tham số đầu tiên của phương thức `insert_many()` là một list bao gồm các dict chứa data muốn insert .
- **VD :**
    ```py
    import pymongo

    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]
    mycol = mydb["customers"]

    mylist = [
        { "name": "Amy", "address": "Apple st 652"},
        { "name": "Hannah", "address": "Mountain 21"},
        { "name": "Michael", "address": "Valley 345"},
        { "name": "Sandy", "address": "Ocean blvd 2"},
        { "name": "Betty", "address": "Green Grass 1"},
        { "name": "Richard", "address": "Sky st 331"},
        { "name": "Susan", "address": "One way 98"},
        { "name": "Vicky", "address": "Yellow Garden 2"},
        { "name": "Ben", "address": "Park Lane 38"},
        { "name": "William", "address": "Central st 954"},
        { "name": "Chuck", "address": "Main Road 989"},
        { "name": "Viola", "address": "Sideway 1633"}
    ]

    x = mycol.insert_many(mylist)

    #print list of the _id values of the inserted documents:
    print(x.inserted_ids)
    ```
    => Output :
    ```
    [ObjectId('5f6db09f853128e2ff609d47'), ObjectId('5f6db09f853128e2ff609d48'), ObjectId('5f6db09f853128e2ff609d49'), ObjectId('5f6db09f853128e2ff609d4a'), ObjectId('5f6db09f853128e2ff609d4b'), ObjectId('5f6db09f853128e2ff609d4c'), ObjectId('5f6db09f853128e2ff609d4d'), ObjectId('5f6db09f853128e2ff609d4e'), ObjectId('5f6db09f853128e2ff609d4f'), ObjectId('5f6db09f853128e2ff609d50'), ObjectId('5f6db09f853128e2ff609d51'), ObjectId('5f6db09f853128e2ff609d52')]
    ```
    > Phương thức `insert_many()` sẽ trả lại **InsertManyResultObject** có các thuộc tính, trong đó `inserted_ids` nắm giữ ID của các document .
### **Insert nhiều document với ID gán sẵn**
- Có thể chủ động gán ID cho document, nhưng cần lưu ý, các document không được có ID trùng nhau .
- **VD :**
    ```py
    import pymongo

    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]
    mycol = mydb["customers"]

    mylist = [
        { "_id": 1, "name": "John", "address": "Highway 37"},
        { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
        { "_id": 3, "name": "Amy", "address": "Apple st 652"},
        { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
        { "_id": 5, "name": "Michael", "address": "Valley 345"},
        { "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
        { "_id": 7, "name": "Betty", "address": "Green Grass 1"},
        { "_id": 8, "name": "Richard", "address": "Sky st 331"},
        { "_id": 9, "name": "Susan", "address": "One way 98"},
        { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
        { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
        { "_id": 12, "name": "William", "address": "Central st 954"},
        { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
        { "_id": 14, "name": "Viola", "address": "Sideway 1633"}
    ]

    x = mycol.insert_many(mylist)

    #print list of the _id values of the inserted documents:
    print(x.inserted_ids)
    ```
    => Output :
    ```
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    ```