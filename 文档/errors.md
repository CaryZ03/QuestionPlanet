## 101 user_register

请求类型：POST

输入数据：

```json
{
    "username": "username",
    "password1": "password1",
    "password2": "password2",
    "email": "email"
}
```

返回数据：

```json
{
    "uid": uid
}
```

错误码：

1011：用户名不合法

1012：用户名已存在

1013：两次输入的密码相同

1014：密码不合法

0：注册成功

## 102 user_login

请求类型：POST

输入数据：

```
{
    "username": "username",
    "password": "password"
}
```

1021：用户不存在

1022：密码错误

0：登录成功

103 admin_login

1031：管理员账号不存在

1032：密码错误

0：登录成功

104 logout

0：登出成功

105 check_profile

0：返回用户信息成功

106 check_profile_admin

0：返回管理员信息成功

107 change_profile

1071：用户名不合法

1072：用户名已存在

1073：两次输入的密码相同

1074：密码不合法

0：修改用户信息成功

108 change_profile_admin

1081：用户名不合法

1082：用户名已存在

1083：两次输入的密码相同

1084：密码不合法

0：修改用户信息成功

109 check_created_questionnaires

0：返回问卷列表成功

110 check_filled_questionnaires

0：返回问卷列表成功