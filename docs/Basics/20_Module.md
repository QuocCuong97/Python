# Module trong Python
## **1) Giới thiệu**
- **Module** chỉ đơn giản là một file python ( `.py` ) bình thường .
- Việc đặt tên cho **module** có ràng buộc như đặt tên một biến .
- **Module** của **Python** không nhất thiết phải là một file **python** mà có thể là những file được viết bằng những ngôn ngữ lập trình khác như **C** , **C++** , **Java** ,.... Những **module** như vậy được gọi là **extension module** , và thường được sử dụng cho việc lưu các external library
- Các module phải được tạo trong cùng một thư mục để hoạt động được cùng nhau .
## **2) Lệnh `import`**
- Đây là câu lệnh cơ bản khi làm việc với **module**
- Cú pháp :
    ```py
    import<tên_module>
    ```
    hoặc có thể import nhiều **module** trên một dòng lệnh :
    ```py
    import module_a, module_b, module_c
    ```
- Công dụng : sau khi thực hiện lệnh , file **module** sẽ chạy và thực hiện tạo ra một **module object** lưu dưới một biến với tên là tên của biến đó . **Module object** này có các **attribute** và **method** lần lượt là các biến và hàm (với scope global) .
- **VD :** Có module `new_module.py` sau :
    ```py
    # new_module.py
    print('Day la vi du ve lenh Import')
    def test(a):
        print(a)
    ```
    - Import `new_module` vào file `main.py` như sau :
    ```py
    # main.py
    import new_module
    new_module.test('Hello')
    new_module.test('World!')
    ```
    - Chạy file `main.py`
    ```py
    $ python3 main.py
    Day la vi du ve lenh Import
    Hello
    World!
    ```
## **3) Lệnh `from import`**
- Cú pháp :
    ```py
    from <module> import <function_in_module>
    ```
    hoặc import nhiều hàm :
    ```py
    from <module> import <function_1>, <function_2>
    ```
    hoặc import tất cả các hàm :
    ```py
    from <module> import *
    ```
- Công dụng : import hàm từ một **module** khác .
- **VD :** Có module `new_module.py` sau :
    ```py
    # new_module.py
    print('Day la vi du ve lenh Import')
    def test(a):
        print(a)
    ```
    - Import `new_module` vào file `main.py` như sau :
    ```py
    # main.py
    from new_module import test
    test('Hello')
    test('World!')
    ```
    - Chạy file `main.py`
    ```py
    $ python3 main.py
    Day la vi du ve lenh Import
    Hello
    World!
    ```
## **4) Import một module nhiều lần**
## **5) Reload module**
## **6) Đổi tên module , attribute khi import**
## **7) Folder `__pycache__`**