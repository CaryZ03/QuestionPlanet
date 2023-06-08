import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'QuestionPlanet.settings')
django.setup()
import json
from django.test import Client, TransactionTestCase
from django.urls import reverse
from user.models import User
from django.core.management import call_command


class RegisterTestCase(TransactionTestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('user:user_register')
        User.objects.all().delete()

    def tearDown(self):
        # 注销当前用户
        self.client.post(reverse('user:logout'))
        # 删除所有表
        call_command('flush', '--noinput')

    def test_register_success(self):
        user_data = {
            'username': 'AAA_',
            'password1': 'aa123456',
            'password2': 'aa123456',
        }
        response = self.client.post(self.url, data=json.dumps(user_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'errno': 0, 'msg': '注册成功', 'uid': 1})

    def test_username_invalid_characters(self):
        invalid_usernames = ['A', '1111111111111111111111111111110', 'A=*——', '_123']
        for username in invalid_usernames:
            with self.subTest(username=username):
                user_data = {
                    'username': username,
                    'password1': 'aa123456',
                    'password2': 'aa123456',
                }
                response = self.client.post(self.url, data=json.dumps(user_data), content_type='application/json')
                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.json(), {'errno': 1011, 'msg': "用户名不合法"})

    def test_username_duplicate(self):
        user_data1 = {
            'username': 'AAA_',
            'password1': 'aa123456',
            'password2': 'aa123456',
        }
        user_data2 = {
            'username': 'AAA_',
            'password1': 'aa123456',
            'password2': 'aa123456',
        }

        # 先注册第一个用户
        self.client.post(self.url, data=json.dumps(user_data1), content_type='application/json')

        # 再尝试注册另一个使用相同用户名的用户
        response = self.client.post(self.url, data=json.dumps(user_data2), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'errno': 1012, 'msg': "用户名已存在"})

    def test_confirm_password_not_match(self):
        user_data = {
            'username': 'abc',
            'password1': 'aa123456',
            'password2': 'aa12345',  # 密码不匹配
        }
        response = self.client.post(self.url, data=json.dumps(user_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'errno': 1013, 'msg': "两次输入的密码不同"})

    def test_password_invalid_characters(self):
        invalid_passwords = ['11a', '11111111111111111111a', '123456', 'aaaaaa']
        for password in invalid_passwords:
            with self.subTest(password=password):
                user_data = {
                    'username': 'abc',
                    'password1': password,
                    'password2': password,
                }
                response = self.client.post(self.url, data=json.dumps(user_data), content_type='application/json')
                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.json(), {'errno': 1014, 'msg': "密码不合法"})
