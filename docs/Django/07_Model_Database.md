# Dùng Model để tạo bảng Database trong Django
## **1) Khái niệm ORM**
- **Object-Relational Mapping** ( **ORM** ) là một kĩ thuật cho phép chúng ta truy vấn và quản lý dữ liệu từ database bằng cách sử dụng mô hình hướng đối tượng . Khi nhắc đến **ORM** , hầu hết mọi người đều nói đến thư viện đã áp dụng kĩ thuật **ORM** .

    <img src=https://i.imgur.com/kwtfEc0.png>

- Vì những thư viện **ORM** là những thư viện đã hoàn chỉnh được viết bằng ngôn ngữ lập trình đang dùng và nó đã gói nhóm code cần thiết để quản lý data, như vậy bạn không cần sử dụng **SQL** nữa mà sẽ tương tác trực tiếp qua cách viết hướng đối tượng của ngôn ngữ đang sử dụng .
## **2) Liên kết Database**
- Sử dụng file `models.py` trong folder của app để thiết kế database .
- **VD :** Tạo bảng **Post** trong database có các cột như sau :
    - `title`: lưu tiêu đề bài viết, có đồ dài tối đa là `100` kí tự
    - `body`: nội dung bài viết, không giới hạn kí tự
    - `date`: ngày viết bài, tự thêm ngày hiện tại khi tạo ra bài viết .
    ```py
    class Post(models.Model):
        title = models.CharField(max_length=100)
        body = models.TextField()
        date = models.DateTimeField(auto_now_add=True)
    ```
    - Trong đó :
        - Khai báo class `Post` kế thừa `models.Model`, là class được viết ra ánh xạ đến bảng trong database .
        - Khai báo field `title` ánh xạ đến cột `title` trong bảng. Field `title` sẽ thuộc `CharField` có tham số `max_length=100`, có nghĩa cột title sẽ lưu trữ kiểu **string** và dài nhất `100` ký tự .
        - Khai báo field `body` ánh xạ đến cột `body` trong bảng. Field body sẽ thuộc TextField, có nghĩa cột body lưu trữ kiểu String vài không giới hạn độ dài.
        - Khai báo field  `date` ánh xạ đến cột `date` trong bảng. Field `date` sẽ có thuộc tính `DateTimeField` có tham số `auto_now_add=True`, có nghĩa cột date lưu kiểu **date** và tự động thêm ngày hiện tại cho record mới .
## **3) Migrations**
- **Migrations** là những cách **Django** kiểm tra sự thay đổi mà người lập trình đã tác động đến các **models** (thêm hay xoá **model**, thêm sửa xoá các field trong **models**, …) mà người lập trình muốn nó tác động đến **database** . **Migrations** được thiết kế cách tự động, tuy nhiên bạn nên biết để dễ config và chỉnh sửa .
- Khi mới tạo project **Django** , **Django** sẽ mặc định config database là **SQLite** - một dạng database đơn giản , dễ học , dễ làm dự án lúc đầu . Đồng thời trong lần **migrate** đầu tiên, **Django** sẽ tự động tạo ra file `db.sqlite3` để lưu trữ database . Tất cả được thể hiện trong file `settings.py` :
    
    <img src=https://i.imgur.com/1Yu5Rlx.png>

- **B1 :** Tạo file `migration` cho Database để update model trong app `blog` . Sử dụng lệnh `makemigrations` để tạo các file `migration` , báo cho Django biết các model  được thay đổi ở app `blog` :
    ```sh
    $ python3 manage.py makemigrations blog
    ```
    > Nếu không ghi tên app kèm theo thì **Django** sẽ quét toàn bộ các app hiện tại .
    - Sau khi chạy lệnh , folder `migrations` trong app sẽ có các file `xxxx_initial.py` để lưu lại các sự thay đổi trong model :
        ```sh
        blog
        ├── admin.py
        ├── apps.py
        ├── __init__.py
        ├── migrations
        │   ├── 0001_initial.py
        │   └── __init__.py
        ├── models.py
        ├── templates
        │   └── pages
        ├── tests.py
        ├── urls.py
        └── views.py
        ```
        - Nội dung file `0001_initial.py` :

            <img src=https://i.imgur.com/VWbNx9Z.png>
