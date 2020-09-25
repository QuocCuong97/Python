# Limit
- Để giới hạn số kết quả truy vấn trong **MongoDB**, sử dụng phương thức `limit()` .
- Phương thức `limit()` sẽ lấy vào 1 tham số là số kết quả muốn trả về .
- **VD :**
    ```py
    mydb = myclient["mydatabase"]
    mycol = mydb["customers"]

    myresult = mycol.find().limit(5)

    #print the result:
    for x in myresult:
        print(x)
    ```
    => Output :
    ```
    {'_id': ObjectId('5f6dab2c87575ae708670be4'), 'name': 'John', 'address': 'Highway 37'}
    {'_id': ObjectId('5f6dad3e52a6ceb0af11a99f'), 'name': 'John', 'address': 'Highway 37'}
    {'_id': ObjectId('5f6db09f853128e2ff609d47'), 'name': 'Amy', 'address': 'Apple st 652'}
    {'_id': ObjectId('5f6db09f853128e2ff609d48'), 'name': 'Hannah', 'address': 'Mountain 21'}
    {'_id': ObjectId('5f6db09f853128e2ff609d49'), 'name': 'Michael', 'address': 'Valley 345'}
    ```