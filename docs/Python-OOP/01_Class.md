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
- **VD :**
    ```py
    class SinhVien:
        pass

    Sinh_Vien_A = SinhVien()
    Sinh_Vien_A.ten = "Cuong"
    Sinh_Vien_A.lop = "VT1"
    Sinh_Vien_A.MSV = "B15VT049"
    print("Tên Sinh Viên :", Sinh_Vien_A.ten)
    print("Lớp :", Sinh_Vien_A.lop)
    print("Mã SV :", Sinh_Vien_A.MSV)
    ```
    => Output :
    ```
    Tên Sinh Viên : Cuong
    Lớp : VT1
    Mã SV : B15VT049
    ```
## **3) Hàm constructor ( initialize method )**
- new