# Class
## **1) Khái niệm class ( lớp )**
- **Class** giống như là một bản mẫu , một khuôn mẫu . Ở đó ta khai báo các thuộc tính ( ***attribute*** ) và phương thức ( ***method*** ) nhằm miêu tả để từ đó ta tạo ra được những object ( ***đối tượng*** ) .
- Cú pháp :
    ```py
    class <ClassName>:
        # code
    ```
    > Theo chuẩn **PEP8** về đặt tên của lớp ( ***class*** ) thì sẽ được viết theo kiểu `CapWords` .
- **VD :**
    ```py
    class MyClass:
        x = 5

    print(MyClass)
    ```
    => Output :
    ```
    <class '__main__.MyClass'>
    ```
## **2) Thuộc tính**
- Khi khai báo thuộc tính cho một object , phải nghĩa ra những thuộc tính để mà giúp có thể phân biệt nó với những object khác cùng class .
