from django.shortcuts import render
import re
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.http.response import JsonResponse
from django.core import serializers
import json
from user.models import User, Admin
from questionnaire.models import Questionnaire
from random import randint
import requests
from django.core.cache import cache


def login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.session.items():
            return JsonResponse({'errno': 1002, 'msg': "未登录"})
        elif request.session['id'] != json.loads(request.body).get('id'):
            return JsonResponse({'errno': 1003, 'msg': "用户不一致"})
        else:
            return view_func(request, *args, **kwargs)
    return wrapper


def not_login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.session.items():
            return view_func(request, *args, **kwargs)
        else:
            return JsonResponse({'errno': 1003, 'msg': "已登录"})
    return wrapper


def admin_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.session['admin'] == 'admin':
            return view_func(request, *args, **kwargs)
        else:
            return JsonResponse({'errno': 1004, 'msg': "需要管理员权限"})
    return wrapper


@csrf_exempt
@not_login_required
@require_http_methods(['POST'])
def user_register(request):
    data_json = json.loads(request.body)
    username = data_json['username']
    password1 = data_json['password1']
    password2 = data_json['password2']
    email = data_json.get('email')
    if not bool(re.match("^[A-Za-z0-9][A-Za-z0-9_]{2,20}$", str(username))):
        return JsonResponse({'errno': 1011, 'msg': "用户名不合法"})
    elif User.objects.filter(user_name=username).exists():
        return JsonResponse({'errno': 1012, 'msg': "用户名已存在"})
    elif password1 != password2:
        return JsonResponse({'errno': 1013, 'msg': "两次输入的密码不同"})
    elif not bool(re.match('^(?=.*\\d)(?=.*[a-zA-Z]).{6,20}$', str(password1))):
        return JsonResponse({'errno': 1014, 'msg': "密码不合法"})
    else:
        new_user = User.objects.create(user_name=username, user_password=password1, user_email=email)
        new_user.save()
        return JsonResponse({'errno': 0, 'msg': "注册成功", 'username': new_user.user_name})


@csrf_exempt
@not_login_required
@require_http_methods(['POST'])
def user_login(request):
    data_json = json.loads(request.body)
    username = data_json['username']
    password = data_json['password']
    if User.objects.filter(user_name=username).exists():
        user = User.objects.get(user_name=username)
        if user.user_password == password:
            request.session['id'] = user.user_id
            request.session['role'] = 'user'
            return JsonResponse({'errno': 0, 'msg': "登录成功", 'uid': user.user_id})
        else:
            return JsonResponse({'errno': 1022, 'msg': "密码错误"})
    else:
        return JsonResponse({'errno': 1021, 'msg': "用户不存在"})


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
    uid = request.session['id']
    user = User.objects.get(user_id=uid)
    user.delete()
    return JsonResponse({'errno': 0, 'msg': "注销成功"})


@csrf_exempt
@login_required
@require_http_methods(['GET'])
def check_profile(request):
    data_json = json.loads(request.body)
    uid = data_json['id']
    user = User.objects.get(user_id=uid)
    user_info = {"user_id": user.user_id, "user_name": user.user_name, "user_password": user.user_password,
                 "user_email": user.user_email, "user_status": user.user_status}
    return JsonResponse({'errno': 0, 'msg': '返回用户信息成功', 'user_info': user_info})


@csrf_exempt
@login_required
@require_http_methods(['POST'])
def change_profile(request):
    data_json = json.loads(request.body)
    uid = request.session.get('id')
    username = data_json['username']
    password1 = data_json['password1']
    password2 = data_json['password2']
    mail = data_json.get('email')
    if not bool(re.match("^[A-Za-z0-9][A-Za-z0-9_]{2,20}$", str(username))):
        return JsonResponse({'errno': 1071, 'msg': "用户名不合法"})
    elif User.objects.filter(user_id__ne=uid, user_name=username).exists():
        return JsonResponse({'errno': 1072, 'msg': "用户名已存在"})
    elif password1 != password2:
        return JsonResponse({'errno': 1073, 'msg': "两次输入的密码不同"})
    elif not re.match('^(?=.*\\d)(?=.*[a-zA-Z]).{6,20}$', str(password1)):
        return JsonResponse({'errno': 1074, 'msg': "密码不合法"})
    else:
        user = User.objects.get(user_id=uid)
        user.user_name = username
        user.user_password = password1
        user.user_mail = mail
        user.save()
        return JsonResponse({'errno': 0, 'msg': '修改用户信息成功'})


@csrf_exempt
@login_required
@require_http_methods(['GET'])
def check_created_questionnaires(request):
    uid = request.session['id']
    user = User.objects.get(user_id=uid)
    questionnaires = user.user_created_questionnaires.all()
    qn_info = []
    for qn_id in questionnaires:
        qn = Questionnaire.objects.get(qn_id=qn_id)
        qn_info.append(qn.to_json)
    return JsonResponse({'errno': 0, 'msg': '返回已创建问卷列表成功', 'qn_info': qn_info})


@csrf_exempt
@login_required
@require_http_methods(['GET'])
def check_filled_questionnaires(request):
    uid = request.session['id']
    user = User.objects.get(user_id=uid)
    questionnaires = user.user_filled_questionnaires.all()
    qn_info = []
    for qn_id in questionnaires:
        qn = Questionnaire.objects.get(qn_id=qn_id)
        qn_info.append(qn.to_json)
    return JsonResponse({'errno': 0, 'msg': '返回已填写问卷列表成功', 'qn_info': qn_info})


