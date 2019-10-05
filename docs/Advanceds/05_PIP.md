# PIP
## **1) Khái niệm**
- **PIP** là trình quản lý các **package** , **module** bất kỳ tùy ý .
- Từ phiên bản `3.4` trở đi , **PIP** đã được cài đặt sẵn trong **Python** .
## **2) Cài đặt PIP**
### **2.1) Cài đặt trên Ubuntu**
#### **2.1.1) Cài đặt từ `yum` ( phiên bản thấp )**
- **B1 :** Update các gói phần mềm hệ thống :
    ```
    $ sudo apt-get update
    ```
- **B2 :** Tải về `pip` ( dành cho `python3` ) :
    ```
    $ sudo apt install -y python3-pip
    ```
- **B3 :** Kiểm tra phiên bản `pip` vừa cài đặt :
    ```
    $ pip3 --version     (hoặc pip3 -V)
    ```
    <img src=https://i.imgur.com/PDncPqL.png>

#### **2.1.2) Cài đặt từ source ( phiên bản mới nhất )**
- **B1 :** Tải về file `get-pip.py` :
    ```
    $ sudo apt install -y curl
    $ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    ```
- **B2 :** Chạy file `get-pip.py` :
    ```
    $ sudo python3 get-pip.py
    ```
- **B3 :** Kiểm tra lại phiên bản `pip` vừa cài đặt :
    ```
    $ pip --version     (hoặc pip -V)
    ```
    <img src=https://i.imgur.com/af966NV.png>
### **2.2) Cài đặt trên CentOS**
#### **2.2.1) Cài đặt từ `yum` ( phiên bản thấp )**
- **B1 :** Update các gói phần mềm hệ thống :
    ```
    # yum -y update
    ```
- **B2 :** Tải về `pip` ( dành cho `python3` ) :
    ```
    # yum -y install python3-pip
    ```
- **B3 :** Kiểm tra phiên bản `pip` vừa cài đặt :
    ```
    # pip3 --version     (hoặc pip3 -V)
    ```
    <img src=https://i.imgur.com/bXWKF8V.png>

#### **2.2.2) Cài đặt từ source ( phiên bản mới nhất )**
- **B1 :** Tải về file `get-pip.py` :
    ```
    # curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    ```
- **B2 :** Chạy file `get-pip.py` :
    ```
    # python3 get-pip.py
    ```
- **B3 :** Kiểm tra lại phiên bản `pip` vừa cài đặt :
    ```
    # pip --version     (hoặc pip -V)
    ```
    <img src=https://i.imgur.com/COYGf1l.png>
### **2.3) Cài đặt trên Windows**
- Mặc định , khi cài `python3` , `pip` đã được cài luôn trên Windows :

    <img src=https://i.imgur.com/OIMFCfT.png>