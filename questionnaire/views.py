import re
from datetime import datetime

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.http.response import JsonResponse
import json
from user.models import User, Admin, Visitor
from questionnaire.models import Questionnaire, AnswerSheet, Question, Answer
from user.views import login_required, not_login_required, admin_required


def questionnaire_exists(view_func):
    def wrapper(request, *args, **kwargs):
        qnid = request.body.get('qnid')
        if not Questionnaire.objects.filter(qn_id=qnid).exists():
            return JsonResponse({'errno': 1005, 'msg': "问卷不存在"})
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
@questionnaire_exists
@require_http_methods(['POST'])
def fill_questionnaire(request):
    qn_id = request.POST.get('qn_id')
    uid = request.session.get('id')
    if not uid:
        filler_ip = get_client_ip(request)
        if User.objects.filter(user_ip=filler_ip).exists():
            filler = User.objects.get(user_ip=filler_ip)
        elif Visitor.objects.filter(visitor_ip=filler_ip).exists():
            filler = Visitor.objects.get(visisitor_ip=filler_ip)
        else:
            filler = Visitor.objects.create(visisitor_ip=filler_ip)
    else:
        filler = User.objects.get(user_id=uid)
    new_as = AnswerSheet.objects.create(as_questionnaire=qn_id)
    if filler is User:
        new_as.as_is_user = True
        new_as.as_user = filler
    else:
        new_as.as_is_user = False
        new_as.as_visitor = filler
    new_as.save()
    return JsonResponse({'errno': 0, 'msg': "答卷创建成功", 'as_id': new_as.as_id})


# path('save_answers', save_answers),
# path('submit_answers', submit_answers),

@csrf_exempt
@questionnaire_exists
@require_http_methods(['POST'])
def save_answers(request):
    answer_sheet = request.POST.get('as_id')
    answer_data = request.POST.get('answer_data')
    answer_sheet.as_temporary_save = answer_data
    answer_sheet.save()
    return JsonResponse({'errno': 0, 'msg': "答卷保存成功"})


@csrf_exempt
@questionnaire_exists
@require_http_methods(['POST'])
def submit_answers(request):
        # 获取请求参数
        answer_sheet = request.POST.get('as_id')
        answer_data = request.POST.get('answer_data')

        # 解析答案数据，创建答案对象
        answer_list = json.loads(answer_data)
        for q_id, a_content in answer_list:
            answer = Answer.objects.create(
                a_answersheet=answer_sheet,
                a_question=q_id,
                a_content=a_content
            )
            question = Question.objects.get(q_id=q_id)
            if question.q_correct_answer == a_content:
                answer.a_score = question.q_score

            answer.save()
            answer_sheet.as_answers.add(answer)
            answer_sheet.as_score += answer.a_score # 计算得分

        answer_sheet.save()
        return JsonResponse({'code': 0, 'message': 'success.'})


# path('refill_questionnaire', refill_questionnaire),
# # 编辑问卷


@csrf_exempt
@login_required
@require_http_methods(['POST'])
def create_questionnaire(request):
    qn = Questionnaire.objects.create()
    qn.save()
    # 返回问卷创建成功的响应
    return JsonResponse({'errno': 0, 'message': '问卷创建成功', 'qn_id': qn.qn_id})


@csrf_exempt
@login_required
@questionnaire_exists
@require_http_methods(['POST'])
def save_questionnaire(request):
    # 从请求中获取问卷信息和问题数据
    qn_id = request.POST.get('qn_id')
    qn_title = request.POST.get('qn_title')
    qn_description = request.POST.get('qn_description')
    qn_end_time = request.POST.get('qn_end_time')
    qn_refillable = request.POST.get('qn_refillable')
    question_data = request.POST.get('question_data')

    # 创建问卷
    qn = Questionnaire.objects.get(qn_id=qn_id)
    qn.qn_title = qn_title
    qn.qn_description = qn_description
    qn.qn_createTime = datetime.now()
    qn.qn_endTime = datetime.strptime(qn_end_time, '%Y-%m-%d %H:%M:%S')
    qn.qn_refillable = qn_refillable

    # 创建问题并加入问卷中
    question_list = json.loads(question_data)
    for i in range(len(question_list)):
        q_data = question_list[i]
        question = Question.objects.create(
            q_questionnaire=qn,
            q_position=i,
            q_type=q_data.get('q_type'),
            q_title=q_data.get('q_title'),
            q_description=q_data.get('q_description'),
            q_option_count=q_data.get('q_option_count'),
            q_options=q_data.get('q_options'),
            q_correct_answer=q_data.get('q_correct_answer'),
            q_score=q_data.get('q_score'),
        )
        question.save()
        qn.qn_questions.add(question)

    qn.save()
    # 返回问卷创建成功的响应
    return JsonResponse({'code': 0, 'message': '问卷创建成功'})


@csrf_exempt
@login_required
@questionnaire_exists
@require_http_methods(['POST'])
def delete_questionnaire(request):
    qnid = request.body.get('qnid')
    qn = Questionnaire.objects.get(qn_id=qnid)
    qn.delete()
    return JsonResponse({'errno': 0, 'msg': "问卷删除成功"})


@csrf_exempt
@login_required
@questionnaire_exists
@require_http_methods(['POST'])
def change_questionnaire_status(request):
    qnid = request.body.get('qnid')
    status = request.body.get('status')
    qn = Questionnaire.objects.get(qn_id=qnid)
    qn.status = status
    qn.save()
    return JsonResponse({'errno': 0, 'msg': "问卷状态更改成功"})


# # 管理员操作
# path('ban_questionnaire', ban_questionnaire),
