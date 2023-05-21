import json

from django.db.models import *
from user.models import *


class Answer(Model):
    a_id = IntegerField(primary_key=True)
    a_answersheet = ForeignKey('Answersheet', on_delete=CASCADE, null=True)
    a_question = ForeignKey('Question', on_delete=CASCADE, null=True)
    a_content = TextField()
    a_score = DecimalField(max_digits=6, decimal_places=2, default=0)
    a_comment = TextField()


class Question(Model):
    q_id = IntegerField(primary_key=True)
    q_questionnaire = ForeignKey('Questionnaire', on_delete=CASCADE, null=True)
    question_types = (
        ('single', "单选"),
        ('multiple', "多选"),
        ('judge', "判断"),
        ('fill', "填空"),
        ('essay', "解答"),
        ('grade', "打分")
    )
    q_type = CharField(max_length=20, choices=question_types, default='single')
    q_manditory = BooleanField(default=False)
    q_title = TextField()
    q_description = TextField()
    q_option_count = IntegerField()
    q_options = JSONField()
    q_correct_answer = TextField()
    q_score = DecimalField(max_digits=6, decimal_places=2, default=0.0)
    q_answers = ManyToManyField(Answer)


class AnswerSheet(Model):
    as_id = IntegerField(primary_key=True)
    as_filler = ForeignKey('user.Filler', on_delete=CASCADE, null=True)
    as_questionnaire = ForeignKey('Questionnaire', on_delete=CASCADE, null=True)
    as_createTime = DateTimeField(auto_now_add=True)
    as_answers = ManyToManyField(Answer)
    as_score = IntegerField()
    as_temporary_save = JSONField(default=None)
    as_submitted = BooleanField(default=False)


class Questionnaire(Model):
    qn_id = IntegerField(primary_key=True)
    qn_title = TextField()
    qn_description = TextField()
    qn_creator = ForeignKey('user.User', on_delete=SET_NULL, null=True)
    qn_createTime = DateTimeField(auto_now_add=True)
    qn_endTime = DateTimeField(default=None)
    status_choices = (
        ('unpublished', "未发布"),
        ('published', "已发布"),
        ('closed', "已关闭"),
        ('banned', "已封禁")
    )
    qn_status = CharField(max_length=20, choices=status_choices, default='unpublished')
    qn_refillable = BooleanField(default=True)
    qn_questions = ManyToManyField(Question)
    qn_answersheets = ManyToManyField(AnswerSheet)

    def to_json(self):
        info = {
            "qn_id": self.qn_id,
            "qn_title": self.qn_title,
            "qn_description": self.qn_description,
            "qn_createTime": self.qn_createTime,
            "qn_endTime": self.qn_endTime,
            "qn_status": self.qn_status,
            "qn_refillable": self.qn_refillable
        }
        return json.dumps(info)
