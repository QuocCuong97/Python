# Kiểu dữ liệu List
## **1) Khái niệm**
- **List** là một container được sử dụng rất nhiều trong các chương trình **Python** .
- Một **list** gồm các yếu tố sau :
    - Được giới hạn bởi cặp ngoặc `[]` , tất cả những gì nằm trong đó là những phần tử của **List** .
    - Các phần tử của **List** được phân cách nhau bởi dấu phẩy ( `,` )
    - **List** có khả năng chứa mọi giá trị , đối tượng trong **Python** . Và bao gồm chứa chính nó .
- **VD :**
    ```py
    >>> [1, 2, 3, 4, 5]               # List chứa 5 số nguyên
    [1, 2, 3, 4, 5]

    >>> ['a', 'b', 'c', 'd']          # Một list chứa 4 chuỗi
    ['a', 'b', 'c', 'd']

    >>> [[1, 2], [3, 4]]              # Một list chứa 2 list [1, 2] và [3, 4]
    [[1, 2], [3, 4]]

    >>> [1, 'one', [2, 'two']]        # List chứa số nguyên, chuỗi, và List
    [1, 'one', [2, 'two']]
    ```
## **2) Cách khởi tạo List**
### **2.1) Sử dụng cặp dấu ngoặc `[]` đặt giá trị bên trong**
- Cú pháp :
    ```
    [<value_1>, <value_2>, <value_3>, ...., <value_n-1>, <value_n>]
    ```
- **VD :**
    ```py
    >>> lst = [1,2,5,'a']
    >>> lst
    [1,2,5,'a']
    >>> empty_list = []              # Khởi tạo list rỗng
    >>> empty_list
    []
    ```
### **2.2) Sử dụng List Comprehension**
- Cú pháp :
    ```
    [comprehension]
    ```
- **VD :**
    ```py
    >>> a = [a for a in range(3)]
    >>> a
    [0, 1, 2]
    >>> b = [[n, n*1, n*2] for n in range(1, 4)]
    >>> b
    [[1, 1, 2], [2, 2, 4], [3, 3, 6]]
    ```
### **2.3) Sử dụng constructor list**
- Cú pháp :
    ```py
    list (iterable)
    ```
- **VD :**
    ```py
    >>> lst = list([1, 2, 3])
    >>> lst
    [1, 2, 3]
    >>> str_lst = list('abcdef')
    >>> str_lst
    ['a', 'b', 'c', 'd' , 'e', 'f']
    ```
## **3) Một số toán tử với list trong Python**
- **Toán tử `+`**
    ```py
    >>> lst = [1, 2]
    >>> lst += ['one', 'two']
    >>> lst
    [1, 2, 'one', 'two']
    >>> lst += 'abc'               # Cộng List với chuỗi
    >>> lst
    [1, 2, 'one', 'two', 'a', 'b', 'c']
    >>> 'abc' + [1, 2]             # Chỉ cho phép list + chuỗi , không cho phép chuỗi + list
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: must be str, not list
    ```
- **Toán tử `*`**
    ```py
    >>> lst = list('abc') * 2
    >>> lst
    ['a', 'b', 'c', 'a', 'b', 'c']
    >>> [1, 2] * 3
    [1, 2, 1, 2, 1, 2]
- **Toán tử `in` :
    ```py
    >>> 'a' in [1, 2, 3]
    False
    >>> 'a' in [a, 2, 3]
    True
    >>> 'a' in [['a'], 'b', 'c']   # Chỉ có ['a'] , không có 'a'
    False
## **4) Indexing và cắt List trong Python**
- **VD :**
    ```py
    >>> lst = [1, 2, 'a', 'b', [3, 4]]
    >>> lst[0]
    1
    >>> lst[-1]
    [3, 4]
    >>> lst[3]
    'b'
    >>> lst[1:3]
    [2, 'a']
    >>> lst[:2]
    [1, 2]
    >>> lst[2:]
    ['a', 'b', [3, 4]]
    >>> lst[::-1]
    [[3, 4], 'b', 2, 1]
    ```
## **5) Thay đổi nội dung List**
- Khác với chuỗi , có thể thay đổi nội dung thành phần trong list :
    ```py
    >>> lst = [1, 'two', 3]
    >>> lst[1]
    'two'
    >>> lst[1] = 2
    >>> lst
    [1, 2, 3]
    ```
## **6) Ma trận**
