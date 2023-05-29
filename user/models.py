import json

from django.db.models import *
from questionnaire.models import Questionnaire


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

    def to_json(self):
        info = {
            "user_id": self.user_id,
            "user_name": self.user_name,
            "user_password": self.user_password,
            "user_signature": self.user_signature,
            "user_email": self.user_email,
            "user_tel": self.user_tel,
            "user_status": self.user_status
        }
        return json.dumps(info)


class Admin(Model):
    admin_id = AutoField(primary_key=True)
    admin_name = CharField(max_length=100)
    admin_password = CharField(max_length=20)

    def to_json(self):
        info = {
            "admin_id": self.admin_id,
            "admin_name": self.admin_name,
            "admin_password": self.admin_password
        }
        return json.dumps(info)


class UserToken(Model):
    key = CharField(max_length=200, unique=True)
    is_admin = BooleanField(default=False)
    user = ForeignKey('User', on_delete=CASCADE, null=True)
    admin = ForeignKey('Admin', on_delete=CASCADE, null=True)
    expire_time = DateTimeField()
