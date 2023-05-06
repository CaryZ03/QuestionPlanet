from django.db.models import *
from user.models import *


class Answer(Model):
    a_id = IntegerField(primary_key=True)
    a_user = ForeignKey('user.User', on_delete=CASCADE, null=True)
    a_question = ForeignKey('Question', on_delete=CASCADE, null=True)
    a_createTime = DateTimeField(auto_now_add=True)
    a_content = TextField()
    a_score = IntegerField()
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
    q_title = TextField()
    q_description = TextField()
    q_option_count = IntegerField()
    q_options = JSONField()
    q_correct_answer = TextField()
    q_answers = ManyToManyField(Answer)


class AnswerSheet(Model):
    as_id = IntegerField(primary_key=True)
    as_user = ForeignKey('user.User', on_delete=CASCADE, null=True)
    as_questionnaire = ForeignKey('Questionnaire', on_delete=CASCADE, null=True)
    as_createTime = DateTimeField(auto_now_add=True)
    as_answers = ManyToManyField(Answer)
    as_score = IntegerField()


class Questionnaire(Model):
    qn_id = IntegerField(primary_key=True)
    qn_title = TextField()
    qn_description = TextField()
    qn_createTime = DateTimeField(auto_now_add=True)
    qn_endTime = DateTimeField(default=None)
    status_choices = (
        ('unpublished', "未发布"),
        ('published', "已发布"),
        ('closed', "已关闭")
    )
    qn_status = CharField(max_length=20, choices=status_choices, default='unpublished')
    qn_refillable = BooleanField(default=True)
    qn_questions = ManyToManyField(Question)
    qn_answers = ManyToManyField(AnswerSheet)




