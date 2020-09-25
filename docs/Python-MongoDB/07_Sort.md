# Sort
### **Sort kết quả**
- Sử dụng phương thức `sort()` để sort kết quả theo chiều tăng dần hoặc giảm dần .
- Phương thức `sort()` nhận một tham số là ***tên field*** và một tham số là ***direction***  (mặc định là tăng dần)
- **VD :**
    ```py
    mydb = myclient["mydatabase"]
    mycol = mydb["customers"]

    mydoc = mycol.find().sort("name")

    for x in mydoc:
        print(x)
    ```
    => Output :
    ```
    {'_id': ObjectId('5f6db09f853128e2ff609d47'), 'name': 'Amy', 'address': 'Apple st 652'}
    {'_id': ObjectId('5f6db09f853128e2ff609d4f'), 'name': 'Ben', 'address': 'Park Lane 38'}
    {'_id': ObjectId('5f6db09f853128e2ff609d4b'), 'name': 'Betty', 'address': 'Green Grass 1'}
    {'_id': ObjectId('5f6db09f853128e2ff609d51'), 'name': 'Chuck', 'address': 'Main Road 989'}
    {'_id': ObjectId('5f6db09f853128e2ff609d48'), 'name': 'Hannah', 'address': 'Mountain 21'}
    {'_id': ObjectId('5f6dab2c87575ae708670be4'), 'name': 'John', 'address': 'Highway 37'}
    {'_id': ObjectId('5f6dad3e52a6ceb0af11a99f'), 'name': 'John', 'address': 'Highway 37'}
    {'_id': ObjectId('5f6db09f853128e2ff609d49'), 'name': 'Michael', 'address': 'Valley 345'}
    {'_id': ObjectId('5f6db09f853128e2ff609d4c'), 'name': 'Richard', 'address': 'Sky st 331'}
    {'_id': ObjectId('5f6db09f853128e2ff609d4a'), 'name': 'Sandy', 'address': 'Ocean blvd 2'}
    {'_id': ObjectId('5f6db09f853128e2ff609d4d'), 'name': 'Susan', 'address': 'One way 98'}
    {'_id': ObjectId('5f6db09f853128e2ff609d4e'), 'name': 'Vicky', 'address': 'Yellow Garden 2'}
    {'_id': ObjectId('5f6db09f853128e2ff609d52'), 'name': 'Viola', 'address': 'Sideway 1633'}
    {'_id': ObjectId('5f6db09f853128e2ff609d50'), 'name': 'William', 'address': 'Central st 954'}
    ```
### **Sort theo chiều giảm dần**
- Sử dụng giá trị ***direction*** là `-1` để sort theo chiều giảm dần :
    ```py
    mydb = myclient["mydatabase"]
    mycol = mydb["customers"]

    mydoc = mycol.find().sort("name", -1)

    for x in mydoc:
        print(x)
    ```
    => Output :
    ```
    {'_id': ObjectId('5f6db09f853128e2ff609d50'), 'name': 'William', 'address': 'Central st 954'}
    {'_id': ObjectId('5f6db09f853128e2ff609d52'), 'name': 'Viola', 'address': 'Sideway 1633'}
    {'_id': ObjectId('5f6db09f853128e2ff609d4e'), 'name': 'Vicky', 'address': 'Yellow Garden 2'}
    {'_id': ObjectId('5f6db09f853128e2ff609d4d'), 'name': 'Susan', 'address': 'One way 98'}
    {'_id': ObjectId('5f6db09f853128e2ff609d4a'), 'name': 'Sandy', 'address': 'Ocean blvd 2'}
    {'_id': ObjectId('5f6db09f853128e2ff609d4c'), 'name': 'Richard', 'address': 'Sky st 331'}
    {'_id': ObjectId('5f6db09f853128e2ff609d49'), 'name': 'Michael', 'address': 'Valley 345'}
    {'_id': ObjectId('5f6dab2c87575ae708670be4'), 'name': 'John', 'address': 'Highway 37'}
    {'_id': ObjectId('5f6dad3e52a6ceb0af11a99f'), 'name': 'John', 'address': 'Highway 37'}
    {'_id': ObjectId('5f6db09f853128e2ff609d48'), 'name': 'Hannah', 'address': 'Mountain 21'}
    {'_id': ObjectId('5f6db09f853128e2ff609d51'), 'name': 'Chuck', 'address': 'Main Road 989'}
    {'_id': ObjectId('5f6db09f853128e2ff609d4b'), 'name': 'Betty', 'address': 'Green Grass 1'}
    {'_id': ObjectId('5f6db09f853128e2ff609d4f'), 'name': 'Ben', 'address': 'Park Lane 38'}
    {'_id': ObjectId('5f6db09f853128e2ff609d47'), 'name': 'Amy', 'address': 'Apple st 652'}
    ```