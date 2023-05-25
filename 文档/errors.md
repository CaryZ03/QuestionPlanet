# 1 api/user/

## models

```python
class Filler(Model):
    filler_id = AutoField(primary_key=True)
    filler_ip = CharField(max_length=30)
    filler_is_user = BooleanField(default=False)
    filler_user = ForeignKey('User', on_delete=SET_NULL, null=True)


class User(Model):
    user_id = AutoField(primary_key=True)
    user_name = CharField(max_length=100)
    user_password = CharField(max_length=20)
    user_email = EmailField(max_length=50, default=None, blank=True, null=True)
    user_tel = TextField(null=True)
    status_choices = (
        ('free', "未封禁"),
        ('banned', "封禁")
    )
    user_status = CharField(max_length=10, choices=status_choices, default='free')
    user_created_questionnaires = ManyToManyField(Questionnaire, related_name='created_by_users')
    user_filled_questionnaires = ManyToManyField(Questionnaire, related_name='filled_by_users')


class Admin(Model):
    admin_id = AutoField(primary_key=True)
    admin_name = CharField(max_length=100)
    admin_password = CharField(max_length=20)
```

## 100 system

1001：未登录

1002：登录信息已过期

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
    "email": email*,
    "tel": tel*
}
```

### 返回数据：

```json
{
    "errno": 0,
    "msg": "注册成功",
    "uid": 用户id
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
cookie:{
    "session_id": session_id
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
    'admin_id': admin_id
}
cookie:{
    "session_id": session_id
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
    "uid": uid
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
    "uid": uid
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
    "uid": uid
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
    "uid": uid
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
    "uid": uid,
    "username": username,
    "password1": password1,
    "password2": password2,
    "email": email*,
    "tel": tel*
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
    "uid": uid,
    "username": username,
    "password1": password1,
    "password2": password2,
    "email": email*,
    "tel": tel*
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

1111：用户名不合法

1112：用户名已存在

1113：两次输入的密码相同

1114：密码不合法

## 112 check_questionnaire_list

### 请求类型：GET

### 输入数据：

```json
{
    "uid": uid,
    "type": type("created", "filled")
}
```

### 返回数据：

```json
{
    "errno": 0,
    "msg": "返回问卷列表成功",
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

### 错误码：

1121：未指定问卷列表

## 113 change_user_status

### 请求类型：POST

### 输入数据：

```json
{
    "username": username,
    "status": status
}
```

### 返回数据：

```json
{
    "errno": 0,
    "msg": "用户封禁成功",
    "status": status
}
```

### 错误码：

1131：用户不存在

# 2 api/questionnaire

## models

```python
class Answer(Model):
    a_id = IntegerField(primary_key=True)
    a_answersheet = ForeignKey('Answersheet', on_delete=CASCADE, null=True)
    a_question = ForeignKey('Question', on_delete=CASCADE, null=True)
    a_content = TextField()
    a_score = DecimalField(max_digits=6, decimal_places=2, default=0)
    a_comment = TextField()


class Question(Model):
    q_id = IntegerField(primary_key=True)
    q_questionnaire = ForeignKey('Questionnaire', on_delete=CASCADE, null=True)
    question_types = (
        ('single', "单选"),
        ('multiple', "多选"),
        ('judge', "判断"),
        ('fill', "填空"),
        ('essay', "解答"),
        ('grade', "打分")
    )
    q_type = CharField(max_length=20, choices=question_types, default='single')
    q_title = TextField()
    q_description = TextField()
    q_option_count = IntegerField()
    q_options = JSONField()
    q_correct_answer = TextField()
    q_score = DecimalField(max_digits=6, decimal_places=2, default=0.0)
    q_answers = ManyToManyField(Answer)


class AnswerSheet(Model):
    as_id = IntegerField(primary_key=True)
    as_filler = ForeignKey('user.Filler', on_delete=CASCADE, null=True)
    as_questionnaire = ForeignKey('Questionnaire', on_delete=CASCADE, null=True)
    as_createTime = DateTimeField(auto_now_add=True)
    as_answers = ManyToManyField(Answer)
    as_score = IntegerField()
    as_temporary_save = JSONField(default='')
    as_submitted = BooleanField(default=False)


class Questionnaire(Model):
    qn_id = IntegerField(primary_key=True)
    qn_title = TextField()
    qn_description = TextField()
    qn_createTime = DateTimeField(auto_now_add=True)
    qn_endTime = DateTimeField(default=None)
    status_choices = (
        ('unpublished', "未发布"),
        ('published', "已发布"),
        ('closed', "已关闭"),
        ('banned', "已封禁")
    )
    qn_status = CharField(max_length=20, choices=status_choices, default='unpublished')
    qn_refillable = BooleanField(default=True)
    qn_questions = ManyToManyField(Question)
    qn_answersheets = ManyToManyField(AnswerSheet)
```

## 200 system

2001：问卷不存在

## 201 fill_questionnaire

### 描述：点击问卷链接时调用，创建新的答卷人或查找已存在答卷人，并创建新的答卷

### 请求类型：POST

### 输入数据：

```json
{
    "qn_id": 问卷id
}
```

### 返回数据：

```json
{
    "errno": 0,
    "msg": "答卷创建成功",
    "as_id": 答卷id, 
    "temp_save": 答卷暂存数据
}
```

### 错误码：无

## 202 save_answers

### 描述：暂存答卷，如果内容为空则删除答卷

### 请求类型：POST

### 输入数据：

```json
{
    "as_id": 答卷id,
    "answer_data": 答卷内容
}
```

### 返回数据：

```json
if answer_data != null
{
    "errno": 0,
    "msg": "答卷保存成功"
}
else
{
    "errno": 0,
    "msg": "答卷删除成功"
}
```

### 错误码：无

## 203 submit_answers

### 描述：提交答卷

### 请求类型：POST

### 输入数据：

```json
{
    "as_id": 答卷id,
    "answer_data": 答卷内容
}
```

### 返回数据：

```json
{
    "errno": 0,
    "msg": "答卷保存成功"
}
```

### 错误码：无

## 204 create_questionnaire

### 描述：创建空白问卷

### 请求类型：POST

### 输入数据：

```json
{
    "uid": 用户id
}
```

### 返回数据：

```json
{
    "errno": 0,
    "msg": "问卷创建成功",
    "qn_id": 问卷id
}
```

### 错误码：无

## 205 save_questionnaire

### 描述：保存问卷

### 请求类型：POST

### 输入数据：

```json
{
    "uid": 用户id,
    "qn_id": 问卷id,
    "qn_title": 问卷标题,
    "qn_description": 问卷描述,
    "qn_end_time": 问卷截止时间,
    "qn_refillable": 是否可重填,
    "question_data": [
        {
            "q_type": 问题类型,
            "q_title": 问题标题,
            "q_description": 问题描述,
            "q_option_count": 选项数,
            "q_options": 选项数据([选项1, ...]),
            "q_correct_answer": 正确答案,
            "q_score": 分数
        }，
        ...
    ]
}
```

### 返回数据：

```json
{
    "errno": 0,
    "msg": "问卷保存成功"
}
```

### 错误码：无

## 206 delete_questionnaire

### 描述：删除问卷

### 请求类型：POST

### 输入数据：

```json
{
    "uid": 用户id,
    "qn_id": 问卷id
}
```

### 返回数据：

```json
{
    "errno": 0,
    "msg": "问卷删除成功"
}
```

### 错误码：无

## 207 change_questionnaire_status

### 描述：更改问卷状态（打开、关闭、封禁、解封）

### 请求类型：POST

### 输入数据：

```json
{
    "uid": 用户id,
    "qn_id": 问卷id,
    "status": 目标状态(unpublished, published, closed, banned)
}
```

### 返回数据：

```json
{
    "errno": 0,
    "msg": "问卷状态更改成功"
}
```

### 错误码：无