# Tổng quan về Django
## **1) Giới thiệu** <img src=https://i.imgur.com/knrEw3J.png align=right width=47% >
- **Django** là một framework bậc cao của **Python** có thể thúc đẩy việc phát triển phần mềm thần tốc và clean , thiết kế thực dụng . Được xây dựng bởi nhiều lập trình viên kinh nghiệm , **Django** tập trung lớn những vấn đề phát triển Web , bạn có thể phát triển trang web của bạn mà không cần xây dựng từ những căn bản . Đặc biệt nó ***free*** và ***open source*** . 
- Phiên bản ổn định hiện tại : `3.0.1`
- Trang chủ : https://www.djangoproject.com/
- Github : https://github.com/django/django
- Những lợi thế của **django**:
    - **Hoàn thiện** : **Django** phát triển theo tư tưởng "*Batteries included*" ( có thể hiểu ý nghĩa là tích hợp toàn bộ, chỉ cần gọi ra mà dùng ) . Nó cung cấp mọi thứ cho developer không cần phải nghĩ phải dùng cái ngoài . Chúng ta chỉ cần tập trung vào sản phẩm , tất cả đều hoạt động liền mạch với nhau .
    - **Đa năng** : **Django** có thể được dùng để xây dựng hầu hết các loại website , từ hệ thống quản lý nội dung , cho đến các trang mạng xã hội hay web tin tức . Nó có thể làm việc với framework client-side , và chuyển nội dung hầu hết các loại format ( **HTML**, **RESS**, **JSON**, **XML**, ... )
    - **Bảo mật** : **Django** giúp các developer trang các lỗi bảo mật thông thường bằng cách cung cấp framework rằng có những kĩ thuật "phải làm như vậy" để bảo vệ website. Ví dụ: **django** cung cấp bảo mật quản lý tên tài khoản và mật khẩu, tránh các lỗi cơ bản như để thông tin session lên cookie, mã hóa mật khẩu thay vì lưu thẳng.
    - **Dễ Scale** : **Django** sử dụng kiến trúc **shared-nothing** dựa vào component ( mỗi phần của kiến trúc sẽ độc lập với nhau, và có thể thay thế hoặc sửa đổi nếu cần thiết ). Có sự chia tách rõ ràng giữa các phần nghĩa là nó có thể scale cho việc gia tăng traffic bằng cách thêm phần cứng ở mỗi cấp độ : caching , servers , database servers , hoặc application servers . Nhiều web về kinh doanh đã thành công khi **django** được scale đáp ứng yêu cầu của họ .
    - **Dễ maintain** : code **django** được viết theo nguyên tắc thiết kế và pattern có thể khuyến khích ý tưởng bảo trì và tái sử dụng code. Trên thực tế , nó sự theo khái niệm *Don't Repeat Yourself* làm cho không có sự lặp lại không cần thiết , giảm một lượng code .
    - **Tính linh động** : **django** được viết bằng **Python** , nó có thể chạy đa nền tảng . Nó có nghĩa rằng bạn không ràng buộc một platform server cụ thể . **Django** được hỗ trợ tốt ở nhiều nhà cung cấp hosting, họ sẽ cung cấp hạ tầng và tài liệu cụ thể cho hosting web **django**.
- Có thể cho rằng **Django** là framework phổ biến . Các trang web phổ biến sử dụng **Django** : **Disqus** , **Instagram** , **Knight Foundation** , **MacArthur Foundation** , **Mozilla** , **National Geographic** , **Open Knowledge Foundation** , **Pinterest** , and **Open Stack** .
## **2) Cài đặt Django**
- Thực hiện cài đặt qua `pip` :
    ```
    $ sudo pip install django
    ```
    ```
    Collecting django
    Downloading https://files.pythonhosted.org/packages/b2/79/df0ffea7bf1e02c073c2633702c90f4384645c40a1dd09a308e02ef0c817/Django-2.2.6-py3-none-any.whl (7.5MB)
        |████████████████████████████████| 7.5MB 5.2MB/s 
    Collecting sqlparse
    Downloading https://files.pythonhosted.org/packages/ef/53/900f7d2a54557c6a37886585a91336520e5539e3ae2423ff1102daf4f3a7/sqlparse-0.3.0-py2.py3-none-any.whl
    Requirement already satisfied: pytz in /usr/lib/python3/dist-packages (from django) (2018.3)
    Installing collected packages: sqlparse, django
    Successfully installed django-2.2.6 sqlparse-0.3.0
    ```
