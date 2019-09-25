# Kiểu dữ liệu Dict
## **1) Khái niệm**
- **Dict ( dictionary )** cũng là một container như **list** , **tuple** .
- Khác biệt là **List** và **Tuple** có các `index` để phân biệt các phần tử còn **Dict** lại dùng các `key` để phân biệt .
- Một **Dict** gồm các yếu tố sau :
    - Được giới hạn bởi các cặp ngoặc nhọn `{}` , tất cả những gì nằm trong đó là những phần tử của **dict** .
    - Các phần tử của **Dict** được phân cách nhau ra bởi dấu phẩy (`,`) .
    - Các phần tử của **Dict** phải là 1 cặp `key-value` .
    - Cặp `key-value` của phần tử trong **Dict** được phân cách bởi dấu hai chấm (`:`) .
    - Các `key` buộc phải là một **hash object** .
## **2) Cách khởi tạo Dict**
### **2.1) Sử dụng cặp dấu ngoặc `{}` và đặt giá trị bên trong**
- Cú pháp :
    ```py
    {<key_1: value_1>, <key_2: value_2>, <key_3: value_3>, ...,<key_n: value_n>}
    ```
- **VD :**
    ```py
    >>> dic = {'name': 'Cuong', 'STT': '1'}
    >>> dic
    {'name': 'Cuong', 'STT': '1'}
    >>> dic_empty = {}           # Khởi tạo dict rỗng
    >>> dic_empty
    {}
    ```
### **2.2) Sử dụng constructor Dict**
#### **2.2.1) Khởi tạo 1 Dict rỗng**
- Cú pháp :
    ```py
    dict()
    ```
- **VD :**
    ```py
    >>> dic = dict()
    >>> dic
    {}
    ```
#### **2.2.2) Khởi tạo một Dict từ một mapping object** `*`
#### **2.2.3) Khởi tạo bằng iterable** `*`
#### **2.2.4) Khởi tạo bằng keyword arguments**
### **2.3) Sử dụng Dict Comprehension**
- **VD :**
    ```py
    >>> dic = {key: value for key, value in [('name', 'Cuong'), ('STT', '1')]}
    >>> dic
    {'name': 'Cuong', 'STT': '1'}
    ```
### **2.4) Sử dụng phương thức fromkeys**
- Cú pháp :
    ```py
    dict.fromkeys(iterable, value)
    ```
- Công dụng : cách này cho phép khởi tạo một **Dict** với các `keys` nằm trong một `iterable` . Các giá trị này đều sẽ nhận được một giá trị với mặc định là `None`
- **VD :**
    ```py
    >>> iter_ = ('name', 'STT')
    >>> dic_none = dict.fromkeys(iter_)