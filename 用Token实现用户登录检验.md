# 用Token实现用户登录检验

## 1. 模型定义

```python
class UserToken(Model):
    key = CharField(max_length=200, unique=True)
    is_admin = BooleanField(default=False)
    user = ForeignKey('User', on_delete=CASCADE, null=True)
    admin = ForeignKey('Admin', on_delete=CASCADE, null=True)
    expire_time = DateTimeField()
```

key是一个随机生成的key，在用户登录时生成并传递给前端并在传回时查找对应的Token。

## 2. 创建Token

```python
from django.core.management.utils import get_random_secret_key
from datetime import timedelta
from django.utils.timezone import now

def create_token(uid, is_admin):
    token_key = get_random_secret_key()
    expiry_time = now() + timedelta(minutes=20)
    if is_admin:
        admin = Admin.objects.get(admin_id=uid)
        token = UserToken(key=token_key, is_admin=is_admin, admin=admin, expire_time=expiry_time)
    else:
        user = User.objects.get(user_id=uid)
        token = UserToken(key=token_key, is_admin=is_admin, user=user, expire_time=expiry_time)
    token.save()

    return token.key
```

生成随机数作为`token_key`，使用Django中Model的方法操作token并保存到数据库，返回key。这里使用`timezone.now()`函数而不是`datetime.now()`是因为`datetime`是无时区的，而`timezone`是使用默认时区的，而`DateTimeField`是使用默认时区的，所以统一，不然后面可能有别的错误。

## 3. 用户登录

```python
@csrf_exempt
@require_http_methods(['POST'])
def user_login(request):
    data_json = json.loads(request.body)
    username = data_json.get('username')
    password = data_json.get('password')
    if User.objects.filter(user_name=username).exists():
        user = User.objects.get(user_name=username)
        if user.user_password == password:
            UserToken.objects.filter(user=user).delete()
            token_key = create_token(user.user_id, False)
            return JsonResponse({'errno': 0, 'msg': "登录成功", 'uid': user.user_id, 'token_key': token_key})
        else:
            return JsonResponse({'errno': 1022, 'msg': "密码错误"})
    else:
        return JsonResponse({'errno': 1021, 'msg': "用户不存在"})
```

将`token_key`包装到`response`中返回给前端，前端通过本地存储保存，并添加到`Headers`中的`Authorization`中，注意`Authorization`的数据只是一个字符串，而不是json格式，因此可以直接读出，或者可以直接带在`request.body`的数据里。

## 4. Token检验

```python
def login_required(view_func):
    def wrapper(request, *args, **kwargs):
        token_key = request.headers.get('Authorization')
        if token_key:
            # 使用 Token 模型的 objects.get 方法查找令牌
            token = UserToken.objects.get(key=token_key)
            if token is None or token.expire_time < now():
                return JsonResponse({'errno': 1002, 'msg': "登录信息已过期"})
            else:
                user = token.user
                if user.user_id != json.loads(request.body).get('uid'):
                    return JsonResponse({'errno': 1003, 'msg': "用户不一致"})
                else:
                    return view_func(request, *args, **kwargs)
        else:
            return JsonResponse({'errno': 1001, 'msg': "未登录"})
    return wrapper
```

从`Headers`中的`Authorization`中直接获得`token_key`，从`UserToken`类中获取相应的Token，并进行检验。这里就涉及到上文提到的时区问题了，在进行过期检验时如果使用`datetime.now()`会提示`naive`（无时区）和`aware`（有时区）的问题，因此统一使用`timezone.now()`。

## 5. 其它设置

在`settings.py`中，需添加

```
CORS_ALLOW_CREDENTIALS = True
```

以允许在跨域访问时带有请求头`Headers`

```
CORS_ALLOW_HEADERS = [
    'Authorization',
]
```

以允许`Authorization`请求头

要求不高的话可以把请求头限制和请求方法限制都删掉，少很多问题。
