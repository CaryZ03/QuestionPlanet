import re
from django.db.models import Q
from django.utils.timezone import now
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.http.response import JsonResponse
from datetime import timedelta
from django.core.management.utils import get_random_secret_key
import json

from user.models import User, Admin, Filler, UserToken
from questionnaire.models import Questionnaire
from random import randint
import smtplib
from email.mime.text import MIMEText
from email.header import Header


def send_email_verification(email, code):
    # 邮件内容
    subject = "验证码"
    message = code
    sender = "2843004375@qq.com"  # 发件人邮箱
    receiver = email  # 收件人邮箱

    # 邮件对象
    msg = MIMEText(message, "plain", "utf-8")
    msg["Subject"] = Header(subject, "utf-8")
    msg["From"] = sender
    msg["To"] = receiver
    
    # SMTP服务器和端口
    smtp_server = "smtp.qq.com"
    smtp_port = 465
    
    # 发件人邮箱和授权码
    username = "2843004375@qq.com"
    password = "atawlpndwpqodfhe"
    
    # 连接SMTP服务器并发送邮件
    with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
        server.login(username, password)
        server.sendmail(sender, receiver, msg.as_string())


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
                # if (request.method == 'POST' and user.user_id != json.loads(request.body).get('uid')) \
                #         or (request.method == 'GET' and user.user_id != request.GET.get('uid')):
                #     return JsonResponse({'errno': 1003, 'msg': "用户不一致"})
                # else:
                return view_func(request, *args, **kwargs)
        else:
            return JsonResponse({'errno': 1001, 'msg': "未登录"})
    return wrapper


# def not_login_required(view_func):
#     def wrapper(request, *args, **kwargs):
#         if not request.session.items():
#             return view_func(request, *args, **kwargs)
#         else:
#             return JsonResponse({'errno': 1002, 'msg': "已登录"})
#     return wrapper


def admin_required(view_func):
    def wrapper(request, *args, **kwargs):
        token_key = request.headers.get('Authorization')
        if token_key:
            # 使用 Token 模型的 objects.get 方法查找令牌
            token = UserToken.objects.get(key=token_key)
            if token is None or token.expire_time < now():
                return JsonResponse({'errno': 1002, 'msg': "登录信息已过期"})
            elif not token.is_admin:
                return JsonResponse({'errno': 1004, 'msg': "需要管理员权限"})
            else:
                admin = token.admin
                if admin.admin_id != json.loads(request.body).get('uid'):
                    return JsonResponse({'errno': 1003, 'msg': "用户不一致"})
                else:
                    return view_func(request, *args, **kwargs)
        else:
            return JsonResponse({'errno': 1001, 'msg': "未登录"})
    return wrapper


@csrf_exempt
# @not_login_required
@require_http_methods(['POST'])
def user_register(request):
    from questionnaire.views import get_client_ip
    data_json = json.loads(request.body)
    username = data_json.get('username')
    password1 = data_json.get('password1')
    password2 = data_json.get('password2')
    if not bool(re.match("^[A-Za-z0-9][A-Za-z0-9_]{2,29}$", str(username))):
        return JsonResponse({'errno': 1011, 'msg': "用户名不合法"})
    elif User.objects.filter(user_name=username).exists():
        return JsonResponse({'errno': 1012, 'msg': "用户名已存在"})
    elif password1 != password2:
        return JsonResponse({'errno': 1013, 'msg': "两次输入的密码不同"})
    elif not bool(re.match('^(?=.*\\d)(?=.*[a-zA-Z]).{6,20}$', str(password1))):
        return JsonResponse({'errno': 1014, 'msg': "密码不合法"})
    else:
        new_user = User.objects.create(user_name=username, user_password=password1)
        new_user.save()
        filler_ip = get_client_ip(request)
        new_filler = Filler.objects.create(filler_ip=filler_ip, filler_is_user=True, filler_user=new_user)
        new_filler.save()
        return JsonResponse({'errno': 0, 'msg': "注册成功", 'uid': new_user.user_id})


