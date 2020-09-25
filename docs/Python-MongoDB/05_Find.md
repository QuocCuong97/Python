# Find
- Trong **MongoDB**, ta sử dụng phương thức `find` và `findOne` để tìm kiếm data bên trong collection . Các phương thức này cũng tương tự như mệnh đề `SELECT` để tìm dữ liệu từ table trong **SQL** .
### **Fine One - `find_one()`**
- Để select data từ một collection trong**MongoDB**, ta có thể sử dụng phương thức `find_one()` .
- Phương thức `find_one()` sẽ trả về giá trị đầu tiên trong vùng chọn .
- **VD :**
    ```py
    mycol = mydb["customers"]

    x = mycol.find_one()

    print(x)
    ```
    => Output :
    ```
    {'_id': ObjectId('5f6dab2c87575ae708670be4'), 'name': 'John', 'address': 'Highway 37'}
    ```
### **Find All - `find()`**
- Để select toàn bộ data từ một collection trong **MongoB**, ta có thể sử dụng phương thức `find()` .
- Phương thức `find()` trả về tất cả các giá trị trong vùng chọn .
- Tham số đầu tiên của phương thức `find()` là một query object . Nếu không sử dụng query object, phương thức sẽ select toàn bộ các document trong collection .
- **VD :**
    ```py
    mycol = mydb["customers"]

    for x in mycol.find():
        print(x)
    ```
    => Output :
    ```
    {'_id': ObjectId('5f6dab2c87575ae708670be4'), 'name': 'John', 'address': 'Highway 37'}
    {'_id': ObjectId('5f6dad3e52a6ceb0af11a99f'), 'name': 'John', 'address': 'Highway 37'}
    {'_id': ObjectId('5f6db09f853128e2ff609d47'), 'name': 'Amy', 'address': 'Apple st 652'}
    {'_id': ObjectId('5f6db09f853128e2ff609d48'), 'name': 'Hannah', 'address': 'Mountain 21'}
    {'_id': ObjectId('5f6db09f853128e2ff609d49'), 'name': 'Michael', 'address': 'Valley 345'}
    {'_id': ObjectId('5f6db09f853128e2ff609d4a'), 'name': 'Sandy', 'address': 'Ocean blvd 2'}
    {'_id': ObjectId('5f6db09f853128e2ff609d4b'), 'name': 'Betty', 'address': 'Green Grass 1'}
    {'_id': ObjectId('5f6db09f853128e2ff609d4c'), 'name': 'Richard', 'address': 'Sky st 331'}
    {'_id': ObjectId('5f6db09f853128e2ff609d4d'), 'name': 'Susan', 'address': 'One way 98'}
    {'_id': ObjectId('5f6db09f853128e2ff609d4e'), 'name': 'Vicky', 'address': 'Yellow Garden 2'}
    {'_id': ObjectId('5f6db09f853128e2ff609d4f'), 'name': 'Ben', 'address': 'Park Lane 38'}
    {'_id': ObjectId('5f6db09f853128e2ff609d50'), 'name': 'William', 'address': 'Central st 954'}
    {'_id': ObjectId('5f6db09f853128e2ff609d51'), 'name': 'Chuck', 'address': 'Main Road 989'}
    {'_id': ObjectId('5f6db09f853128e2ff609d52'), 'name': 'Viola', 'address': 'Sideway 1633'}
    ```
### **Tìm kiếm với các field cụ thể**
- Tham số thứ 2 trong phương thức `find()` là một object mô tả các field sẽ trả ra trong kết quả . Tham số này không bắt buộc, nếu không có nó, mặc định sẽ trả về tất cả các field .
- **VD :**
    ```py
    mydb = myclient["mydatabase"]
    mycol = mydb["customers"]

    for x in mycol.find({},{ "_id": 0, "name": 1, "address": 1 }):
        print(x)
    ```
    => Output :
    ```
    {'name': 'John', 'address': 'Highway 37'}
    {'name': 'John', 'address': 'Highway 37'}
    {'name': 'Amy', 'address': 'Apple st 652'}
    {'name': 'Hannah', 'address': 'Mountain 21'}
    {'name': 'Michael', 'address': 'Valley 345'}
    {'name': 'Sandy', 'address': 'Ocean blvd 2'}
    {'name': 'Betty', 'address': 'Green Grass 1'}
    {'name': 'Richard', 'address': 'Sky st 331'}
    {'name': 'Susan', 'address': 'One way 98'}
    {'name': 'Vicky', 'address': 'Yellow Garden 2'}
    {'name': 'Ben', 'address': 'Park Lane 38'}
    {'name': 'William', 'address': 'Central st 954'}
    {'name': 'Chuck', 'address': 'Main Road 989'}
    {'name': 'Viola', 'address': 'Sideway 1633'}
    ```
- **Chú ý 1 :** không được phép chỉ định cả giá trị `0` và `1` trong cùng một object (trừ trường hợp một trong các field là `_id`). Nếu chỉ định field với giá trị `0`, tất cả các field khác sẽ là `1` - field set là `0` sẽ không được hiển thị :
    ```py
    mydb = myclient["mydatabase"]
    mycol = mydb["customers"]

    for x in mycol.find({},{ "address": 0 }):
        print(x)
    ```
    => Output :
    ```
    {'_id': ObjectId('5f6dab2c87575ae708670be4'), 'name': 'John'}
    {'_id': ObjectId('5f6dad3e52a6ceb0af11a99f'), 'name': 'John'}
    {'_id': ObjectId('5f6db09f853128e2ff609d47'), 'name': 'Amy'}
    {'_id': ObjectId('5f6db09f853128e2ff609d48'), 'name': 'Hannah'}
    {'_id': ObjectId('5f6db09f853128e2ff609d49'), 'name': 'Michael'}
    {'_id': ObjectId('5f6db09f853128e2ff609d4a'), 'name': 'Sandy'}
    {'_id': ObjectId('5f6db09f853128e2ff609d4b'), 'name': 'Betty'}
    {'_id': ObjectId('5f6db09f853128e2ff609d4c'), 'name': 'Richard'}
    {'_id': ObjectId('5f6db09f853128e2ff609d4d'), 'name': 'Susan'}
    {'_id': ObjectId('5f6db09f853128e2ff609d4e'), 'name': 'Vicky'}
    {'_id': ObjectId('5f6db09f853128e2ff609d4f'), 'name': 'Ben'}
    {'_id': ObjectId('5f6db09f853128e2ff609d50'), 'name': 'William'}
    {'_id': ObjectId('5f6db09f853128e2ff609d51'), 'name': 'Chuck'}
    {'_id': ObjectId('5f6db09f853128e2ff609d52'), 'name': 'Viola'}
    ```
- **Chú ý 2 :** Sẽ xảy ra lỗi nếu set cả `0` và `1` cho cùng một object (trừ trường hợp `0` được set cho `_id`) :
    ```py
    mydb = myclient["mydatabase"]
    mycol = mydb["customers"]

    for x in mycol.find({},{ "name": 1, "address": 0 }):
        print(x)
    ```
    => Output :
    ```
    pymongo.errors.OperationFailure: Cannot do exclusion on field address in inclusion projection, full error: {'ok': 0.0, 'errmsg': 'Cannot do exclusion on field address in inclusion projection', 'code': 31254, 'codeName': 'Location31254'}
    ```