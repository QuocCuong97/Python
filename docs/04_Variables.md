# Biến trong Python
### **Mục lục**
[1.     Khởi tạo `biến` trong **Python**](https://github.com/QuocCuong97/Python/blob/master/docs/04_Variables.md#1-kh%E1%BB%9Fi-t%E1%BA%A1o-bi%E1%BA%BFn-trong-python)
- [1.1.  Đặc điểm của `biến`](https://github.com/QuocCuong97/Python/blob/master/docs/04_Variables.md#11-%C4%91%E1%BA%B7c-%C4%91i%E1%BB%83m-c%E1%BB%A7a-bi%E1%BA%BFn)
- [1.2.  Khởi tạo 1 `biến`](https://github.com/QuocCuong97/Python/blob/master/docs/04_Variables.md#12-kh%E1%BB%9Fi-t%E1%BA%A1o-1-bi%E1%BA%BFn)
- [1.3.  Khởi tạo nhiều `biến`](https://github.com/QuocCuong97/Python/blob/master/docs/04_Variables.md#13-kh%E1%BB%9Fi-t%E1%BA%A1o-nhi%E1%BB%81u-bi%E1%BA%BFn)

[2.     Các kiểu biến trong **Python**](https://github.com/QuocCuong97/Python/blob/master/docs/04_Variables.md#2-c%C3%A1c-ki%E1%BB%83u-bi%E1%BA%BFn-trong-python)
- [2.1.  Numbers](https://github.com/QuocCuong97/Python/blob/master/docs/04_Variables.md#21-numbers)
    - [2.1.1.    Số nguyên](https://github.com/QuocCuong97/Python/blob/master/docs/04_Variables.md#211-s%E1%BB%91-nguy%C3%AAn)
    - [2.1.2.    Số thực](https://github.com/QuocCuong97/Python/blob/master/docs/04_Variables.md#212-s%E1%BB%91-th%E1%BB%B1c)
    - [2.1.3.    Phân số](https://github.com/QuocCuong97/Python/blob/master/docs/04_Variables.md#213-ph%C3%A2n-s%E1%BB%91)
    - [2.1.4.    Số phức](https://github.com/QuocCuong97/Python/blob/master/docs/04_Variables.md#214-s%E1%BB%91-ph%E1%BB%A9c)
    - [2.1.5.    Các kiểu toán tử cơ bản](https://github.com/QuocCuong97/Python/blob/master/docs/04_Variables.md#215-c%C3%A1c-ki%E1%BB%83u-to%C3%A1n-t%E1%BB%AD-c%C6%A1-b%E1%BA%A3n)
    - [2.1.6.    Thư viện `math` trong **Python**](https://github.com/QuocCuong97/Python/blob/master/docs/04_Variables.md#216-th%C6%B0-vi%E1%BB%87n-math-trong-python)
- [2.2. String](https://github.com/QuocCuong97/Python/blob/master/docs/04_Variables.md#22-string)
    - [2.2.1.    Sự khác nhau giữa `' '` và `" "`](https://github.com/QuocCuong97/Python/blob/master/docs/04_Variables.md#221-s%E1%BB%B1-kh%C3%A1c-nhau-gi%E1%BB%AFa---v%C3%A0--)
    - [2.2.2.    Chuỗi nhiều dòng với `'''` và `"""`](https://github.com/QuocCuong97/Python/blob/master/docs/04_Variables.md#222-chu%E1%BB%97i-nhi%E1%BB%81u-d%C3%B2ng-v%E1%BB%9Bi--v%C3%A0-)
    - [2.2.3.    Docstring](https://github.com/QuocCuong97/Python/blob/master/docs/04_Variables.md#223-docstring)
    - [2.2.4.    Escape Sequence](https://github.com/QuocCuong97/Python/blob/master/docs/04_Variables.md#224-escape-sequence)
    - [2.2.5.    Chuỗi trần](https://github.com/QuocCuong97/Python/blob/master/docs/04_Variables.md#225-chu%E1%BB%97i-tr%E1%BA%A7n)
    - [2.2.6.    Một số toán tử với chuỗi](https://github.com/QuocCuong97/Python/blob/master/docs/04_Variables.md#226-m%E1%BB%99t-s%E1%BB%91-to%C3%A1n-t%E1%BB%AD-v%E1%BB%9Bi-chu%E1%BB%97i)
    - [2.2.7.    Indexing](https://github.com/QuocCuong97/Python/blob/master/docs/04_Variables.md#227-indexing)
    - [2.2.8.    Cắt chuỗi](https://github.com/QuocCuong97/Python/blob/master/docs/04_Variables.md#228-c%E1%BA%AFt-chu%E1%BB%97i)
    - [2.2.9.    Ép kiểu dữ liệu](https://github.com/QuocCuong97/Python/blob/master/docs/04_Variables.md#229-%C3%A9p-ki%E1%BB%83u-d%E1%BB%AF-li%E1%BB%87u)
    - [2.2.10.   Thay đổi nội dung chuỗi](https://github.com/QuocCuong97/Python/blob/master/docs/04_Variables.md#2210-thay-%C4%91%E1%BB%95i-n%E1%BB%99i-dung-chu%E1%BB%97i)
------------------------------------------------------
- Trong lập trình , `biến` ( **variable** ) là tên của 1 vùng trong bộ nhớ RAM , được sử dụng để lưu trữ thông tin . Có thể gán thông tin cho 1 biến , và lấy thông tin đó ra để sử dụng . Khi một biến được khai báo , một vùng trong bộ nhớ sẽ dành cho các biến .
- `Biến` cực kỳ quan trọng và không thể thiếu trong bất cứ chương trình lớn nhỏ nào .
## **1) Khởi tạo `biến` trong Python**
### **1.1) Đặc điểm của `biến`**
- Tên `biến` không được bắt đầu bằng số
- Tên `biến` không được trùng với các từ khóa của **Python**
- Tên `biến` chỉ chứa các chữ cái , số và dấu `_`
- Tên `biến` có phân biệt chữ hoa và chữ thường . **VD :** `PI` , `pi` , `pI` , `Pi` là 4 biến khác nhau
### **1.2) Khởi tạo 1 `biến`**
- Cú pháp :
    ```py
    <tên_biến> = <value>
    ```
- **VD :**

    <img src=https://i.imgur.com/G9ZxWtW.png>

### **1.3) Khởi tạo nhiều `biến`**
- Cú pháp :
    ```py
    <tên_biến_1>, <tên_biến_2>, <tên_biến_3>,..... = <value_1>, <value_2>, <value_3>,.....
    ```
- **VD :**

    <img src=https://i.imgur.com/0j3ckMZ.png>

## **2) Các kiểu biến trong Python**
- **Python** có 5 kiểu biến :
    - **`Numbers`**
    - **`String`**
    - **`List`**
    - **`Tuple`**
    - **`Dictionary`**
### **2.1) Numbers**
- Trong **Python** hỗ trợ rất nhiều kiểu dữ liệu số ( ***numeric*** ) . Một số kiểu dữ liệu cơ bản như **số nguyên** ( *`integer`* ) , **số thực** ( *`floating-point`* ) , **phân số** ( *`fraction`* ) , **số phức** ( *`complex`* ) , 
#### **2.1.1) Số nguyên**
- **Số nguyên** bao gồm các số nguyên dương (`1`,`2`,`3`,...) , các số nguyên âm ( `-1`,`-2`,`-3`,...) và số `0` .
- Trong **Python** , kiểu dữ liệu **số nguyên** cũng không có gì khác biệt .
#### **2.1.2) Số thực**
- **Số thực** ( *`float`* ) là tập hợp các **số nguyên** ( *`integer`* ) và các số thập phân ( *`decimal`* )
- **VD :** Gán giá trị số thực :
    ```py
    >>> Pi = 3.14
    ```
    > ***Chú ý :*** Thường khi viết **số thực** , phần nguyên và phần thập phân được phân cách nhau bằng dấu phẩy (`,`) . Thế nhưng trong **Python** , dấu phẩy này được thay thế bằng dấu chấm (`.`)
- **Số thực** trong **Python** có độ chính xác xấp xỉ `15` chữ số thập phân :
    ```py
    >>> 10 / 3
    3.3333333333333335
    ```
- Nếu muốn kết quả trên chính xác hơn thì nên dùng ở dạng **số thập phân** ( *`decimal`* ) :
    ```py
    >>> from decimal import *     # Lấy toàn bộ nội dung thư viện Decimal
    >>> getcontext().prec = 20    # Lấy tối đa 20 chữ số phần nguyên và phần thập phân
    >>> Decimal(10) / Decimal(3)
    Decimal('3.33333333333333333333')
    ```
    > ***Chú ý :*** Tuy *`decimal`* có độ chính xác cao hơn so với *`float`* nhưng lại khá rườm rà so với *`float`* . Vì vậy nên cân nhắc mỗi lần sử dụng .
#### **2.1.3) Phân số**
- Để tạo 1 **phân số** ( *`fraction`* ) trong **Python** , sử dụng hàm `Fraction` với cú pháp sau :
    ```py
    Fraction(tử_số, mẫu_số)
    ```
- **VD :** Nhập các phân số <code>&frac12;</code> , <code>&frac45;</code> :
    ```py
    >>> from fractions import *    # Lấy toàn bộ nội dung thư viện Decimal
    >>> Fraction(1,2)              # Phân số với tử số là 1, mẫu số là 2
    Fraction(1,2)
    >>> Fraction(4,5)              # Phân số với tử số là 4, mẫu số là 5
    Fraction(4,5)
    ```
#### **2.1.4) Số phức**
- **Số phức** gồm 2 phần :
    ```py
    <phần_thực> + <phần_ảo>j
    ```
    - Trong đó :
        - <`phần_thực`> , <`phần_ảo`> là số thực
        - `j` là đơn vị ảo trong toán học với <code>j<sup>2</sup> = 1</code>
- Để tạo 1 số phức , sử dụng hàm `Complex` với cú pháp sau :
    ```py
    complex(<phần_thực>,<phần_ảo>)
    ```
- Gán giá trị số phức cho 1 biến :
    ```
    <tên_biến> = <phần_thực> + <phần ảo>j
    ```
- Xuất ra từng phần của số phức :
    - Xuất ra phần thực :
        ```
        <tên_biến>.real
        ```
    - Xuất ra phần ảo :
        ```
        <tên_biến>.imag
        ```
- **VD :** Nhập một số số phức sau :
    - Gán biến `c` có giá trị `2 + 1j` . Xuất ra phần thực và phần ảo của biến `c` .
    - `4 + j` ( sẽ có lỗi vì kiểu dữ liệu nhập không đúng ) .
    - Tạo số phức có phần thực là `3` , phần ảo là `1` .
    - Tạo số phức có phần thực là `3` , phần ảo là `1` .
    - Tạo số phức chỉ có phần thực là `2` .
    ```py
    >>> c = 2 + 1j   # gán giá trị cho biến c là 1 số phức với phần thực là 2 còn phần ảo là 1
    >>> c
    (2 + 1j)
    >>> c.imag       # lấy phần ảo của số phức 2 + 1j mà ta đã gán cho biến c
    1.0
    >>> c.real       # lấy phần thực
    2.0
    -------------------------------------------------------------
    >>> 4 + j        # phần ảo là 1 , tuy vậy chúng ta không được phép bỏ số 1 như trong toán
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NameError: name 'j' is not defined
    >>> 4 + 1j
    (4 + 1j)
    -------------------------------------------------------------
    >>> 3j + 1       # phần thực là 1 , phần ảo là 3
    (1 + 3j)
    -------------------------------------------------------------
    >>> complex(3, 1)# dùng hàm complex để tạo 1 số phức với phần thực là 3, ảo là 1
    (3 + 1j)
    -------------------------------------------------------------
    >>> complex(2)   # chỉ có phần thực, phần ảo được mặc định là 0
    (2 + 0j)
    ```

#### **2.1.5) Các kiểu toán tử cơ bản**
- Một số biểu thức toán học :
    
    | Biểu thức | Mô tả |
    |-----------|-------|
    | `X + Y` | Tổng của `X` và `Y` |
    | `X - Y` | Hiệu của `X` và `Y` |
    | `X * Y` | Tích của `X` và `Y` |
    | `X / Y` | Thương của `X` và `Y` ( luôn là 1 số thực ) |
    | `X // Y` | Thương nguyên của `X` với `Y` ( kết quả luôn luôn nhỏ hơn hoặc bằng `X / Y` ) |
    | `X % Y` | Phần dư của phép chia `X` cho `Y` |
    | `X ** Y` | Lũy thừa mũ `Y` với cơ số `X` ( <code>X<sup>Y</sup></code> ) |

#### **2.1.6) Thư viện `math` trong Python**
- Thư viện **`math`** trong **Python** hỗ trợ rất nhiều hàm tính toán liên quan đến toán học .
- Để sử dụng 1 thư viện nào đó , ta dùng lệnh :
    ```py
    import <tên_thư_viện>
    ```
- Muốn sử dụng hàm nào đó của thư viện , ta sử dụng cú pháp :
    ```py
    <tên_thư_viện>.<tên_hàm>
    ```
- Dưới đây là 1 số hàm thường được dùng trong việc tính toán cơ bản :

    | Tên hàm | Công dụng |
    |---------|-----------|
    | `.trunc(x)` | Trả về 1 số nguyên là phần nguyên của số `x` |
    | `.floor(x)` | Trả về 1 số nguyên được làm tròn số từ số `x` , kết quả luôn luôn nhỏ hơn hoặc bằng `x` |
    | `.ceil(x)` | Trả về 1 số nguyên được làm tròn số từ số `x` , kết quả luôn luôn lớn hơn hoặc bằng `x` |
    | `.fabs(x)` | Trả về 1 số thực là trị tuyệt đối của số `x` |
    | `.sqrt(x)` | Trả về 1 số thực là căn bậc 2 ( <code>&Sqrt;</code> ) của số `x` |
    | `.gcd(x, y)` | Trả về 1 số nguyên là ước chung lớn nhất của 2 số `x` và `y` |

- **VD :**
    ```py
    >>> import math      # lấy nội dung của thư viện math về sử dụng
    >>> math.trunc(3.9)
    3
    >>> math.fabs(-3)
    3.0
    >>> math.sqrt(16)
    4.0
    >>> math.gcd(6, 4)
    2
    ```
### **2.2) String**
- Trong **Python** , chuỗi ( ***string*** ) là những thứ được đặt trong cặp dấu `' '` , hoặc `" "`, có thể cũng là cặp `''' '''` , `""" """` . Nhưng cơ bản và thường được sử dụng nhất là cặp `' '` và `" "` .
#### **2.2.1) Sự khác nhau giữa `' '` và `" "`**
- 2 cặp dấu nháy này có công dụng tương đương nhau .
- Xét **VD :** `'I'm a Student'`
    - Trong trường hợp này , nếu sử dụng `' '` thì string sẽ được hiểu là "`I`" . Phần đằng sau "`m a Student'`" sẽ không có ý nghĩa => Lỗi `SyntaxError` .
    - Nếu sử dụng `" "` thì cú pháp sẽ hoàn toàn đúng và không bị trùng lặp các cặp dấu : `"I'm a Student"`
- Làm tương tự với các trường hợp ngược lại
#### **2.2.2) Chuỗi nhiều dòng với `'''` và `"""`**
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
#### **2.2.3) Docstring**
- **Docstring** là một dạng chú thích nhiều dòng , hay xuất hiện ở đầu file **Python** , sau 1 dòng định nghĩa **class** hoặc **hàm** . Đây cũng là một trong những chuẩn ước về định dạng , trình bày code **Python** .
    ```py
    '''
    Day la doan code vi du
    Ve khai niem Docstring
    '''
    print("Hello_World!")
    ```
#### **2.2.4) Escape Sequence**
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

#### **2.2.5) Chuỗi trần**
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
#### **2.2.6) Một số toán tử với chuỗi**
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
#### **2.2.7) Indexing**
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
#### **2.2.8) Cắt chuỗi**
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
#### **2.2.9) Ép kiểu dữ liệu**
#### **2.2.10) Thay đổi nội dung chuỗi**














### **2.6) Kiểm tra kiểu dữ liệu của biến**
- Không như đa số các ngôn ngữ lập trình khác, khi khai báo biến phải đi kèm với kiểu dữ liệu. Trong **Python** việc khai báo kiểu dữ liệu cho biến không cần thiết mà **Python** sẽ tự biết kiểu dữ liệu của giá trị gán cho biến .
- Để kiểm tra kiểu dữ liệu giá trị của 1 biến đã khởi tạo , ta sử dụng hàm `type()` . Cú pháp :
    ```py
    type(<tên_biến>)
    ```
- **VD :**

    <img src=https://i.imgur.com/m04iBlR.png>
