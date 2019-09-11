# Kiểu dữ liệu Chuỗi
- Trong **Python** , chuỗi ( ***string*** ) là những thứ được đặt trong cặp dấu `' '` , hoặc `" "`, có thể cũng là cặp `''' '''` , `""" """` . Nhưng cơ bản và thường được sử dụng nhất là cặp `' '` và `" "` .
## **1) Sự khác nhau giữa `' '` và `" "`**
- 2 cặp dấu nháy này có công dụng tương đương nhau .
- Xét **VD :** `'I'm a Student'`
    - Trong trường hợp này , nếu sử dụng `' '` thì string sẽ được hiểu là "`I`" . Phần đằng sau "`m a Student'`" sẽ không có ý nghĩa => Lỗi `SyntaxError` .
    - Nếu sử dụng `" "` thì cú pháp sẽ hoàn toàn đúng và không bị trùng lặp các cặp dấu : `"I'm a Student"`
- Làm tương tự với các trường hợp ngược lại
## **2) Chuỗi nhiều dòng với `'''` và `"""`**
- Chuỗi nhiều dòng sẽ được đặt trong các cặp dấu `'''` hoặc `"""` .
- **VD :**
    ```py
    >>> s = '''dong 1
    dong 2
    dong 3'''
    >>> s
    'dong 1\ndong 2\ndong 3'
    >>> print(s)        # sử dụng hàm print() để hiển thị kết quả mong muốn
    dong 1
    dong 2
    dong 3
    ```
## **3) Docstring**
- **Docstring** là một dạng chú thích nhiều dòng , hay xuất hiện ở đầu file **Python** , sau 1 dòng định nghĩa **class** hoặc **hàm** . Đây cũng là một trong những chuẩn ước về định dạng , trình bày code **Python** .
    ```py
    '''
    Day la doan code vi du
    Ve khai niem Docstring
    '''
    print("Hello_World!")
    ```
## **4) Escape Sequence**
- **Escape Sequence** là 1 chuỗi đặc biệt gồm 1 ký tự theo sau dấu `\` có công dụng cụ thể .
- Một số **escape sequence** :

    | Tên | Ký hiệu | Giải thích |
    |-----|---------|------------|
    | Alert | `\a` | Phát ra 1 tiếng bíp |
    | Backspace | `\b` | Đưa con trỏ về lại 1 khoảng trắng |
    | Newline | `\n` | Đưa con trỏ xuống dòng tiếp theo |
    | Horizontal tab | `\t` | In một tab ngang |
    | Single quote | `\'` | In ra ký tự `'` |
    | Double quote | `\"` | In ra ký tự `"` |
    | Blackslash | `\\` | In ra ký tự `\` | 

## **5) Chuỗi trần**
- **Python** cho phép sử dụng một dạng , gọi là **chuỗi trần** . **Chuỗi trần** sẽ không quan tâm đến **escape sequence** .
- Cú pháp :
    ```py
    r'nội_dung_chuỗi'
    ```
- **VD :**
    ```py
    >>> a = r'\neu mot ngay'     # chuỗi trần, bỏ qua \n
    >>> print(a)
    '\neu mot ngay'
    ```
## **6) Một số toán tử với chuỗi**
- **Toán tử `+` :**
    - Đây là một toán tử rất được hay sử dụng trong việc nối các chuỗi .
    - Cú pháp :
        ```py
        A + B    # A và B là 2 chuỗi
        ```
    - **VD :**
        ```py
        >>> s = 'hello'
        >>> s += 'Python'     # tương tự câu lệnh s = s + 'Python'
        >>> s
        'hello Python'
        >>> s2 = ', good bye'
        >>> s3 = s + s2
        >>> s3
        'hello Python, goodbye'
        ```
- **Toán tử `*` :**
    - Toán tử này giúp tạo ra một chuỗi nhờ lặp đi lặp lại chuỗi với số lần mong muốn .
    - Cú pháp :
        ```py
        A * N         #  Với A là một chuỗi, N là một số nguyên
        ```
    - **VD :**
        ```py
        >>> 'a' * 3      # tạo ra chuỗi lặp lại chuỗi 'a' 3 lần 
        'aaa'
        >>> s = 'abc'
        >>> s *= 2       # tương tự câu lệnh s = s * 2
        >>> s
        'abcabc'
        >>> s * 0        # bất cứ chuỗi nào * 0 đều có kết quả là :
        ''
        >>> 'Hello World' * (-2)  # đối với số âm cũng sẽ trả về một chuỗi ''
        ''
- **Toán tử `in` :**
    - Khi sử dụng toán tử này, chỉ có thể nhận được 1 trong 2 đáp án là `True` hoặc `False` .
    - Cú pháp :
        ```py
        s in A     # với s và A là chuỗi
        ```
        => Kết quả sẽ là `True` nếu chuỗi `s` xuất hiện trong chuỗi `A` . Ngược lại sẽ là `False`
    - **VD :**
        ```py
        >>> 'a' in 'abc'
        True
        >>> 'ab' in 'abc'
        True
        >>> 'ac' in 'abc'
        False
        ```
