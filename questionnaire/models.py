import json

from django.db.models import *


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
    q_mandatory = BooleanField(default=False)
    q_title = TextField(null=True)
    q_description = TextField(null=True)
    q_option_count = IntegerField(default=1)
    q_options = JSONField(null=True)
    q_correct_answer = TextField(null=True)
    q_score = DecimalField(max_digits=6, decimal_places=2, default=0.0, null=True)
    q_answers = ManyToManyField(Answer)

    def to_json(self):
        info = {
            "q_id": self.q_id,
            "q_questionnaire": self.q_questionnaire.qn_id,
            "q_position": self.q_position,
            "q_type": self.q_type,
            "q_mandatory": self.q_mandatory,
            "q_title": self.q_title,
            "q_description": self.q_description,
            "q_option_count": self.q_option_count,
            "q_options": self.q_options,
            "q_correct_answer": self.q_correct_answer,
            "q_score": str(self.q_score)
        }
        return json.dumps(info)


class AnswerSheet(Model):
    as_id = AutoField(primary_key=True)
    as_filler = ForeignKey('user.Filler', on_delete=CASCADE, null=True)
    as_questionnaire = ForeignKey('Questionnaire', on_delete=CASCADE, null=True)
    as_create_time = DateTimeField(auto_now_add=True)
    as_answers = ManyToManyField(Answer)
    as_score = IntegerField(default=0)
    as_temporary_save = JSONField(default=None, null=True)
    as_submitted = BooleanField(default=False)


class Questionnaire(Model):
    qn_id = AutoField(primary_key=True)
    qn_title = TextField(null=True)
    qn_description = TextField(null=True)
    qn_types = (
        ('normal', "普通问卷"),
        ('test', "考试问卷"),
        ('vote', "投票问卷"),
        ('application', "申请问卷")
    )
    qn_type = CharField(max_length=20, choices=qn_types, default='normal')
    qn_creator = ForeignKey('user.User', on_delete=SET_NULL, null=True, related_name='creator')
    qn_create_time = DateTimeField(auto_now_add=True)
    qn_publish_time = DateTimeField(default=None, null=True)
    qn_end_time = DateTimeField(default=None, null=True)
    qn_status_choices = (
        ('unpublished', "未发布"),
        ('published', "已发布"),
        ('closed', "已关闭"),
        ('banned', "已封禁"),
        ('deleted', "已删除")
    )
    qn_status = CharField(max_length=20, choices=qn_status_choices, default='unpublished')
    qn_refillable = BooleanField(default=True)
    qn_questions = ManyToManyField(Question)
    qn_answersheets = ManyToManyField(AnswerSheet)
    qn_allowed_users = ManyToManyField('user.User', related_name='allowed_users')
    qn_data_json = JSONField(default=None, null=True)

    def to_json(self):
        info = {
            "qn_id": self.qn_id,
            "qn_title": self.qn_title,
            "qn_description": self.qn_description,
            "qn_type": self.qn_type,
            "qn_create_time": str(self.qn_create_time),
            "qn_publish_time": str(self.qn_publish_time),
            "qn_end_time": str(self.qn_end_time),
            "qn_status": self.qn_status,
            "qn_refillable": self.qn_refillable,
            "qn_answersheet_count": self.qn_answersheets.count()
        }
        return json.dumps(info)
