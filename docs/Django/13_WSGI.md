# Sử dụng mod_wsgi để kết nối Django với Apache
## **1) Giới thiệu về `mod_wsgi`**
## **2) Các bước thực hiện**
- **B1 :** Update các package sẵn có :
    ```
    yum update -y
    yum upgrade -y
    ```
- **B2 :** Cài đặt **Python `3.6`** và các package hỗ trợ :
    ```
    yum install epel-release -y
    curl 'https://setup.ius.io/' -o setup-ius.sh
    sh setup-ius.sh
    yum install https://repo.ius.io/ius-release-el7.rpm https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
    yum repolist
    yum install -y python36u python36u-libs python36u-devel python36u-mod_wsgi
    ```
- **B3 :** Cài đặt **PIP** phiên bản mới nhất :
    ```
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python3 get-pip.py
    ```
- **B4 :** Cài đặt package `git`, `httpd` :
    ```
    yum install -y git httpd
    ```
- **B5 :** Cấu hình **firewalld** cho phép dịch vụ `httpd` ( trong trường hợp có sử dụng **firewalld** ) :
    ```
    firewall-cmd --zone=public --permanent --add-service=http
    firewall-cmd --reload
    ```
- **B6 :** Khởi động `httpd` và cho phép khởi động cùng hệ thống :
    ```
    systemctl start httpd
    systemctl enable httpd
    ```
- **B7 :** Truy cập vào đường dẫn `/var/www` và clone source code vào thư mục `project` :
    ```
    cd /var/www
    git clone https://github.com/QuocCuong97/Pricelist project
    ```
- **B8 :** Vào thư mục source code vừa tạo và tạo `virtualenv` :
    ```
    cd project
    pip install virtualenv==16.7.4
    virtualenv env_crawl
    ```
    ```
    /var/www/
    └── project
        ├── db.sqlite3
        ├── domain_price
        ├── env_crawl
        ├── manage.py
        ├── Pricelist
        ├── README.md
        ├── requirements.txt
        └── static
    ```
- **B9 :** Đổi môi trường sang virtualenv vừa tạo :
    ```
    source env_crawl/bin/activate
    (env_crawl) #
    ```
- **B10 :** Cài đặt các gói và thư viện cần thiết trong file `requirements.txt` :
    ```
    (env_crawl) # pip install -r requirements.txt
    ```
- **B11 :** Chỉnh sửa file `settings.py` của thư mục `Pricelist` để cho phép truy cập server từ xa . Thêm địa chỉ IP Public của server vào phần `ALLOW HOSTS` :
    ```
    ALLOWED HOSTS = ['10.10.34.156', '127.0.0.1']
    ```
    <img src=https://i.imgur.com/0bG7qki.png>

- **B12 :** Tạo mới file `crawl_pricelist.conf` trong thư mục `/etc/httpd/conf.d/` với nội dung sau (chú ý các đường dẫn) :
    ```
    vi /etc/httpd/conf.d/crawl_pricelist.conf
    ```
    ```
    <VirtualHost *:80>
    ServerName testings123.space
    Alias /static  /var/www/project/static
        <Directory  /var/www/project/static>
            AllowOverride All
            Require all granted
        </Directory>

        <Directory /var/www/project>
            <Files wsgi.py>
                Require all granted
            </Files>
        </Directory>

    WSGIDaemonProcess Pricelist python-path=/var/www/project/env_crawl/lib/python3.6/site-packages lang='en_US.UTF-8' locale='en_US.UTF-8' processes=6 threads=1
    WSGIProcessGroup Pricelist
    WSGIScriptAlias / /var/www/project/Pricelist/wsgi.py
    WSGIApplicationGroup %{GLOBAL}
    WSGIPassAuthorization On
    </VirtualHost>
    ```
- **B13 :** Chỉnh sửa file `wsgi.py` của thư mục `Pricelist` :
    ```py
    """
    WSGI config for Pricelist project.

    It exposes the WSGI callable as a module-level variable named ``application``.

    For more information on this file, see
    https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
    """
    import os
    import signal
    import sys
    import time
    import traceback

    from django.core.wsgi import get_wsgi_application

    sys.path.append('/var/www/project')
    sys.path.append('/var/www/project/env_crawl/lib/python3.6/site-packages')


    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Pricelist.settings')

    try:
        application = get_wsgi_application()
    except Exception:
        # Error loading applications
        if 'mod_wsgi' in sys.modules:
            traceback.print_exc()
            os.kill(os.getpid(), signal.SIGINT)
            time.sleep(2.5)
    ```
- **B14 :** Khởi động lại dịch vụ `httpd` :
    ```
    systemctl restart httpd
    ```
    => Kết quả hiển thị trên trình duyệt :

    <img src=https://i.imgur.com/XEtycuq.jpg>