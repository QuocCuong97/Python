# Update
### **Update một document**
- Có thể update các document bằng cách sử dụng phương thức `update_one()` .
- Tham số đầu tiên truyền vào trong phương thức là query object chỉ định document sẽ được update
    > Nếu query tìm được nhiều hơn 1 kết quả, thì nó sẽ xóa kết quả đầu tiên 
- Tham số thứ 2 truyền vào sẽ là giá trị mới gán cho document .
- **VD :**
    ```py
    mydb = myclient["mydatabase"]
    mycol = mydb["customers"]

    myquery = { "address": "Valley 345" }
    newvalues = { "$set": { "address": "Canyon 123" } }

    mycol.update_one(myquery, newvalues)

    #print "customers" after the update:
    for x in mycol.find():
        print(x)
    ```
### **Update nhiều document**
- Để update tất cả các document phù hợp với query, sử dụng phương thức `update_many()`
- **VD :** Update tất cả các document có `address` bắt đầu bằng ký tự `S` :
    ```py
    mydb = myclient["mydatabase"]
    mycol = mydb["customers"]

    myquery = { "address": { "$regex": "^S" } }
    newvalues = { "$set": { "name": "Minnie" } }

    x = mycol.update_many(myquery, newvalues)

    print(x.modified_count, "documents updated.")
    ```
