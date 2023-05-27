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
def create_token(uid, is_admin):
    token_key = get_random_secret_key()
    expiry_time = now() + timedelta(minutes=20)
    if is_admin:
        admin = Admin.objects.get(admin_id=uid)
        token = UserToken(key=token_key, admin=admin, expire_time=expiry_time)
    else:
        user = User.objects.get(user_id=uid)
        token = UserToken(key=token_key, user=user, expire_time=expiry_time)
    token.save()

    return token.key
```

