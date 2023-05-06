from django.db.models import *
from questionnaire.models import *


class Visitor(Model):
    visitor_id = IntegerField(primary_key=True)
    visitor_ip = CharField(max_length=30)


class User(Model):
    user_id = IntegerField(primary_key=True)
    user_name = CharField(max_length=100)
    user_password = CharField(max_length=20)
    status_choices = (
        ('free', "未封禁"),
        ('banned', "封禁")
    )
    user_status = CharField(max_length=10, choices=status_choices, default='free')
    user_created_questionnaires = ManyToManyField(Questionnaire, related_name='created_by_users')
    user_filled_questionnaires = ManyToManyField(Questionnaire, related_name='filled_by_users')


class Admin(Model):
    admin_id = IntegerField(primary_key=True)
    admin_name = CharField(max_length=100)
    admin_password = CharField(max_length=20)







