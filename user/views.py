import re
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.http.response import JsonResponse
from django.contrib.sessions.models import Session
from django.utils import timezone
import json

from user.models import User, Admin, Filler
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


def get_session(session_id):
    # 查询会话对象
    session = Session.objects.get(session_key=session_id)

    # 检查会话是否已过期
    if session.expire_date < timezone.now():
        # 会话已过期，可以选择删除该会话
        session.delete()
        return None

    # 返回与会话关联的request.session对象
    return session.get_decoded()


def login_required(view_func):
    def wrapper(request, *args, **kwargs):
        session_id = request.COOKIES.get('session_id')
        if session_id:
            # 根据session_id获取相应的会话数据
            session_data = get_session(session_id)
            # 处理会话数据
            if session_data is None:
                return JsonResponse({'errno': 1002, 'msg': "登录信息已过期"})
            elif session_data.get('id') != json.loads(request.body).get('uid'):
                return JsonResponse({'errno': 1003, 'msg': "用户不一致"})
            else:
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
        session_id = request.COOKIES.get('session_id')
        if session_id:
            # 根据session_id获取相应的会话数据
            session_data = get_session(session_id)
            # 处理会话数据
            if session_data is None:
                return JsonResponse({'errno': 1002, 'msg': "登录信息已过期"})
            elif session_data.get('id') != json.loads(request.body).get('uid'):
                return JsonResponse({'errno': 1003, 'msg': "用户不一致"})
            elif session_data.get('role') != 'admin':
                return JsonResponse({'errno': 1004, 'msg': "需要管理员权限"})
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
    email = data_json.get('email')
    tel = data_json.get('tel')
    if not bool(re.match("^[A-Za-z0-9][A-Za-z0-9_]{2,20}$", str(username))):
        return JsonResponse({'errno': 1011, 'msg': "用户名不合法"})
    elif User.objects.filter(user_name=username).exists():
        return JsonResponse({'errno': 1012, 'msg': "用户名已存在"})
    elif password1 != password2:
        return JsonResponse({'errno': 1013, 'msg': "两次输入的密码不同"})
    elif not bool(re.match('^(?=.*\\d)(?=.*[a-zA-Z]).{6,20}$', str(password1))):
        return JsonResponse({'errno': 1014, 'msg': "密码不合法"})
    else:
        new_user = User.objects.create(user_name=username, user_password=password1, user_email=email, user_tel=tel)
        new_user.save()
        filler_ip = get_client_ip(request)
        new_filler = Filler.objects.create(filler_ip=filler_ip, filler_is_user=True, filler_user=new_user)
        new_filler.save()
        return JsonResponse({'errno': 0, 'msg': "注册成功", 'username': new_user.user_name})


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
            request.session['id'] = user.user_id
            request.session['role'] = 'user'
            request.session.save()
            session_id = request.session.session_key
            response = JsonResponse({'errno': 0, 'msg': "登录成功", 'uid': user.user_id})
            response.set_cookie('session_id', session_id)
            return response
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
            request.session['id'] = admin.admin_id
            request.session['role'] = 'admin'
            request.session.save()
            session_id = request.session.session_key
            response = JsonResponse({'errno': 0, 'msg': "管理员登录成功", 'adid': admin.admin_id})
            response.set_cookie('session_id', session_id)
            return response
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
    request.session.flush()
    return JsonResponse({'errno': 0, 'msg': "登出成功"})


@csrf_exempt
@login_required
@require_http_methods(['POST'])
def cancel_account(request):
    uid = json.loads(request.body).get('id')
    user = User.objects.get(user_id=uid)
    user.delete()
    return JsonResponse({'errno': 0, 'msg': "注销成功"})


@csrf_exempt
@login_required
@require_http_methods(['GET'])
def check_profile(request):
    data_json = json.loads(request.body)
    uid = data_json.get('uid')
    user = User.objects.get(user_id=uid)
    user_info = user.to_json()
    return JsonResponse({'errno': 0, 'msg': '返回用户信息成功', 'user_info': user_info})


@csrf_exempt
@admin_required
@require_http_methods(['GET'])
def check_profile_admin(request):
    data_json = json.loads(request.body)
    adid = data_json.get('uid')
    admin = Admin.objects.get(admin_id=adid)
    admin_info = admin.to_json()
    return JsonResponse({'errno': 0, 'msg': '返回管理员信息成功', 'admin_info': admin_info})


@csrf_exempt
@login_required
@require_http_methods(['POST'])
def change_profile(request):
    data_json = json.loads(request.body)
    uid = json.loads(request.body).get('id')
    username = data_json.get('username')
    password1 = data_json.get('password1')
    password2 = data_json.get('password2')
    mail = data_json.get('email')
    tel = data_json.get('tel')
    if not bool(re.match("^[A-Za-z0-9][A-Za-z0-9_]{2,20}$", str(username))):
        return JsonResponse({'errno': 1101, 'msg': "用户名不合法"})
    elif User.objects.filter(user_id__ne=uid, user_name=username).exists():
        return JsonResponse({'errno': 1102, 'msg': "用户名已存在"})
    elif password1 != password2:
        return JsonResponse({'errno': 1103, 'msg': "两次输入的密码不同"})
    elif not re.match('^(?=.*\\d)(?=.*[a-zA-Z]).{6,20}$', str(password1)):
        return JsonResponse({'errno': 1104, 'msg': "密码不合法"})
    else:
        user = User.objects.get(user_id=uid)
        user.user_name = username
        user.user_password = password1
        user.user_mail = mail
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
    mail = data_json.get('email')
    tel = data_json.get('tel')
    if not bool(re.match("^[A-Za-z0-9][A-Za-z0-9_]{2,20}$", str(username))):
        return JsonResponse({'errno': 1111, 'msg': "用户名不合法"})
    elif User.objects.filter(user_id__ne=uid, user_name=username).exists():
        return JsonResponse({'errno': 1112, 'msg': "用户名已存在"})
    elif password1 != password2:
        return JsonResponse({'errno': 1113, 'msg': "两次输入的密码不同"})
    elif not re.match('^(?=.*\\d)(?=.*[a-zA-Z]).{6,20}$', str(password1)):
        return JsonResponse({'errno': 1114, 'msg': "密码不合法"})
    else:
        user = User.objects.get(user_id=uid)
        user.user_name = username
        user.user_password = password1
        user.user_mail = mail
        user.user_tel = tel
        user.save()
        return JsonResponse({'errno': 0, 'msg': '修改用户信息成功'})


@csrf_exempt
@login_required
@require_http_methods(['GET'])
def check_questionnaire_list(request):
    uid = json.loads(request.body).get('id')
    qntype = json.loads(request.body).get('type')
    user = User.objects.get(user_id=uid)
    if qntype == 'created':
        questionnaires = user.user_created_questionnaires.all()
    elif qntype == 'filled':
        questionnaires = user.user_filled_questionnaires.all()
    else:
        return JsonResponse({'errno': 1121, 'msg': '未指定问卷列表'})
    qn_info = []
    for qn in questionnaires:
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
    return JsonResponse({'errno': 0, 'ver': "4"})
