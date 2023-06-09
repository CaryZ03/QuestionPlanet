import re
from datetime import datetime

from django.core.management.utils import get_random_secret_key
from django.db.models import Q
from django.http import JsonResponse
from django.utils.timezone import now
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.http.response import JsonResponse
import json
from user.models import User, Admin, Filler, UserToken
from questionnaire.models import Questionnaire, AnswerSheet, Question, Answer
from user.views import login_required, admin_required, create_token


def questionnaire_exists(view_func):
    def wrapper(request, *args, **kwargs):
        qn_id = kwargs.get('qn_id')
        if qn_id is None:
            qn_id = json.loads(request.body).get('qn_id')
        if not Questionnaire.objects.filter(qn_id=qn_id).exists():
            return JsonResponse({'errno': 2001, 'qn_id': qn_id, 'msg': "问卷不存在"})
        else:
            return view_func(request, *args, **kwargs)
    return wrapper


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        # 如果存在多个IP地址，取第一个
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


# path('fill_questionnaire', fill_questionnaire),
@csrf_exempt
@require_http_methods(['POST'])
def fill_questionnaire(request, qn_key):
    token_key = request.headers.get('Authorization')
    if token_key:
        token = UserToken.objects.get(key=token_key)
        filler = token.filler
    else:
        filler_ip = get_client_ip(request)
        if Filler.objects.filter(filler_ip=filler_ip).exists():
            filler = Filler.objects.filter(filler_ip=filler_ip).last()
        else:
            filler = Filler.objects.create(filler_ip=filler_ip)
            filler.save()
        token_key = create_token(filler.filler_id, False)
    if not Questionnaire.objects.filter(qn_key=qn_key).exists():
        return JsonResponse({'errno': 2001, 'msg': "问卷不存在"})
    questionnaire = Questionnaire.objects.get(qn_key=qn_key)
    if questionnaire.qn_status != 'published':
        return JsonResponse({'errno': 2011, 'msg': "问卷未发布"})
    if AnswerSheet.objects.filter(as_questionnaire=questionnaire, as_filler=filler).exists():
        answer_sheet = AnswerSheet.objects.get(as_questionnaire=questionnaire, as_filler=filler)
    else:
        answer_sheet = AnswerSheet.objects.create(as_questionnaire=questionnaire, as_filler=filler)
        answer_sheet.save()
        if filler.filler_is_user:
            filler.filler_user.user_filled_questionnaires.add(questionnaire)
            filler.filler_user.save()
    temp_save = answer_sheet.as_temporary_save
    return JsonResponse({'errno': 0, 'msg': "答卷创建成功", 'as_id': answer_sheet.as_id, 'temp_save': temp_save, 'token_key': token_key})


# path('save_answers', save_answers),
# path('submit_answers', submit_answers),

@csrf_exempt
@questionnaire_exists
@require_http_methods(['POST'])
def save_answers(request):
    data_json = json.loads(request.body)
    as_id = data_json.get('as_id')
    if not AnswerSheet.objects.filter(as_id=as_id).exists():
        return JsonResponse({'code': 2021, 'message': '答卷不存在'})
    answer_sheet = AnswerSheet.objects.get(as_id=as_id)
    answer_data = data_json.get('answer_data')
    if answer_data is not None:
        answer_sheet.as_temporary_save = answer_data
        answer_sheet.save()
        return JsonResponse({'errno': 0, 'msg': "答卷保存成功"})
    else:
        answer_sheet.delete()
        return JsonResponse({'errno': 0, 'msg': "答卷删除成功"})


@csrf_exempt
@questionnaire_exists
@require_http_methods(['POST'])
def submit_answers(request):
    # 获取请求参数
    data_json = json.loads(request.body)
    as_id = data_json.get('as_id')
    answer_data = data_json.get('answer_data')
    if not AnswerSheet.objects.filter(as_id=as_id).exists():
        return JsonResponse({'code': 2031, 'message': '答卷不存在'})
    answer_sheet = AnswerSheet.objects.get(as_id=as_id)
    answer_sheet.as_answers.all().delete()
    # 解析答案数据，创建答案对象
    answer_list = json.loads(answer_data)
    for a_data in answer_list:
        q_id = a_data.get('q_id')
        a_content = a_data.get('a_content')
        question = Question.objects.get(q_id=q_id)
        answer = Answer.objects.create(
            a_answersheet=answer_sheet,
            a_question=question,
            a_content=a_content
        )
        if question.q_correct_answer == a_content:
            answer.a_score = question.q_score

        answer.save()
        question.q_answers.add(answer)
        question.save()
        answer_sheet.as_answers.add(answer)
        answer_sheet.as_score += answer.a_score  # 计算得分

    answer_sheet.as_temporary_save = answer_data
    answer_sheet.as_submitted = True
    answer_sheet.as_questionnaire.qn_answersheets.add(answer_sheet)
    answer_sheet.save()
    return JsonResponse({'code': 0, 'message': '答卷提交成功'})


# path('refill_questionnaire', refill_questionnaire),
# # 编辑问卷


@csrf_exempt
@login_required
@require_http_methods(['POST'])
def create_questionnaire(request, user):
    qn = Questionnaire.objects.create(qn_creator=user, qn_key=get_random_secret_key())
    qn.save()
    user.user_created_questionnaires.add(qn)
    user.save()
    # 返回问卷创建成功的响应
    return JsonResponse({'errno': 0, 'message': '问卷创建成功', 'qn_id': qn.qn_id})