@csrf_exempt
# @not_login_required
@require_http_methods(['POST'])
def user_login(request):
    data_json = json.loads(request.body)
    username = data_json.get('username')
    password = data_json.get('password')
    if User.objects.filter(user_name=username).exists():
        user = User.objects.get(user_name=username)
        if user.user_password == password:
            # UserToken.objects.filter(user=user).delete()
            token_key = create_token(user.user_id, False)
            return JsonResponse({'errno': 0, 'msg': "登录成功", 'uid': user.user_id, 'token_key': token_key})
        else:
            return JsonResponse({'errno': 1022, 'msg': "密码错误"})
    else:
        return JsonResponse({'errno': 1021, 'msg': "用户不存在"})


@csrf_exempt
# @not_login_required
@require_http_methods(['POST'])
def admin_login(request):
    data_json = json.loads(request.body)
    admin_name = data_json.get('admin_name')
    password = data_json.get('password')
    if Admin.objects.filter(admin_name=admin_name).exists():
        admin = Admin.objects.get(admin_name=admin_name)
        if admin.admin_password == password:
            UserToken.objects.filter(admin=admin).delete()
            token_key = create_token(admin.admin_id, True)
            return JsonResponse({'errno': 0, 'msg': "管理员登录成功", 'admin_id': admin.admin_id, 'token_key': token_key})
        else:
            return JsonResponse({'errno': 1032, 'msg': "密码错误"})
    else:
        return JsonResponse({'errno': 1031, 'msg': "管理员账号不存在"})


@csrf_exempt
# @not_login_required
@require_http_methods(['POST'])
def send_verification_code(request):
    data_json = json.loads(request.body)
    username = data_json.get('username')
    if User.objects.filter(user_name=username).exists():
        user = User.objects.get(user_name=username)
        email = user.user_email
        if email:
            code = randint(100000, 999999)
            send_email_verification(email, str(code))
            return JsonResponse({'errno': 0, 'msg': '邮件发送成功', 'code': code})
        return JsonResponse({'errno': 1042, 'msg': '邮箱不存在'})
    else:
        return JsonResponse({'errno': 1041, 'msg': "用户不存在"})


@csrf_exempt
# @not_login_required
@require_http_methods(['POST'])
def reset_password(request):
    data_json = json.loads(request.body)
    username = data_json.get('username')
    password1 = data_json.get('password1')
    password2 = data_json.get('password2')
    if User.objects.filter(user_name=username).exists():
        user = User.objects.get(user_name=username)
        if password1 != password2:
            return JsonResponse({'errno': 1052, 'msg': "两次输入的密码不同"})
        elif not re.match('^(?=.*\\d)(?=.*[a-zA-Z]).{6,20}$', str(password1)):
            return JsonResponse({'errno': 1053, 'msg': "密码不合法"})
        else:
            user.password = password1
            user.save()
            return JsonResponse({'errno': 0, 'msg': "重置密码成功"})
    else:
        return JsonResponse({'errno': 1051, 'msg': "用户不存在"})


@csrf_exempt
@login_required
@require_http_methods(['POST'])
def logout(request):
    token_key = request.headers.get('Authorization')
    # UserToken.objects.get(key=token_key).delete()
    return JsonResponse({'errno': 0, 'msg': "登出成功"})


@csrf_exempt
@login_required
@require_http_methods(['POST'])
def cancel_account(request):
    uid = json.loads(request.body).get('id')
    user = User.objects.get(user_id=uid)
    UserToken.objects.filter(user=user).delete()
    user.delete()
    return JsonResponse({'errno': 0, 'msg': "注销成功"})


@csrf_exempt
@login_required
@require_http_methods(['GET'])
def check_profile(request):
    uid = request.GET.get('uid')
    user = User.objects.get(user_id=uid)
    user_info = user.to_json()
    return JsonResponse({'errno': 0, 'msg': '返回用户信息成功', 'user_info': user_info})


@csrf_exempt
@admin_required
@require_http_methods(['GET'])
def check_profile_admin(request):
    data_json = json.loads(request.body)
    admin_id = data_json.get('uid')
    admin = Admin.objects.get(admin_id=admin_id)
    admin_info = admin.to_json()
    return JsonResponse({'errno': 0, 'msg': '返回管理员信息成功', 'admin_info': admin_info})