def send_simple_message(mail, code):
    return requests.post(
        "https://api.mailgun.net/v3/sandboxdf0686a9196242e6bc7cfd605a329a55.mailgun.org/messages",
        auth=("api", "key-768b5b09ca15e3c73881617406651be8"),
        data={"from": "Mailgun Sandbox <postmaster@sandboxdf0686a9196242e6bc7cfd605a329a55.mailgun.org>",
              "to": mail,
              "subject": "Code",
              "text": code})


@require_http_methods(['GET', 'PUT', 'DELETE', 'PATCH'])
def unsupported_request(request):
    return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})


@csrf_exempt
@not_login_required
@require_http_methods(['POST'])
def send_verification_code(request):
    data_json = json.loads(request.body)
    username = data_json['username']
    if User.objects.filter(user_name=username).exists():
        user = User.objects.get(user_name=username)
        email = user.user_email
        if email:
            code = randint(100000, 999999)
            response = send_simple_message(email, str(code))
            if response.status_code == 200:
                return JsonResponse({'errno': 0, 'msg': '邮件发送成功', 'code': code})
            return JsonResponse({'errno': 1012, 'msg': '邮箱发送失败'})
        return JsonResponse({'errno': 1014, 'msg': '邮箱不存在'})
    else:
        return JsonResponse({'errno': 1008, 'msg': "用户不存在"})


@csrf_exempt
@not_login_required
@require_http_methods(['POST'])
def reset_password(request):
    data_json = json.loads(request.body)
    username = data_json['username']
    password1 = data_json['password1']
    password2 = data_json['password2']
    if User.objects.filter(user_name=username).exists():
        user = User.objects.get(user_name=username)
        if password1 != password2:
            return JsonResponse({'errno': 1002, 'msg': "两次输入的密码不同"})
        elif not re.match('^(?=.*\\d)(?=.*[a-zA-Z]).{6,20}$', str(password1)):
            return JsonResponse({'errno': 1005, 'msg': "密码不合法"})
        else:
            user.password = password1
            user.save()
            return JsonResponse({'errno': 0, 'msg': "重置密码成功"})
    else:
        return JsonResponse({'errno': 1008, 'msg': "用户不存在"})





@csrf_exempt
@not_login_required
@require_http_methods(['POST'])
def admin_login(request):
    data_json = json.loads(request.body)
    adminname = data_json['adminname']
    password = data_json['password']
    if Admin.objects.filter(admin_name=adminname).exists():
        admin = Admin.objects.get(admin_name=adminname)
        if admin.admin_password == password:
            request.session['id'] = admin.admin_id
            request.session['role'] = 'admin'
            return JsonResponse({'errno': 0, 'msg': "管理员登录成功", 'adid': admin.admin_id})
        else:
            return JsonResponse({'errno': 1032, 'msg': "密码错误"})
    else:
        return JsonResponse({'errno': 1031, 'msg': "管理员账号不存在"})


@csrf_exempt
@admin_required
@require_http_methods(['GET'])
def check_profile_admin(request):
    data_json = json.loads(request.body)
    adid = data_json['id']
    admin = Admin.objects.get(admin_id=adid)
    admin_info = {"admin_id": admin.admin_id, "admin_name": admin.admin_name, "admin_password": admin.admin_password}
    return JsonResponse({'errno': 0, 'msg': '返回管理员信息成功', 'admin_info': admin_info})


@csrf_exempt
@admin_required
@require_http_methods(['POST'])
def change_profile_admin(request):
    data_json = json.loads(request.body)
    uid = data_json['id']
    password1 = data_json['password1']
    password2 = data_json['password2']
    mail = data_json.get('email', '')
    if not bool(re.match("^[A-Za-z0-9][A-Za-z0-9_]{2,20}$", str(username))):
        return JsonResponse({'errno': 1081, 'msg': "用户名不合法"})
    elif User.objects.filter(user_id__ne=uid, user_name=username).exists():
        return JsonResponse({'errno': 1082, 'msg': "用户名已存在"})
    elif password1 != password2:
        return JsonResponse({'errno': 1083, 'msg': "两次输入的密码不同"})
    elif not re.match('^(?=.*\\d)(?=.*[a-zA-Z]).{6,20}$', str(password1)):
        return JsonResponse({'errno': 1084, 'msg': "密码不合法"})
    else:
        user = User.objects.get(user_id=uid)
        user.user_name = username
        user.user_password = password1
        user.user_mail = mail
        user.save()
        return JsonResponse({'errno': 0, 'data': user, 'msg': '修改用户信息成功'})


@csrf_exempt
@login_required
@require_http_methods(['POST'])
def ban_user(request):
    id = request.session['id']
    user = User.objects.get(user_id=id)
    user.status = 'banned'
    user.save()
    return JsonResponse({'errno': 0, 'msg': "用户封禁成功"})


@csrf_exempt
@login_required
@require_http_methods(['POST'])
def un_ban_user(request):
    id = request.session['id']
    user = User.objects.get(user_id=id)
    user.status = 'free'
    user.save()
    return JsonResponse({'errno': 0, 'msg': "用户解封成功"})