# Kiểu dữ liệu Tuple
## **1) Khái niệm**
- **Tuple** là một container cũng được sử dụng rất nhiều trong các chương trình **Python** không thua kém gì **list** .
- Một **Tuple** gồm các yếu tố sau :
    - Được giới hạn bởi cặp ngoặc `()` , tất cả những gì nằm trong đó là những phần tử của **Tuple** .
    - Các phần tử của **Tuple** được phân cách nhau ra bởi dấu phẩy (`,`)
    - **Tuple** có khả năng chứa mọi giá trị , đối tượng trong **Python** .
- **VD :**
    ```py
    >>> (1, 2, 3, 4, 5)             # Một Tuple chứa 5 số nguyên
    (1, 2, 3, 4, 5)
    >>> ('h', 'e', 'l', 'l', 'o')   # Một Tuple chứa 5 chuỗi
    ('h', 'e', 'l', 'l', 'o')
    >>> ([1, 2], [3, 4])            # Một Tuple chứa 1 list là [1, 2] và 1 tuple là (3, 4)
    ([1, 2], [3, 4])
    ```
## **2) Cách khởi tạo Tuple**
### **2.1) Sử dụng cặp dấu ngoặc `()` và đặt giá trị bên trong**
- Cú pháp :
    