## **7) Indexing**
- Trong một chuỗi của **Python** , các ký tự tạo nên chuỗi đó sẽ được đánh số từ `0` đến `n-1` từ trái qua phải với `n` là số kí tự có trong chuỗi .
- Không chỉ đánh số từ `0` tới `n-1` từ trái qua phải với `n` là độ dài chuỗi , các ký tự của chuỗi còn được đánh số từ phải qua trái từ `-1` đến `-n` với `n` là độ dài chuỗi .
- Cú pháp index : 
    ```
    <chuỗi><vị_trí>
    ```
- **VD :** Có chuỗi `'abc xyz'`
    ```py
    >>> s = 'abc xyz'
    >>> s
    'abc xyz'
    ```
    => Các ký tự trong chuỗi sẽ được đánh số như sau :

    | `a` | `b` | `c` | _ | `x` | `y` | `z` |
    |---|---|---|--|---|---|---|
    | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 
    | -7 | -6 | -5 | -4 | -3 | -2 | -1 |

    => Dựa vào đây , có thể lấy được bất cứ kí tự nào trong chuỗi 
    ```py
    >>> s = 'abc xyz'
    >>> s[0]
    'a'
    >>> s[-7]
    'a'
    >>> s[3]
    ''
    >>> s[7]     # truy cập vị trí không có trong chuỗi
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    IndexError: string index out of range
    >>> s[len(s) - 1]    # truy cập phần tử cuối cùng của chuỗi
    'z'
    ```
## **8) Cắt chuỗi**
- Dựa trên **Indexing** , **Python** cho phép cắt chuỗi .
- Cú pháp ( cắt từ **trái sang phải** ) :
    ```py
    <chuỗi>[vị_trí_bắt_đầu:vị_trí_dừng]
    ```
    => Khi sử dụng cú pháp này , ta sẽ nhận được 1 chuỗi . Chuỗi này chính là bản sao của chuỗi mà ta muốn cắt . Ta sẽ cắt lấy từng ký tự có vị trí từ `<vị_trí_bắt_đầu>` đến `<vị_trí_dừng> -1` và từ trái sang phải .
    - **VD :** Có chuỗi `'abc xyz'` :
        ```py
        >>> s = 'abc xyz'
        >>> s[1:5]            # cắt từng ký tự có vị trí từ 1 đến 4
        'bc x'
        >>> s[0:3]            # cắt từng ký tự có vị trí từ 0 đến 3
        'abc '
        >>> s[-4:-1]          # cắt từng kí tự có vị trí từ -4 đến -2
        ' xy'
        >>> s[1:None]         # lấy các ký tự có vị trí 1 đến hết chuỗi
        'bc xyz'
        >>> s[1:]             # chỉ cần bỏ trống, Python sẽ tự hiểu là None
        'bc xyz'
        >>> s[:]              # sao chép chuỗi
        'abc xyz'
        ```
- Cú pháp ( cắt từ **phải sang trái** ) :
    ```py
    <chuỗi>[vị_trí_bắt_đầu:vị_trí_dừng:bước]
    ```
    - Với cú pháp đầu tiên , không cần nhập số `bước` . Mặc định `bước` = `1` ( vị trí của ký tự sau hơn vị trí của ký tự trước `1` đơn vị )
    - Có thể tăng `bước` :
        ```py
        >>> s = 'abc xyz'
        >>> s = [1:7:2]        # bước là 2 => trả về s[1], s[3], [s5]
        'b y'
        ```
    - Cắt từ phải sang trái bằng việc đặt `bước` âm :
        ```py
        >>> s = 'abc xyz'
        >>> s[3:1-1]   # bắt đầu từ s[3] tới s[1] => trả về s[3], s[2]
        ```
    > ***Chú ý :*** Không được đặt `bước = 0`
## **9) Ép kiểu dữ liệu**
- Trong trường hợp muốn chuyển chuỗi (có nội dung là số) về số để tính toán hoặc ngược lại, phải ép kiểu dữ liệu .
- Sử dụng hàm `int()` để chuyển đổi về số nguyên :
    ```py
    int(<tên_biến>)
    ```
    - **VD :** 
        ```py
        >>> s = '69'
        >>> int(s)
        69
        >>> t = 3.63
        >>> int(t)
        3
        ```
    > ***Chú ý :*** không thể chuyển đổi số thực dưới dạng chuỗi bằng hàm `int()`
- Sử dụng hàm `float` để chuyển đổi về số thực :
    ```py
    float(<tên_biến>)
    ```
    - **VD :**
        ```py
        >>> s = '3.63'
        >>> f = float(s)
        >>> a
        3.63
        >>> i = int(a)
        3
        ```
## **10) Thay đổi nội dung chuỗi**
- **Python** không cho phép thay thế bằng phương pháp **Indexing** giống như các ngôn ngữ khác .
    ```py
    >>> s = 'abc xyz'
    >>> s[0] = k
    >>> s
    Traceback (most recent call last) :
      File '<stdin>', line 1, in <module>
    TypeError: 'str' object does not support item assignment
    ```
- Chỉ có thể sử dụng phương pháp cắt chuỗi :
    ```py
    >>> s = 'abc xyz'
    >>> s = 'k' + s[1:0]   # bỏ qua không lấy s[0]
    >>> s
    'kbc xyz'
    ```
## **11) Định dạng chuỗi trong Python**
### **11.1) Định dạng bằng toán tử `%`**
- Đây là kiểu định dạng quen thuộc khá giống lập trình `C` .
- Cú pháp :
    ```py
    <tên_chuỗi> % (value_1,value_2,value_3,...)
    ```
- **VD :** 
