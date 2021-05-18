# Sử dụng PyInstaller để build Python app
## **1) Vấn đề người dùng**
- Khởi tạo mội project **Python** có thể gây khó khăn, đặc biệt đối với những non-developers. Thông thường, việc đầu tiên là phải mở **Terminal** - thứ mà không phải ai cũng biết sử dụng. Những "bức tường" kỹ thuật này đã khiến người dùng khó đi tới cả những bước sâu vào các chi tiết thư thiết lập môi trường ảo, phiên bản **Python** hay cài đặt các dependency.
- Tưởng tượng các vấn đề xảy ra khi thiết lập một máy để phát triển **Python** :
    - Download và cài đặt một phiên bản **Python** cụ thể
    - Cài đặt `pip`
    - Cài đặt `virtualenv`
    - Clone code (from `git`)
    - Cài đặt các dependency
- Các bước trên hoàn toàn làm khó một người không hiểu về **Python**
## **2) Giới thiệu PyInstaller**
- **PyInstaller** cung cấp khả năng tạo một thư mục hoặc file thực thi mà người dùng có thể chạy ngay lập tức mà không cần cài đặt gì thêm.
- **PyInstaller** thực hiện việc này bằng cách tổ chức lại code **Python** của bạn, sau đó đóng gói chúng thành định dạng phù hợp tùy vào hệ điều hành của bạn.
- **PyInstaller** có thể tạo các tệp thực thi cho Windows, Linux và MacOS. Có nghĩa người dùng Windows sẽ nhận được file `.exe`, người dùng Linux sẽ nhận được file thực thi thông thường, ngường dùng MacOS sẽ nhận được file `.app`.
## **3) Sử dụng PyInstaller**
- **PyInstaller** yêu cầu ứng dụng của bạn tuân thủ một số kiến trúc tối thiểu, cụ thể là cần có file CLI để khởi động ứng dụng. Theo cách thông thường có nghĩa là cần tạo 1 file `main.py` ở phía ngoài để chạy ứng dụng. File này còn được gọi là ***entry-point script***.
- Cài đặt **PyInstaller** :
    ```
    $ pip install pyinstaller
    ```
- Chạy `pyinstaller` với ***entry-point script*** để sinh ra các thư mục/file mặc định cho app cần build:
    ```
    $ pyinstaller app.py
    ```
    ```
    259 INFO: PyInstaller: 4.3
    259 INFO: Python: 3.9.5
    274 INFO: Platform: Windows-10-10.0.19042-SP0
    277 INFO: wrote C:\Users\taikh\Documents\dynatrace-problem-report\app.spec
    287 INFO: UPX is not available.
    301 INFO: Extending PYTHONPATH with paths
    .....
    24717 INFO: Writing RT_ICON 1 resource with 3752 bytes
    24717 INFO: Writing RT_ICON 2 resource with 2216 bytes
    24718 INFO: Writing RT_ICON 3 resource with 1384 bytes
    24718 INFO: Writing RT_ICON 4 resource with 37019 bytes
    24718 INFO: Writing RT_ICON 5 resource with 9640 bytes
    24719 INFO: Writing RT_ICON 6 resource with 4264 bytes
    24719 INFO: Writing RT_ICON 7 resource with 1128 bytes
    24724 INFO: Appending archive to EXE C:\Users\taikh\Documents\dynatrace-problem-report\build\app\app.exe    
    25696 INFO: Building EXE from EXE-00.toc completed successfully.
    25700 INFO: checking COLLECT
    25701 INFO: Building COLLECT because COLLECT-00.toc is non existent
    25703 INFO: Building COLLECT COLLECT-00.toc
    32009 INFO: Building COLLECT COLLECT-00.toc completed successfully
    ```
- Theo mặc định, **PyInstaller** sẽ tạo ra những thứ sau :
    - Một file `.spec`
    - Một thư mục `build/`
    - Một thư mục `dist/`
### **Spec file**
- Spec file mặc định sẽ được đặt tên thoe file ***entry-point script***. Ví dụ nội dung file `app.spec` :
    ```spec
    # -*- mode: python ; coding: utf-8 -*-


    block_cipher = None


    a = Analysis(['app.py'],
                pathex=['C:\\Users\\taikh\\Documents\\dynatrace-problem-report'],
                binaries=[],
                datas=[],
                hiddenimports=[],
                hookspath=[],
                runtime_hooks=[],
                excludes=[],
                win_no_prefer_redirects=False,
                win_private_assemblies=False,
                cipher=block_cipher,
                noarchive=False)
    pyz = PYZ(a.pure, a.zipped_data,
                cipher=block_cipher)
    exe = EXE(pyz,
            a.scripts,
            [],
            exclude_binaries=True,
            name='app',
            debug=False,
            bootloader_ignore_signals=False,
            strip=False,
            upx=True,
            console=True )
    coll = COLLECT(exe,
                a.binaries,
                a.zipfiles,
                a.datas,
                strip=False,
                upx=True,
                upx_exclude=[],
                name='app')
    ```
### **Build folder**
- Thư mục `build/` là nơi **PyInstaller** đặt hầu hết các metadata là lưu trữ internal để xây dựng file thực thi. Nội dung thư mục như sau :
    ```
    build/
    |
    └── app/
        ├── Analysis-00.toc
        ├── base_library.zip
        ├── COLLECT-00.toc
        ├── EXE-00.toc
        ├── PKG-00.pkg
        ├── PKG-00.toc
        ├── PYZ-00.pyz
        ├── PYZ-00.toc
        ...
        ├── warn-cli.txt
        └── xref-cli.html
    ```
- Thư mục `build/` có thể hữu ích khi cần thực hiện debug.
### **Dist folder**
- Thư mục `dist/` chứa phần mềm đích cuối cùng. Bên trong thư mục `dist/` sẽ chứa 1 thư mục được đặt tên theo ***entry-point script*** chứa tất cả cá thành phần phục thuộc và có thể thực thi cho ứng dụng (`app.exe`)
- Có thể thấy nhiều file `.so`, `.pyd`, `.dll` tùy thuộc vào hệ điều hành. Đây là các thư viện được chia sẻ đại diện cho các dependency của project mà **PyInstaller** đã tạo và thu thập.