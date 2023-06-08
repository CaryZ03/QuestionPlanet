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
    user_signature = TextField(null=True)
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


class UserToken(Model):
    key = CharField(max_length=200, unique=True)
    is_admin = BooleanField(default=False)
    user = ForeignKey('User', on_delete=CASCADE, null=True)
    admin = ForeignKey('Admin', on_delete=CASCADE, null=True)
    expire_time = DateTimeField()
```

## 100 system

1001：未登录

1002：登录信息已过期

1003：需要管理员权限

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
    "uid": user_id,
    "token_key": token_key
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
    'admin_id': admin_id,
	"token_key": token_key
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
    "username": username或
    "email": email
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

1043：邮件发送失败

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

### Header：Authorization

### 输入数据：无

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

### Header：Authorization

### 输入数据：无

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

### Header：Authorization

### 输入数据：无

### 返回数据：

```json
{
    'errno': 0,
    'msg': '返回用户信息成功',
    'user_info': {
            "user_id": user.user_id,
            "user_name": user.user_name,
            "user_password": user.user_password,
            "user_signature": self.user_signature,
            "user_email": user.user_email,
            "user_tel": self.user_tel,
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

### Header：Authorization

### 输入数据：

```json
{
    "username": username,
    "password1": password1,
    "password2": password2,
    "signature": signature,
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

### Header：Authorization

### 输入数据：

```json
{
    "username": username,
    "password1": password1,
    "password2": password2,
    "signature": signature,
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

### URL：check_questionnaire_list/<qn_list_type>?uid=uid

### 请求类型：GET

### Header：Authorization

### 输入数据：无

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

## 114 upload_avatar

### 请求类型：POST

### Header：Authorization

### 输入数据：

```json
{
    "data": base64
}
```

### 返回数据：

```json
{
    "errno": 0,
    "msg": "用户头像更改成功"
}
```

### 错误码：无

## 114 check_token

### 请求类型：GET

### Header：Authorization

### 输入数据：无

### 返回数据：

```json
{
    "errno": 0,
    "msg": "token有效"
}
```

### 错误码：

1151：token错误

# 2 api/questionnaire

## models

```python
class Answer(Model):
    a_id = AutoField(primary_key=True)
    a_answersheet = ForeignKey('Answersheet', on_delete=CASCADE, null=True)
    a_question = ForeignKey('Question', on_delete=CASCADE, null=True)
    a_content = TextField(null=True)
    a_score = DecimalField(max_digits=6, decimal_places=2, default=0)
    a_comment = TextField(null=True)


class Question(Model):
    q_id = AutoField(primary_key=True)
    q_questionnaire = ForeignKey('Questionnaire', on_delete=CASCADE, null=True)
    q_position = IntegerField(default=0)
    question_types = (
        ('single', "单选"),
        ('multiple', "多选"),
        ('judge', "判断"),
        ('fill', "填空"),
        ('essay', "解答"),
        ('grade', "打分")
    )
    q_type = CharField(max_length=20, choices=question_types, default='single')
    q_mandatory = BooleanField(default=False)
    q_title = TextField(null=True)
    q_description = TextField(null=True)
    q_option_count = IntegerField(default=1)
    q_options = JSONField(null=True)
    q_correct_answer = TextField(null=True)
    q_score = DecimalField(max_digits=6, decimal_places=2, default=0.0)
    q_answers = ManyToManyField(Answer)


class AnswerSheet(Model):
    as_id = AutoField(primary_key=True)
    as_filler = ForeignKey('user.Filler', on_delete=CASCADE, null=True)
    as_questionnaire = ForeignKey('Questionnaire', on_delete=CASCADE, null=True)
    as_createTime = DateTimeField(auto_now_add=True)
    as_answers = ManyToManyField(Answer)
    as_score = IntegerField(default=0)
    as_temporary_save = JSONField(default=None, null=True)
    as_submitted = BooleanField(default=False)


class Questionnaire(Model):
    qn_id = AutoField(primary_key=True)
    qn_title = TextField(null=True)
    qn_description = TextField(null=True)
    qn_creator = ForeignKey('user.User', on_delete=SET_NULL, null=True)
    qn_createTime = DateTimeField(auto_now_add=True)
    qn_endTime = DateTimeField(default=None, null=True)
    status_choices = (
        ('unpublished', "未发布"),
        ('published', "已发布"),
        ('closed', "已关闭"),
        ('banned', "已封禁"),
        ('deleted', "已删除")
    )
    qn_status = CharField(max_length=20, choices=status_choices, default='unpublished')
    qn_refillable = BooleanField(default=True)
    qn_questions = ManyToManyField(Question)
    qn_answersheets = ManyToManyField(AnswerSheet)
    qn_data_json = JSONField(default=None, null=True)
```

## 200 system

2001：问卷不存在

## 201 fill_questionnaire

### 描述：点击问卷链接时调用，创建新的答卷人或查找已存在答卷人，并创建新的答卷

### URL：fill_questionnaire/<qn_id>

### 请求类型：POST

### Header：Authorization

### 输入数据：无

### 返回数据：

```json
{
    "errno": 0,
    "msg": "答卷创建成功",
    "as_id": 答卷id, 
    "temp_save": 答卷暂存数据
}
```

### 错误码：

2011：问卷不存在

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

### 错误码：

2021：答卷不存在

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

### 错误码：

2031：答卷不存在

## 204 create_questionnaire

### 描述：创建空白问卷

### 请求类型：POST

### Header：Authorization

### 输入数据：无

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

### Header：Authorization

### 输入数据：

```json
{
    "qn_id": 问卷id,
    "qn_title": 问卷标题,
    "qn_description": 问卷描述,
    "qn_end_time": 问卷截止时间,
    "qn_refillable": 是否可重填,
    "question_list": [
        {
            "q_type": 问题类型,
            "q_mandatory": 是否必填,
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

## 205 copy_questionnaire

### 描述：复制问卷

### URL：fill_questionnaire/<qn_id>

### 请求类型：POST

### Header：Authorization

### 输入数据：无

### 返回数据：

```json
{
    "errno": 0,
    "msg": "问卷复制成功",
    "qn_id": 新问卷id
}
```

### 错误码：无

## 207 check_questionnaire

### 描述：查看问卷

### URL：check_questionnaire/<qn_id>

### 请求类型：GET

### 输入数据：无

### 返回数据：

```json
{
    "qn_info":{
        "qn_id": self.qn_id,
        "qn_title": self.qn_title,
        "qn_description": self.qn_description,
        "qn_createTime": str(self.qn_createTime),
        "qn_endTime": str(self.qn_endTime),
        "qn_status": self.qn_status,
        "qn_refillable": self.qn_refillable,
        "qn_answersheet_count": self.qn_answersheets.count()
    },
    "question_list": [
        {
            "q_id": self.q_id,
            "q_questionnaire": self.q_questionnaire,
            "q_position": self.q_position,
            "q_type": self.q_type,
            "q_mandatory": self.q_mandatory,
            "q_title": self.q_title,
            "q_description": self.q_description,
            "q_option_count": self.q_option_count,
            "q_options": self.q_options,
            "q_correct_answer": self.q_correct_answer,
            "q_score": self.q_score
        }，
        ...
    ]
}
```

### 错误码：无

## 208 delete_questionnaire

### 描述：删除问卷

### 请求类型：POST

### Header：Authorization

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
    "msg": "问卷删除成功"
}
```

### 错误码：无

## 209 change_questionnaire_status

### 描述：更改问卷状态（打开、关闭、封禁、解封）

### 请求类型：POST

### 输入数据：

```json
{
    "uid": 用户id,
    "qn_id": 问卷id,
    "status": 目标状态('unpublished', 'published', 'closed', 'banned', 'deleted')
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