@csrf_exempt
@login_required
@require_http_methods(['POST'])
def change_profile(request):
    data_json = json.loads(request.body)
    uid = data_json.get('uid')
    username = data_json.get('username')
    password1 = data_json.get('password1')
    password2 = data_json.get('password2')
    signature = data_json.get('signature')
    email = data_json.get('email')
    tel = data_json.get('tel')
    if not bool(re.match("^[A-Za-z0-9][A-Za-z0-9_]{2,29}$", str(username))):
        return JsonResponse({'errno': 1101, 'msg': "用户名不合法"})
    elif User.objects.filter(~Q(user_id=uid) & Q(user_name=username)).exists():
        return JsonResponse({'errno': 1102, 'msg': "用户名已存在"})
    elif password1 != password2:
        return JsonResponse({'errno': 1103, 'msg': "两次输入的密码不同"})
    elif not re.match('^(?=.*\\d)(?=.*[a-zA-Z]).{6,20}$', str(password1)):
        return JsonResponse({'errno': 1104, 'msg': "密码不合法"})
    else:
        user = User.objects.get(user_id=uid)
        user.user_name = username
        user.user_password = password1
        user.user_signature = signature
        user.user_email = email
        user.user_tel = tel
        user.save()
        return JsonResponse({'errno': 0, 'msg': '修改用户信息成功'})


@csrf_exempt
@admin_required
@require_http_methods(['POST'])
def change_profile_admin(request):
    data_json = json.loads(request.body)
    uid = data_json.get('uid')
    username = data_json.get('username')
    password1 = data_json.get('password1')
    password2 = data_json.get('password2')
    signature = data_json.get('signature')
    email = data_json.get('email')
    tel = data_json.get('tel')
    if not bool(re.match("^[A-Za-z0-9][A-Za-z0-9_]{2,29}$", str(username))):
        return JsonResponse({'errno': 1111, 'msg': "用户名不合法"})
    elif User.objects.filter(~Q(user_id=uid) & Q(user_name=username)).exists():
        return JsonResponse({'errno': 1112, 'msg': "用户名已存在"})
    elif password1 != password2:
        return JsonResponse({'errno': 1113, 'msg': "两次输入的密码不同"})
    elif not re.match('^(?=.*\\d)(?=.*[a-zA-Z]).{6,20}$', str(password1)):
        return JsonResponse({'errno': 1114, 'msg': "密码不合法"})
    else:
        user = User.objects.get(user_id=uid)
        user.user_name = username
        user.user_password = password1
        user.user_signature = signature
        user.user_email = email
        user.user_tel = tel
        user.save()
        return JsonResponse({'errno': 0, 'msg': '修改用户信息成功'})


@csrf_exempt
@login_required
@require_http_methods(['GET'])
def check_questionnaire_list(request, qn_list_type):
    uid = request.GET.get('uid')
    user = User.objects.get(user_id=uid)
    if qn_list_type == 'created' or qn_list_type == 'deleted':
        questionnaires = user.user_created_questionnaires.all()
    elif qn_list_type == 'filled':
        questionnaires = user.user_filled_questionnaires.all()
    else:
        return JsonResponse({'errno': 1121, 'msg': '未指定问卷列表'})
    qn_info = []
    if qn_list_type == 'deleted':
        for qn in questionnaires:
            if qn.qn_status == 'deleted':
                qn_info.append(qn.to_json())
    else:
        for qn in questionnaires:
            if qn.qn_status != 'deleted':
                qn_info.append(qn.to_json())
    return JsonResponse({'errno': 0, 'msg': '返回问卷列表成功', 'qn_info': qn_info})


@csrf_exempt
@admin_required
@require_http_methods(['POST'])
def change_user_status(request):
    data_json = json.loads(request.body)
    username = data_json.get('username')
    status = data_json.get('status')
    if not User.objects.filter(username=username).exists():
        return JsonResponse({'errno': 1131, 'msg': "用户不存在"})
    else:
        user = User.objects.get(user_name=username)
        user.status = status
        user.save()
        return JsonResponse({'errno': 0, 'msg': "用户状态更改成功", 'status': status})


@csrf_exempt
@require_http_methods(['POST'])
def deploy_test(request):
    return JsonResponse({'errno': 0, 'ver': "5", 'cur_time': now()})