@csrf_exempt
@login_required
@questionnaire_exists
@require_http_methods(['POST'])
def save_questionnaire(request, user):
    # 从请求中获取问卷信息和问题数据
    data_json = json.loads(request.body)
    qn_id = data_json.get('qn_id')
    qn_title = data_json.get('qn_title')
    qn_description = data_json.get('qn_description')
    qn_type = data_json.get('qn_type')
    qn_end_time = data_json.get('qn_end_time')
    qn_refillable = data_json.get('qn_refillable')
    question_list = data_json.get('question_list')

    qn = Questionnaire.objects.get(qn_id=qn_id)
    qn.qn_title = qn_title
    qn.qn_description = qn_description
    qn.qn_type = qn_type
    qn.qn_end_time = datetime.strptime(qn_end_time, '%Y-%m-%d %H:%M:%S')
    qn.qn_refillable = qn_refillable

    qn.qn_answersheets.all().delete()
    qn.qn_questions.all().delete()

    qn.qn_data_json = data_json

    # 创建问题并加入问卷中
    for i in range(len(question_list)):
        q_data = question_list[i]
        question = Question.objects.create(
            q_questionnaire=qn,
            q_position=i,
            q_type=q_data.get('q_type'),
            q_mandatory=q_data.get('q_mandatory'),
            q_title=q_data.get('q_title'),
            q_description=q_data.get('q_description'),
            q_option_count=q_data.get('q_option_count'),
            q_options=json.dumps(q_data.get('q_options')),
            q_correct_answer=q_data.get('q_correct_answer'),
            q_score=q_data.get('q_score'),
        )
        question.save()
        qn.qn_questions.add(question)
    qn.save()
    return JsonResponse({'code': 0, 'message': '问卷保存成功'})


@csrf_exempt
@login_required
@questionnaire_exists
@require_http_methods(['POST'])
def copy_questionnaire(request, user, qn_id):
    new_qn = Questionnaire.objects.create()
    new_qn.qn_creator = user
    user.user_created_questionnaires.add(new_qn)
    user.save()

    old_qn = Questionnaire.objects.get(qn_id=qn_id)
    qn_title = old_qn.qn_title
    qn_description = old_qn.qn_description
    qn_end_time = old_qn.qn_end_time
    qn_refillable = old_qn.qn_refillable
    question_list = old_qn.qn_questions.all()
    allowed_users = old_qn.qn_allowed_users.all()

    new_qn.qn_title = qn_title
    new_qn.qn_description = qn_description
    new_qn.qn_end_time = qn_end_time
    new_qn.qn_refillable = qn_refillable
    new_qn.qn_allowed_users.set(allowed_users)

    new_qn.qn_data_json = old_qn.qn_data_json

    # 创建问题并加入问卷中
    for q_data in question_list:
        question = Question.objects.create(
            q_questionnaire=new_qn,
            q_position=q_data.q_position,
            q_type=q_data.q_type,
            q_mandatory=q_data.q_mandatory,
            q_title=q_data.q_title,
            q_description=q_data.q_description,
            q_option_count=q_data.q_option_count,
            q_options=q_data.q_options,
            q_correct_answer=q_data.q_correct_answer,
            q_score=q_data.q_score,
        )
        question.save()
        new_qn.qn_questions.add(question)
    new_qn.save()
    return JsonResponse({'code': 0, 'message': '问卷复制成功', 'qn_id': new_qn.qn_id})


@csrf_exempt
@require_http_methods(['GET'])
def check_questionnaire(request, qn_id):
    if not Questionnaire.objects.filter(qn_id=qn_id).exists():
        return JsonResponse({'code': 2061, 'message': '问卷不存在'})
    questionnaire = Questionnaire.objects.get(qn_id=qn_id)
    question_list = []
    for q in questionnaire.qn_questions.all():
        question_list.append(q.to_json())
    return JsonResponse({'errno': 0, 'msg': '问卷查看成功', 'qn_info': questionnaire.to_json(), 'question_list': question_list})


@csrf_exempt
@login_required
@questionnaire_exists
@require_http_methods(['POST'])
def delete_questionnaire(request, user):
    qn_id = json.loads(request.body).get('qn_id')
    qn = Questionnaire.objects.get(qn_id=qn_id)
    qn.delete()
    return JsonResponse({'errno': 0, 'msg': "问卷删除成功"})


@csrf_exempt
@login_required
@questionnaire_exists
@require_http_methods(['POST'])
def publish_questionnaire(request, user, qn_id):
    qn = Questionnaire.objects.get(qn_id=qn_id)
    qn.qn_status = 'published'
    qn.save()
    qn_key = qn.qn_key
    return JsonResponse({'errno': 0, 'msg': "问卷发布成功", 'key': qn_key})


@csrf_exempt
@login_required
@questionnaire_exists
@require_http_methods(['POST'])
def close_questionnaire(request, user, qn_id):
    qn = Questionnaire.objects.get(qn_id=qn_id)
    qn.qn_status = 'closed'
    an.save()
    return JsonResponse({'errno': 0, 'msg': "问卷关闭成功"})

@csrf_exempt
@login_required
@questionnaire_exists
@require_http_methods(['POST'])
def change_questionnaire_status(request, user):
    data_json = json.loads(request.body)
    qn_id = data_json.get('qn_id')
    status = data_json.get('status')
    qn = Questionnaire.objects.get(qn_id=qn_id)
    qn.qn_status = status
    qn.save()
    if status == 'published':
        qn.qn_publish_time = now()
    return JsonResponse({'errno': 0, 'msg': "问卷状态更改成功"})


# # 管理员操作
# path('ban_questionnaire', ban_questionnaire),
