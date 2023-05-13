from django.shortcuts import render
import re
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.http.response import JsonResponse
from django.core import serializers
import json
from user.models import User, Admin
from questionnaire.models import *
from random import randint
import requests
from django.core.cache import cache


def login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.session is not None:
            return view_func(request, *args, **kwargs)
        else:
            return JsonResponse({'errno': 1002, 'msg': "未登录"})
    return wrapper


def not_login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.session is None:
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
    email = data_json.get('email', ' ')
    if not bool(re.match("^[A-Za-z0-9][A-Za-z0-9_]{2,20}$", str(username))):
        return JsonResponse({'errno': 1003, 'msg': "用户名不合法"})
    elif User.objects.filter(user_name=username).exists():
        return JsonResponse({'errno': 1004, 'msg': "用户名已存在"})
    elif password1 != password2:
        return JsonResponse({'errno': 1002, 'msg': "两次输入的密码不同"})
    elif not bool(re.match('^(?=.*\\d)(?=.*[a-zA-Z]).{6,20}$', str(password1))):
        return JsonResponse({'errno': 1005, 'msg': "密码不合法"})
    else:
        new_user = User.objects.create(user_name=username, user_password=password1, user_email=email)
        return JsonResponse({'errno': 0, 'msg': "注册成功"})


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
            return JsonResponse({'errno': 0, 'data': user, 'msg': "登录成功"})
        else:
            return JsonResponse({'errno': 1007, 'msg': "密码错误"})
    else:
        return JsonResponse({'errno': 1008, 'msg': "用户不存在"})


@csrf_exempt
@not_login_required
@require_http_methods(['POST'])
def admin_login(request):
    data_json = json.loads(request.body)
    adid = data_json['id']
    password = data_json['password']
    if Admin.objects.filter(admin_id=adid).exists():
        admin = Admin.objects.get(admin_id=adid)
        if admin.admin_password == password:
            request.session['id'] = adid
            request.session['role'] = 'admin'
            return JsonResponse({'errno': 0, 'data': admin, 'msg': "登录成功"})
        else:
            return JsonResponse({'errno': 1007, 'msg': "密码错误"})
    else:
        return JsonResponse({'errno': 1009, 'msg': "管理员账号不存在"})


@csrf_exempt
@login_required
@require_http_methods(['POST'])
def logout(request):
    request.session.flush()
    return JsonResponse({'errno': 0, 'msg': "登出成功"})


@csrf_exempt
@login_required
@require_http_methods(['GET'])
def check_profile(request):
    data_json = json.loads(request.body)
    uid = data_json['id']
    user = User.objects.get(user_id=uid)
    return JsonResponse({'error': 0, 'data': user, 'msg': '返回用户信息成功'})


@csrf_exempt
@admin_required
@require_http_methods(['GET'])
def check_profile_admin(request):
    data_json = json.loads(request.body)
    adid = data_json['id']
    admin = Admin.objects.get(admin_id=adid)
    return JsonResponse({'error': 0, 'data': admin, 'msg': '返回管理员信息成功'})


@csrf_exempt
@login_required
@require_http_methods(['POST'])
def change_profile(request):
    data_json = json.loads(request.body)
    id = data_json['id']
    username = data_json['username']
    password1 = data_json['password1']
    password2 = data_json['password2']
    mail = data_json.get('email', '')
    if not bool(re.match("^[A-Za-z0-9][A-Za-z0-9_]{2,20}*$", str(username))):
        return JsonResponse({'errno': 1003, 'msg': "用户名不合法"})
    elif User.objects.filter(user_id!=id, user_name=username).exists():
        return JsonResponse({'errno': 1004, 'msg': "用户名已存在"})
    elif password1 != password2:
        return JsonResponse({'errno': 1002, 'msg': "两次输入的密码不同"})
    elif not re.match('^(?=.*\\d)(?=.*[a-zA-Z]).{6,20}$', str(password1)):
        return JsonResponse({'errno': 1005, 'msg': "密码不合法"})
    else:
        user = User.objects.get(id=id)
        user.user_name = username
        user.user_password = password1
        user.user_mail = mail
        user.save()
        return JsonResponse({'error': 0, 'data': user, 'msg': '修改用户信息成功'})


@csrf_exempt
@admin_required
@require_http_methods(['POST'])
def change_profile_admin(request):
    data_json = json.loads(request.body)
    id = data_json['id']
    password1 = data_json['password1']
    password2 = data_json['password2']
    if request.session.get('id') == id:
        if password1 != password2:
            return JsonResponse({'errno': 1002, 'msg': "两次输入的密码不同"})
        elif not re.match('^(?=.*\\d)(?=.*[a-zA-Z]).{6,20}$', str(password1)):
            return JsonResponse({'errno': 1005, 'msg': "密码不合法"})
        else:
            admin = Admin.objects.get(admin_id=id)
            admin.password = password1
            return JsonResponse({'error': 0, 'data': Admin, 'msg': '修改用户信息成功'})
    else:
        return JsonResponse({'errno': 1011, 'msg': "该管理员未登录"})


