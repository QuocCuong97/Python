# Thao tác với User và quyền
- Chuyển đổi user để làm việc :
    ```py
    >>> switch_user(username, password)
    ```
- Show các user :
    ```py
    >>> client.get_list_users()
    ```
    ```
    [{'user': 'telegraf', 'admin': False}]
    ```
- Show các quyền được gán cho user :
    ```py
    >>> client.get_list_privileges(username)
    ```
    ```
    [{'database': 'telegraf', 'privilege': 'ALL PRIVILEGES'}]
    ```
- Tạo user mới :
    ```py
    >>> client.create_user(username, password, admin=False)
    ```
    - Trong đó : `admin` là quyền cao nhất, set là `True` để nhóm user vào quyền administrator
- Đổi password cho user có sẵn :
    ```py
    >>> set_user_password(username, password)
    ```
    
- Xóa user :
    ```py
    >>> client.drop_user(username)
    ```
- Cấp quyền admin cho user :
    ```py
    >>> client.grant_admin_privileges(username)
    ```
- Cấp quyền cho user trên database cụ thể :
    ```py
    >>> client.grant_privilege(privilege, database, username)
    ```
    - Trong đó: 
        - `privilege` là một trong các quyền `read`, `write`, `all`
- Thu hồi quyền admin :
    ```py
    >>> client.revoke_admin_privileges(username)
    ```
- Thu hồi quyền của user trên database cụ thể :
    ```py
    >>> revoke_privilege(privilege, database, username)
    ```
    - Trong đó: 
        - `privilege` là một trong các quyền `read`, `write`, `all`