# Biến trong Python
- Trong lập trình , `biến` ( **variable** ) là tên của 1 vùng trong bộ nhớ RAM , được sử dụng để lưu trữ thông tin . Có thể gán thông tin cho 1 biến , và lấy thông tin đó ra để sử dụng . Khi một biến được khai báo , một vùng trong bộ nhớ sẽ dành cho các biến .
- `Biến` cực kỳ quan trọng và không thể thiếu trong bất cứ chương trình lớn nhỏ nào .
## **1) Khởi tạo `biến` trong Python**
### **1.1) Đặc điểm của `biến`**
- Tên `biến` không được bắt đầu bằng số
- Tên `biến` không được trùng với các từ khóa của **Python**
- Tên `biến` chỉ chứa các chữ cái , số và dấu `_`
- Tên `biến` có phân biệt chữ hoa và chữ thường . **VD :** `PI` , `pi` , `pI` , `Pi` là 4 biến khác nhau
### **1.2) Khởi tạo 1 biến**
- Cú pháp :
    ```py
    <tên_biến> = <value>
    ```
- **VD :**

    <img src=https://i.imgur.com/G9ZxWtW.png>

### **1.3) Khởi tạo nhiều biến**
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
- **VD :**
#### **2.1.5) Các kiểu toán tử cơ bản**
- Một số biểu thức toán học :
    
    | Biểu thức | Mô tả |
    |-----------|-------|
    | `X + Y` | Tổng của `X` và `Y` |
    | `X - Y` | Hiệu của `X` và `Y` |
    | `X * Y` | Tích của `X` và `Y` |
    | `X \ Y` | Thương của `X` và `Y` ( luôn là 1 số thực ) |
### **2.2) String**