@csrf_exempt
@login_required
@require_http_methods(['GET'])
def check_created_questionnaires(request):
    data_json = json.loads(request.body)
    id = data_json['id']
    user = User.objects.get(id=id)
    return JsonResponse({'error': 0, 'data': user, 'msg': '返回用户信息成功'})


@csrf_exempt
@login_required
@require_http_methods(['GET'])
def check_filled_questionnaires(request):
    data_json = json.loads(request.body)
    id = data_json['id']
    user = User.objects.get(id=id)
    return JsonResponse({'error': 0, 'data': user, 'msg': '返回用户信息成功'})


def send_simple_message(mail, code):
    return requests.post(
        "https://api.mailgun.net/v3/sandboxdf0686a9196242e6bc7cfd605a329a55.mailgun.org/messages",
        auth=("api", "8598ba9cde175f797c60edb63230e8a3-102c75d8-ae039287"),
        data={"from": "Mailgun Sandbox <postmaster@sandboxdf0686a9196242e6bc7cfd605a329a55.mailgun.org>",
              "to": mail,
              "subject": "Code",
              "text": code})


@require_http_methods(['GET', 'PUT', 'DELETE', 'PATCH'])
def unsupported_request(request):
    return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})



#
# @csrf_exempt
# @require_http_methods(['POST'])
# def update_pass_user_step1(request):
#     if request.session == None:
#         data_json = json.loads(request.body)
#         username = data_json['username']
#         if User.objects.filter(username=username).exists() == True:
#             user = User.objects.get(username=username)
#             mail = user.mail
#             if mail:
#                 code = randint(100000, 999999)
#                 cache.set(mail, str(code), 300)
#                 response = send_simple_message(mail, str(code))
#                 if response.status_code == 200:
#                     return JsonResponse({'errno': 200, 'msg': '邮件发送成功'})
#                 return JsonResponse({'errno': 1012, 'msg': '邮箱发送失败'})
#             return JsonResponse({'errno': 1014, 'msg': '邮箱不存在'})
#         else:
#             return JsonResponse({'errno': 1008, 'msg': "用户不存在"})
#     else:
#         return JsonResponse({'errno': 1006, 'msg': "已有用户登录"})
#
#
# @csrf_exempt
# @require_http_methods(['POST'])
# def update_pass_user_step2(request):
#     data_json = json.loads(request.body)
#     username = data_json['username']
#     verification_code = data_json['verification_code']
#     if User.objects.filter(username=username).exists() == True:
#         user = User.objects.get(username=username)
#         mail = user.mail
#         if verification_code:
#             code = cache.get(mail)
#         if code and code == verification_code:
#             return JsonResponse({'errno': 0, 'msg': '验证成功'})
#         else:
#             return JsonResponse({'error': 1013, 'msg': '验证码错误'})
#     else:
#         return JsonResponse({'errno': 1008, 'msg': "用户不存在"})
#
#
# @csrf_exempt
# @require_http_methods(['POST'])
# def update_pass_user_step3(request):
#     data_json = json.loads(request.body)
#     username = data_json['username']
#     password1 = data_json['password1']
#     password2 = data_json['password2']
#     if User.objects.filter(username=username).exists() == True:
#         user = User.objects.get(username=username)
#         if password1 != password2:
#             return JsonResponse({'errno': 1002, 'msg': "两次输入的密码不同"})
#         elif not re.match('^(?=.*\\d)(?=.*[a-zA-Z]).{6,20}$', str(password1)):
#             return JsonResponse({'errno': 1005, 'msg': "密码不合法"})
#         else:
#             user.password = password1
#             return JsonResponse({'errno': 0, 'msg': "重置密码成功"})
#     else:
#         return JsonResponse({'errno': 1008, 'msg': "用户不存在"})
#
#
# @csrf_exempt
# @require_http_methods(['GET'])
# def show_ticket(request):
#     data_json = json.loads(request.body)
#     id = data_json['id']
#     method = data_json['method']
#     if request.session != id:
#         if method == 0:
#             if Ticket.objects.filter(userid=id, status='doing').exists() == True:
#                 tickets = Ticket.objects.filter(userid=id, status='doing')
#                 return JsonResponse({'error': 0, 'data': tickets, 'msg': '查询机票成功'})
#             else:
#                 return JsonResponse({'error': 1015, 'data': tickets, 'msg': '查询机票为空'})
#         if method == 1:
#             if Ticket.objects.filter(userid=id, status='end').exists() == True:
#                 tickets = Ticket.objects.filter(userid=id, status='end')
#                 return JsonResponse({'error': 0, 'data': tickets, 'msg': '查询机票成功'})
#             else:
#                 return JsonResponse({'error': 1015, 'data': tickets, 'msg': '查询机票为空'})
#         if method == 2:
#             if Ticket.objects.filter(userid=id, status='false').exists() == True:
#                 tickets = Ticket.objects.filter(userid=id, status='false')
#                 return JsonResponse({'error': 0, 'data': tickets, 'msg': '查询机票成功'})
#             else:
#                 return JsonResponse({'error': 1015, 'data': tickets, 'msg': '查询机票为空'})
#         else:
#             return JsonResponse({'error': 1016, 'data': tickets, 'msg': 'method 不合法'})
#     else:
#         return JsonResponse({'errno': 1011, 'msg': "该用户未登录"})
