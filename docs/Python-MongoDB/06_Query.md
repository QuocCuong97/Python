# Query
### **Lọc kết quả**
- Khi tìm kiếm document trong collection, có thể filter kết quả bằng các sử dụng query object .
- Tham số đầu tiên của phương thức `find()` là query object, được sử dụng để giới hạn kết quả tìm kiếm .
- **VD :** Tìm document có field `address` có giá trị "`Park Lane 38`" :
    ```py
    mydb = myclient["mydatabase"]
    mycol = mydb["customers"]

    myquery = { "address": "Park Lane 38" }

    mydoc = mycol.find(myquery)

    for x in mydoc:
        print(x)
    ```
    => Output :
    ```
    {'_id': ObjectId('5f6db09f853128e2ff609d4f'), 'name': 'Ben', 'address': 'Park Lane 38'}
    ```

### **Query nâng cao**
- Để thực hiện các truy vấn nâng cao, có thể sử dụng modifier
To make advanced queries you can use modifiers as values in the query object.
- **VD :** Để tìm kiếm document có field "`address`" bắt đầu với chữ cái "`S`" hoặc cao hơn (theo thứ tự bảng chữ cái), sử dụng cấu trúc greater : `{"$gt": "S"}` :
    ```py
    mydb = myclient["mydatabase"]
    mycol = mydb["customers"]

    myquery = { "address": { "$gt": "S" } }

    mydoc = mycol.find(myquery)

    for x in mydoc:
        print(x)
    ```
    => Output :
    ```
    {'_id': ObjectId('5f6db09f853128e2ff609d49'), 'name': 'Michael', 'address': 'Valley 345'}
    {'_id': ObjectId('5f6db09f853128e2ff609d4c'), 'name': 'Richard', 'address': 'Sky st 331'}
    {'_id': ObjectId('5f6db09f853128e2ff609d4e'), 'name': 'Vicky', 'address': 'Yellow Garden 2'}
    {'_id': ObjectId('5f6db09f853128e2ff609d52'), 'name': 'Viola', 'address': 'Sideway 1633'}
    ```
### **Sử dụng Regular Expression để tìm kiếm**
- Có thể sử dụng **regular expression** để hỗ trợ truy vấn tốt hơn .
- Để tìm kiếm chỉ những document nào có field "`address`" bắt đầu bằng chữ cái "`S`", sử dụng cú pháp **regular expression** : `{"$regex": "^S"}` :
    ```py
    mydb = myclient["mydatabase"]
    mycol = mydb["customers"]

    myquery = { "address": { "$regex": "^S" } }

    mydoc = mycol.find(myquery)

    for x in mydoc:
        print(x)
    ```
    => Output :
    ```
    {'_id': ObjectId('5f6db09f853128e2ff609d4c'), 'name': 'Richard', 'address': 'Sky st 331'}
    {'_id': ObjectId('5f6db09f853128e2ff609d52'), 'name': 'Viola', 'address': 'Sideway 1633'}
    ```
