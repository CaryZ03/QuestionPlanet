# 1 api/user/

## 100 system

1001：未登录

1002：已登录

1003：用户不一致

1004：需要管理员权限

## 101 user_register

### 请求类型：POST

### 输入数据：

```json
{
    "username": username,
    "password1": password1,
    "password2": password2,
    "email": email*
}
```

### 返回数据：

```json
{
    "errno": 0,
    "msg": "注册成功",
    "username": user_name
}
```

### 错误码：

1011：用户名不合法

1012：用户名已存在

1013：两次输入的密码相同

1014：密码不合法

## 102 user_login

### 请求类型：POST

### 输入数据：

```json
{
    "username": username,
    "password": password
}
```

### 返回数据：

```json
{
    "errno": 0,
    "msg": "登录成功",
    "uid": user_id
}
```

### 错误码：

1021：用户不存在

1022：密码错误

## 103 admin_login

### 请求类型：POST

### 输入数据：

```json
{
    "adminname": adminname,
    "password": password
}
```

### 返回数据：

```json
{
    "errno": 0,
    "msg": "管理员登录成功",
    'adid': admin_id
}
```

### 错误码：

1031：管理员账号不存在

1032：密码错误

## 104 send_verification_code

### 请求类型：POST

### 输入数据：

```json
{
    "username": username
}
```

### 返回数据：

```json
{
    "errno": 0,
    "msg": "邮件发送成功",
    "code": code
}
```

### 错误码：

1041：用户不存在

1042：邮箱不存在

## 105 reset_password

### 请求类型：POST

### 输入数据：

```json
{
    "username": username,
    "password1": password1,
    "password2": password2
}
```

### 返回数据：

```json
{
    "errno": 0,
    "msg": "重置密码成功"
}
```

### 错误码：

1051：用户不存在

1052：两次输入的密码相同

1053：密码不合法

## 106 logout

### 请求类型：POST

### 输入数据：

```json
{
    "id": id
}
```

### 返回数据：

```json
{
    "errno": 0,
    "msg": "登出成功"
}
```

### 错误码：无

## 107 cancel_account

### 请求类型：POST

### 输入数据：

```json
{
    "id": id
}
```

### 返回数据：

```json
{
    "errno": 0,
    "msg": "注销成功"
}
```

### 错误码：无

## 108 check_profile

### 请求类型：GET

### 输入数据：

```json
{
    "id": id
}
```

### 返回数据：

```json
{
    'errno': 0,
    'msg': '返回用户信息成功',
    'user_info': {
            "user_id": user.user_id,
            "user_name": user.user_name,
            "user_password": user.user_password,
            "user_email": user.user_email,
            "user_status": user.user_status
    }
}
```

### 错误码：无

## 109 check_profile_admin

### 请求类型：GET

### 输入数据：

```json
{
    "id": id
}
```

### 返回数据：

```json
{
    'errno': 0,
    'msg': '返回管理员信息成功',
    'admin_info': {
        "admin_id": admin.admin_id,
        "admin_name": admin.admin_name,
        "admin_password": admin.admin_password
    }
}
```

### 错误码：无

## 110 change_profile

### 请求类型：POST

### 输入数据：

```json
{
    "id": id,
    "username": username,
    "password1": password1,
    "password2": password2,
    "email": email*
}
```

### 返回数据：

```json
{
    "errno": 0,
    "msg": "修改用户信息成功"
}
```

### 错误码：

1101：用户名不合法

1102：用户名已存在

1103：两次输入的密码相同

1104：密码不合法

## 111 change_profile_admin

### 请求类型：POST

### 输入数据：

```json
{
    "id": id,
    "username": username,
    "password1": password1,
    "password2": password2,
    "email": email*
}
```

### 返回数据：

```json
{
    "errno": 0,
    "msg": "修改用户信息成功"
}
```

### 错误码：

1081：用户名不合法

1082：用户名已存在

1083：两次输入的密码相同

1084：密码不合法

## 112 check_created_questionnaires

### 请求类型：GET

### 输入数据：

```json
{
    "id": id
}
```

### 返回数据：

```json
{
    "errno": 0,
    "msg": "返回已创建问卷列表成功",
    'qn_info': [
        {
            "qn_id": qn_id,
            "qn_title": qn_title,
            "qn_description": qn_description,
            "qn_createTime": qn_createTime,
            "qn_endTime": qn_endTime,
            "qn_status": qm_status,
            "qn_refillable": qn_refillable
        },
        ...
    ]
}
```

### 错误码：无

## 113 check_filled_questionnaires

### 请求类型：GET

### 输入数据：

```json
{
    "id": id
}
```

### 返回数据：

```json
{
    "errno": 0,
    "msg": "返回已填写问卷列表成功",
    'qn_info': [
        {
            "qn_id": qn_id,
            "qn_title": qn_title,
            "qn_description": qn_description,
            "qn_createTime": qn_createTime,
            "qn_endTime": qn_endTime,
            "qn_status": qm_status,
            "qn_refillable": qn_refillable
        },
        ...
    ]
}
```

### 错误码：无

## 114 ban_user

### 请求类型：POST

### 输入数据：

```json
{
    "username": username
}
```

### 返回数据：

```json
{
    "errno": 0,
    "msg": "用户封禁成功"
}
```

### 错误码：

1141：用户不存在

## 115 un_ban_user

### 请求类型：POST

### 输入数据：

```json
{
    "username": username
}
```

### 返回数据：

```json
{
    "errno": 0,
    "msg": "用户解封成功"
}
```

### 错误码：

1151：用户不存在