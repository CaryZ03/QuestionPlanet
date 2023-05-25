import json

from django.db.models import *
from user.models import *


class Answer(Model):
    a_id = AutoField(primary_key=True)
    a_answersheet = ForeignKey('Answersheet', on_delete=CASCADE, null=True)
    a_question = ForeignKey('Question', on_delete=CASCADE, null=True)
    a_content = TextField(null=True)
    a_score = DecimalField(max_digits=6, decimal_places=2, default=0)
    a_comment = TextField(null=True)

    def to_json(self):
        info = {
            "a_id": self.a_id,
            "a_answersheet": self.a_answersheet,
            "a_question": self.a_question,
            "a_content": self.a_content,
            "a_score": self.a_score,
            "a_comment": self.a_comment
        }
        return json.dumps(info)


class Question(Model):
    q_id = AutoField(primary_key=True)
    q_questionnaire = ForeignKey('Questionnaire', on_delete=CASCADE, null=True)
    q_position = IntegerField(default=0)
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
    q_title = TextField(null=True)
    q_description = TextField(null=True)
    q_option_count = IntegerField(default=1)
    q_options = JSONField(null=True)
    q_correct_answer = TextField(null=True)
    q_score = DecimalField(max_digits=6, decimal_places=2, default=0.0)
    q_answers = ManyToManyField(Answer)


class AnswerSheet(Model):
    as_id = AutoField(primary_key=True)
    as_filler = ForeignKey('user.Filler', on_delete=CASCADE, null=True)
    as_questionnaire = ForeignKey('Questionnaire', on_delete=CASCADE, null=True)
    as_createTime = DateTimeField(auto_now_add=True)
    as_answers = ManyToManyField(Answer)
    as_score = IntegerField(default=0)
    as_temporary_save = JSONField(default=None, null=True)
    as_submitted = BooleanField(default=False)


class Questionnaire(Model):
    qn_id = AutoField(primary_key=True)
    qn_title = TextField(null=True)
    qn_description = TextField(null=True)
    qn_creator = ForeignKey('user.User', on_delete=SET_NULL, null=True)
    qn_createTime = DateTimeField(auto_now_add=True)
    qn_endTime = DateTimeField(default=None, null=True)
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
    qn_data_json = JSONField(default=None, null=True)

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