- **B2 :** Sử dụng lệnh `migrate` để yêu cầu **Django** chạy các file `migrations` và thực hiện thay đổi đến database :
    ```sh
    $ python3 manage.py migrate
    ```
    ```
    Operations to perform:
      Apply all migrations: admin, auth, contenttypes, home, sessions
    Running migrations:
      Applying blog.0001_initial... OK
    ```
    => Kết quả OK có nghĩa là đã migrate thành công .
    > Ngoài các cột `title`, `body` và `date` được tạo thì có thêm cột `id` mặc định được **Django** tạo sẵn (là id để phân biệt các record, giá trị sẽ tự tăng) 

    <img src=https://i.imgur.com/HhDlg7v.png>
## **4) Cách tương tác với các database khác**
- **Django** hiện tại hỗ trợ **ORM** cho `5` hệ quản trị cơ sở dữ liệu là: **SQLite**, **MySQL**, **MariaDB**, **PostgreSQL** và **Oracle**.
### **4.1) MySQL**
- [Tham khảo](https://docs.djangoproject.com/en/3.0/ref/databases/#mysql-notes)
### **4.2) MariaDB**
- [Tham khảo](https://docs.djangoproject.com/en/3.0/ref/databases/#mariadb-notes)
### **4.3) PostgreSQL**
- [Tham khảo](https://docs.djangoproject.com/en/3.0/ref/databases/#postgresql-notes)
### **4.4) Oracle**
- [Tham khảo](https://docs.djangoproject.com/en/3.0/ref/databases/#oracle-notes)
## **5) Sử dụng API Python Shell để tương tác Database**
- Để sử dụng những câu lệnh truy vấn trực tiếp đến Database, sử dụng API Shell có sẵn của **Django** .
- Sử dụng lệnh sau để kích hoạt chế độ **shell** :
    ```sh
    $ python3 manage.py shell
    ```
    <img src=https://i.imgur.com/bJ8XKCm.png>
- Muốn truy vấn bảng nào trong Database, cần import vào **shell** :
    ```py
    >>> from blog.models import Post
    ```
### **5.1) Insert giá trị vào bảng**
- Khởi tạo các đối tượng theo hướng **OOP** để insert giá trị vào các bảng :
    ```py
    >>> a = Post()
    >>> a.title = 'First Title'
    >>> a.body = 'First Body'
    >>> a.save()
    >>> b = Post()
    >>> b.title = 'Second Title'
    >>> b.body = 'Second Body'
    >>> b.save()
    ```
    - Hoặc có thể viết gọn lại như sau :
    ```py
    >>> a = Post(title='First Title', body='First Body')
    >>> a.save()
    >>> b = Post(title='Second Title', body='Second Body')
    >>> b.save()
    ```
- Sau khi tạo xong có thể sử dụng **DB Browser for SQLite** để kiểm tra bảng vừa tạo :
    - Thực hiện query truy vấn ( theo cấu trúc `[app_name]_[table_name]` ) :
        ```
        select * from blog_post;   
        ```
    - Kết quả hiển thị :

        <img src=https://i.imgur.com/B6tg6hT.png>

    - Giờ hiển thị ở đây có thể bị sai do cấu hình `TIME_ZONE` trong file `settings.py` đang để mặc định là "`UTC`" . Thay đổi `TIME_ZONE` thành "`Asia/Ho_Chi_Minh`" :
        
        <img src=https://i.imgur.com/96XIedF.png>

### **5.2) Cách select giá trị**
- Để show toàn bộ các record bên trong bảng `post`, sử dụng lệnh sau :
    ```py
    >>> Post.objects.all()
    <QuerySet [<Post: Post object (1)>, <Post: Post object (2)>]>
    ```
- Nếu query theo cách này thì sẽ không thể biết nội dung các record . Ta sẽ sử dụng mẹo để hiển thị các thông tin của record bằng cách thêm hàm `__str__` vào class `Post` :
    
    <img src=https://i.imgur.com/8eqGWZB.png>

    - Kết quả :
        ```py
        >>> Post.objects.all()
        <QuerySet [<Post: First Title>, <Post: Second Title>]>
        ```
### **5.3) Cách update giá trị record**
- Việc cập nhật dữ liệu ở **Django** khá đơn giản , ta chỉ cần truy vấn tìm object Post muốn cập nhật, thay đổi thuộc tính mình cần và dùng phương thức `save()` để cập nhật :
    ```py
    >>> a = Post.objects.get(id=1)
    >>> a.body = 'Changing Body'
    >>> a.save()
    ```