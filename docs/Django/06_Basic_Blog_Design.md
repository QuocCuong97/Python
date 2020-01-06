# Thiết kết một blog cơ bản
- **B1 :** Tạo 1 app mới :
    ```sh
    $ python3 manage.py startapp blog
    ```
    ```
    PythonWeb/
    ├── blog
    ├── db.sqlite3
    ├── home
    ├── manage.py
    ├── PythonWeb
    └── static

    4 directories, 2 files
    ```
- **B2 :** Ở phần `INSTALLED_APPS` trong file `settings.py` , thêm app `blog` vừa tạo :

    <img src=https://i.imgur.com/mkiKu4j.png>

- **B3 :** Thực hiện migrate để apply file `settings.py` :
    ```sh
    $ python3 manage.py migrate
    ```
- **B4 :** Thiết kế  cơ bản trong file `base.html` :
    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">
      {% load static %}
      <link rel="stylesheet" type="text/css" href="{% static 'css/bootstrap.min.css' %}">
      <script src="{% static 'js/bootstrap.min.js' %}"></script>
      <title>{% block title %}{% endblock %}</title>
    </head>
    <body>
    <div class="container-fluid">
      <div class="row">
        <div class="col-sm-2">
          <center><img src="{% static 'images/logo.png' %}" class="responsive-img" style="max-height:150px"/></center>
        </div>
        <div class="col-sm-10 bg-info">
          <center><h1>Blog về Python</h1></center>
        </div>
      </div>
    </div>
    {% block content %}
    
    {% endblock %}
    </body>
    </html>
    ```
    - Hiển thị trên trình duyệt :

        <img src=https://i.imgur.com/sldNmM3.png>

- **B5 :** Thiết kế **sidebar** :
    ```html
    <div class="row">
      <div class="col-sm-2">
        <div class="bs-sliderbar" style="background-color: #ffffff;">
        <ul class="nav flex-column">
            <li><a href="#"> Thông tin cá nhân</a></li>
            <li><a href="#"> Bài viết</a></li>
            <li><a href="#"> Liên hệ</a></li>
        </ul>
        </div>
      </div>
      <div class="col-sm-10">
        {% block content %}

        {% endblock %}  
      </div>
    </div>
    ```
    - Hiển thị trên trình duyệt :

        <img src=https://i.imgur.com/HvAszJd.png>

- **B6 :** Thiết kế **footer** :
    ```html
    <footer>
      <div class="container-fluid">
        <a href="#">Facebook</a> | <a href="#">Twitter</a> | <a href="#">Instagram</a>
      </div>
    </footer>
    ```
    

