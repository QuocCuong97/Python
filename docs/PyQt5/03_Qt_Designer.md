# Sử dụng Qt Designer
- Bộ cài đặt **PyQt** đi kèm với một bộ công cụ xây dựng giao diện gọi là **Qt Designer**.
- Sử dụng giao diện drag-and-drop đơn giản, giao diện của app có thể được xây dựng mà không cần dòng code nào. Tuy nhiên, nó không phải IDE giống như **Visual Studio**. **Qt Designer** không có chức năng debug và build app.
- Truy cập **Qt Designer** :
    ```
    pyqt5-tools designer
    ```
- Giao diện chính của **Qt Designer** :

    <img src=https://i.imgur.com/RKmbx1j.png>

- Convert file `.ui` thành file `.py` :
    ```
    pyuic5 -x demo.ui -o demo.py
    ```
- Convert file `.src` thành file `.py` :
    ```
    pyrcc5 .\test.qrc -o test_rc.py
    ```