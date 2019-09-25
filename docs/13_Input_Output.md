# Nhập/Xuất trong Python
## **1) Hàm `print`**
- Hàm `print` giúp xuất các nội dung mà người dùng muốn ra shell ( `terminal` , `command prompt` , `powershell` , ...)
- Cú pháp :
    ```py
    print(*object, sep='', end='\n', file=sys.stdout, flush=False)
    ```
- Trong đó :
    - `*object` : `*` chính là **packing argument** . Nó sẽ gom các **argument** lại thành một **tuple**
        ```py
        >>> packing = 1, 2, 3, 4
        >>> packing
        (1, 2, 3, 4)
        >>> print('Hello', 'World!')
        Hello World!
        ```
    - `sep` - `separate` : giá trị mặc định của `sep` là một khoảng trắng ( `space` ) . Khi các `argument` ném vào hàm `print` để hàm `print` in ra nội dung , nó sẽ được gói vào 1 **Tuple** . Các giá trị trong **tuple** sẽ được nối với nhau bằng `sep` .
        ```py
        >>> print('around', 'the', 'world')       # sep mặc định là space
        around the world
        >>> print('around', 'the', 'world', sep='---')
        around---the---world
        >>> print('around', 'the', 'world', sep='\n')
    - `end`
    - `file`
    - `flush`
## **2) Hàm `input`** :
- Cú pháp :
    ```py
    input(prompt=None)
    ```
- Công dụng : hàm này giúp ta đọc một chuỗi từ **standard input** , sau đó trả về cho chúng ta . Và thứ mà nó đọc vào luôn là một **chuỗi** cho dù có nhập **tuple** , **list** , **dict** ,...