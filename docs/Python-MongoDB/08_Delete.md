# Delete
### **Xóa 1 document**
- Để xóa một document, sử dụng phương thức `delete_one()`
- Tham số đầu tiên của phương thức `delete_one()` là một query object chỉ định document sẽ xóa .
    > Nếu query tìm được nhiều hơn 1 kết quả, thì nó sẽ xóa kết quả đầu tiên 
- **VD :**
    ```py
    mydb = myclient["mydatabase"]
    mycol = mydb["customers"]

    myquery = { "address": "Mountain 21" }

    mycol.delete_one(myquery)
    ```
### **Xóa nhiều document**
- Để xóa nhiều hơn một document, sử dụng phương thức `delete_many()` .
- Tham số đầu tiên của phương thức `delete_many()` là một **query object** chỉ định document sẽ xóa .
- **VD :** Xóa toàn bộ các document có `address` bắt đầu bằng ký tự `S` :
    ```py
    mydb = myclient["mydatabase"]
    mycol = mydb["customers"]

    myquery = { "address": {"$regex": "^S"} }

    x = mycol.delete_many(myquery)

    print(x.deleted_count, " documents deleted.")
    ```
### **Xóa toàn bộ các document trong Collection**
- Để xóa toàn bộ document trong Collector, để trống query trong phương thức `delete_many()` .
- **VD :**
    ```py
    mydb = myclient["mydatabase"]
    mycol = mydb["customers"]

    x = mycol.delete_many({})

    print(x.deleted_count, " documents deleted.")
    ```
### **Xóa Collection**
- Để xóa một collection trong **MongoDB**, sử dụng phương thức `drop()` .
- **VD :** Xóa collection `customers` :
    ```py
    mydb = myclient["mydatabase"]
    mycol = mydb["customers"]

    mycol.drop()
    ```
    > Phương thức `drop()` sẽ trả về `True` nếp drop thành công, trả về `False` nếu collection không tồn tại .