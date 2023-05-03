from django.db.models import *
from questionnaire.models import *


class Visitor(Model):
    visitor_id = IntegerField(primary_key=True)


class User(Model):
    user_id = IntegerField(primary_key=True)
    user_name = CharField(max_length=100)
    user_password = CharField(max_length=20)
    status_choices = (
        ('free', "未封禁"),
        ('banned', "封禁")
    )
    user_status = CharField(max_length=10, choices=status_choices, default='free')
    user_created_questionnaires = ManyToManyField(Questionnaire)
    user_filled_questionnaires = ManyToManyField(Questionnaire)


class Admin(Model):
    admin_id = IntegerField(primary_key=True)
    admin_name = CharField(max_length=100)
    admin_password = CharField(max_length=20)







