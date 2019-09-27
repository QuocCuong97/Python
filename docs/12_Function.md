# Hàm (function)
## **1) Các thao tác với hàm**
### **1.1) Khai báo hàm**
- Để khai báo một **hàm** , ta sử dụng từ khóa `def` với cú pháp :
    ```py
    def <function_name>(parameter_1, parameter_2, ...., parameter_n):
        function-block
    ```
### **1.2) Gọi hàm**
- Cú pháp :
    ```py
    <function_name>()
    ```
- Khi gọi **hàm** , các câu lệnh có trong **hàm** sẽ được thực thi .
- **VD :**
    ```py
    >>> def test():
    ...     print('Hello World!')
    ... 
    >>> test()
    Hello World!
    ```
### **1.3) Sử dụng parameter và argument**
- Đầu tiên , khởi tạo một hàm có `parameter` ( trong trường hợp này là biến `text` ) :
    ```py
    >>> def test_2(text)
    ...     print(text)
    ```
- Khi gọi hàm có `parameter` , phải truyền vào `argument` tương ứng ( trong trường hợp này là truyền giá trị vào cho biến `text` ):
    ```py
    >>> test_2('Hello World!')
    Hello World!
>#### **Giá trị mặc định của `parameter` ( default `argument` )**
- Khi có một giá trị chuỗi được sử dụng nhiều , nên sử dụng **default `argument`** .
- **VD :**
    ```py
    >>> def test_3(khoi, lop):
    ... print('--' + khoi, lop + '--')
    ...
    >>> test_3('D15', 'VT1')
    --D15VT1--
    >>> test_3('D15', 'VT2')
    --D15VT2--
    >>> test_3('D15', 'VT3')   # Giá trị 'D15' được sử dụng nhiều lần
    --D15VT3--
- Theo ví dụ trên , ta thấy chuỗi '`D15`' được người dùng nhập lại nhiều lần . Để giảm thiểu việc nhập liệu , ta sẽ sử dụng **default `argument`** :
    ```py
    >>> def test_3(khoi='D15', lop):
    ... print('--' + khoi, lop + '--')
    ...
    >>> test_3('VT1')
    --D15VT1--
    >>> test_3('VT2')
    --D15VT2--
    >>> test_3('VT3')
    --D15VT3--
    ```
## **2) Positional argument và keyword argument**
## **3) Packing argument và Unpacking argument**
## **4) Biến locals và globals**
## **5) Lệnh `return`**
## **6) Lệnh `yield`**
## **7) Lệnh `lambda`**
## **8) Một số công cụ hỗ trợ**
## **9) Đệ quy ( recursion )**