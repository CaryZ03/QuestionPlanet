from collections import Counter
from django.shortcuts import render
from django.db.models import Count, Avg, StdDev
from datetime import datetime
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest
from questionnaire.models import *
from user.models import *
from django.views.decorators.http import require_GET, require_http_methods
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64
import json
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.db import transaction
import csv


def get_session(session_id):
    return session_id


def check_identity(view_func):
    def wrapper(request, *args, **kwargs):
        token_key = request.headers.get('Authorization')
        body = request.body.decode('utf-8')
        data = json.loads(body)
        if token_key:
            # 使用 Token 模型的 objects.get 方法查找令牌
            token = UserToken.objects.filter(key=token_key).first()
            if token is None or token.expire_time < now():
                return JsonResponse({'errno': 3002, 'msg': "登录信息已过期"})
            elif not token.is_admin:
                user_id = data.get('uid')
                if token.user.user_id != user_id:
                    return JsonResponse({'errno': 3003, 'msg': "用户不一致"})
                if not User.objects.filter(user_id=user_id).exists():
                    return JsonResponse({'errno': 3004, 'msg': "用户不存在"})
                user = User.objects.get(user_id=user_id)
                if 'qn_id' in data:
                    qn_id = data.get('qn_id')
                    if not Questionnaire.objects.filter(qn_id=qn_id).exists():
                        return JsonResponse({'errno': 3005, 'msg': "问卷不存在"})
                    questionnaire = Questionnaire.objects.get(qn_id=qn_id)
                    if questionnaire not in user.user_created_questionnaires.all():
                        return JsonResponse({'errno': 3008, 'msg': '用户没有权限进行该操作'})
                elif 'q_id' in data:
                    q_id = data.get('q_id')
                    if not Question.objects.filter(q_id=q_id).exists():
                        return JsonResponse({'errno': 3006, 'msg': "问题不存在"})
                    question = Question.objects.get(q_id=q_id)
                    questionnaire = question.q_questionnaire
                    if questionnaire not in user.user_created_questionnaires.all():
                        return JsonResponse({'errno': 3008, 'msg': '用户没有权限进行该操作'})
                elif 'a_id' in data:
                    a_id = data.get('a_id')
                    if not Answer.objects.filter(a_id=a_id).exists():
                        return JsonResponse({'errno': 3007, 'msg': "答案不存在"})
                    answer = Answer.objects.get(a_id=a_id)
                    question = answer.a_question
                    questionnaire = question.q_questionnaire
                    if questionnaire not in user.user_created_questionnaires.all():
                        return JsonResponse({'errno': 3008, 'msg': '用户没有权限进行该操作'})
                return view_func(request, *args, **kwargs)
            else:
                admin_id = data.get('uid')
                if token.admin.admin_id != admin_id:
                    return JsonResponse({'errno': 3003, 'msg': "用户不一致"})
                else:
                    return view_func(request, *args, **kwargs)
        else:
            return JsonResponse({'errno': 3001, 'msg': "未登录"})

    return wrapper


# def check_identity(view_func):
#     def wrapper(request, *args, **kwargs):
#         session_id = request.COOKIES.get('session_id')
#         body = request.body.decode('utf-8')
#         data = json.loads(body)
#         if session_id:
#             # 根据session_id获取相应的会话数据
#             session_data = get_session(session_id)
#             # 处理会话数据
#             if session_data is None:
#                 return JsonResponse({'errno': 3002, 'msg': "登录信息已过期"})
#             elif session_data.get('id') != json.loads(request.body).get('uid'):
#                 return JsonResponse({'errno': 3003, 'msg': "用户不一致"})
#             elif session_data.get('role') != 'admin':
#                 user_id = data.get('uid')
#                 if not User.objects.filter(user_id=user_id).exists():
#                     return JsonResponse({'errno': 3004, 'msg': "用户不存在"})
#                 user = User.objects.get(user_id=user_id)
#                 if 'qn_id' in data:
#                     qn_id = data.get('qn_id')
#                     if not Questionnaire.objects.filter(qn_id=qn_id).exists():
#                         return JsonResponse({'errno': 3005, 'msg': "问卷不存在"})
#                     questionnaire = Questionnaire.objects.get(qn_id=qn_id)
#                     if questionnaire not in user.user_created_questionnaires.all():
#                         return JsonResponse({'errno': 3008, 'msg': '用户没有权限进行该操作'})
#                 elif 'q_id' in data:
#                     q_id = data.get('q_id')
#                     if not Question.objects.filter(q_id=q_id).exists():
#                         return JsonResponse({'errno': 3006, 'msg': "问题不存在"})
#                     question = Question.objects.get(q_id=q_id)
#                     questionnaire = question.q_questionnaire
#                     if questionnaire not in user.user_created_questionnaires.all():
#                         return JsonResponse({'errno': 3008, 'msg': '用户没有权限进行该操作'})
#                 elif 'a_id' in data:
#                     a_id = data.get('a_id')
#                     if not Answer.objects.filter(a_id=a_id).exists():
#                         return JsonResponse({'errno': 3007, 'msg': "答案不存在"})
#                     answer = Answer.objects.get(a_id=a_id)
#                     question = answer.a_question
#                     questionnaire = question.q_questionnaire
#                     if questionnaire not in user.user_created_questionnaires.all():
#                         return JsonResponse({'errno': 3008, 'msg': '用户没有权限进行该操作'})
#             return view_func(request, *args, **kwargs)
#         else:
#             return JsonResponse({'errno': 3001, 'msg': "未登录"})
#     return wrapper
def calculate_score(answer_sheet):
    total_score = 0
    for answer in answer_sheet.as_answers.all():
        total_score += answer.a_score
    return total_score


@csrf_exempt
@check_identity
@require_http_methods(['GET'])
def questionnaire_export(request):
    qn_id = json.loads(request.body.decode('utf-8')).get('qn_id')
    questionnaire = Questionnaire.objects.get(qn_id=qn_id)
    questions_count = Question.objects.filter(q_questionnaire=questionnaire).count()
    answer_sheet_count = AnswerSheet.objects.filter(as_questionnaire=questionnaire).count()
    score_avg = Answer.objects.filter(a_question__q_questionnaire=questionnaire).aggregate(Avg('a_score'))[
        'a_score__avg']
    score_stddev = Answer.objects.filter(a_question__q_questionnaire=questionnaire).aggregate(StdDev('a_score'))[
        'a_score__stddev']
    single_count = Question.objects.filter(q_questionnaire=questionnaire, q_type='single').count()
    multiple_count = Question.objects.filter(q_questionnaire=questionnaire, q_type='multiple').count()
    judge_count = Question.objects.filter(q_questionnaire=questionnaire, q_type='judge').count()
    fill_count = Question.objects.filter(q_questionnaire=questionnaire, q_type='fill').count()
    essay_count = Question.objects.filter(q_questionnaire=questionnaire, q_type='essay').count()
    grade_count = Question.objects.filter(q_questionnaire=questionnaire, q_type='grade').count()
    result = {
        'questionnaire_id': questionnaire.qn_id,
        'questionnaire_title': questionnaire.qn_title,
        'questionnaire_description': questionnaire.qn_description,
        'questions_count': questions_count,
        'answer_sheet_count': answer_sheet_count,
        'score_avg': score_avg,
        'score_stddev': score_stddev,
        'single_count': single_count,
        'multiple_count': multiple_count,
        'judge_count': judge_count,
        'fill_count': fill_count,
        'essay_count': essay_count,
        'grade_count': grade_count
    }
    return JsonResponse({'errno': 0, 'msg': '信息导出成功', 'result': result})


@csrf_exempt
@check_identity
@require_http_methods(['GET'])
def questionnaire_export_file(request):
    qn_id = json.loads(request.body.decode('utf-8')).get('qn_id')
    questionnaire = Questionnaire.objects.get(qn_id=qn_id)
    questions_count = Question.objects.filter(q_questionnaire=questionnaire).count()
    answer_sheet_count = AnswerSheet.objects.filter(as_questionnaire=questionnaire).count()
    score_avg = Answer.objects.filter(a_question__q_questionnaire=questionnaire).aggregate(Avg('a_score'))[
        'a_score__avg']
    score_stddev = Answer.objects.filter(a_question__q_questionnaire=questionnaire).aggregate(StdDev('a_score'))[
        'a_score__stddev']
    single_count = Question.objects.filter(q_questionnaire=questionnaire, q_type='single').count()
    multiple_count = Question.objects.filter(q_questionnaire=questionnaire, q_type='multiple').count()
    judge_count = Question.objects.filter(q_questionnaire=questionnaire, q_type='judge').count()
    fill_count = Question.objects.filter(q_questionnaire=questionnaire, q_type='fill').count()
    essay_count = Question.objects.filter(q_questionnaire=questionnaire, q_type='essay').count()
    grade_count = Question.objects.filter(q_questionnaire=questionnaire, q_type='grade').count()

    # 创建CSV文件
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="questionnaire_{qn_id}_export.csv"'

    writer = csv.writer(response)

    # 写入问卷信息
    writer.writerow(['Questionnaire ID', 'Questionnaire Title', 'Questionnaire Description', 'Questions Count',
                     'Answer Sheet Count', 'Score Average', 'Score Standard Deviation', 'Single Choice Count',
                     'Multiple Choice Count', 'Judge Count', 'Fill Count', 'Essay Count', 'Grade Count'])

    writer.writerow([questionnaire.qn_id, questionnaire.qn_title, questionnaire.qn_description, questions_count,
                     answer_sheet_count, score_avg, score_stddev, single_count, multiple_count, judge_count,
                     fill_count, essay_count, grade_count])

    return response


@csrf_exempt
@check_identity
@require_http_methods('GET')
def questionnaire_analysis(request):
    qn_id = json.loads(request.body.decode('utf-8')).get('qn_id')
    questionnaire = Questionnaire.objects.get(qn_id=qn_id)
    questions_count = Question.objects.filter(q_questionnaire=questionnaire).count()
    questions = Question.objects.filter(q_questionnaire=questionnaire)
    q_results = []
    i = 0
    for question in questions:
        answers = Answer.objects.filter(a_question=question)
        q_result = {}
        q_result['q_description'] = question.q_description
        q_result['q_type'] = question.q_type
        if question.q_type == 'single' or question.q_type == 'multiple':
            options = list(question.q_options)
            q_result['q_options'] = [{'choose': str(num), 'label': option, 'num': 0} for num, option in enumerate(options)]
            for answer in answers:
                a_content = answer.a_content.upper()
                for option in q_result['q_options']:
                    if option['choose'] in a_content:
                        option['num'] += 1
        elif question.q_type == 'judge':
            q_result['q_options'] = [{'choose': '0', 'label': 'False', 'num': 0}, {'choose': '1', 'label': 'True', 'num': 0}]
            for answer in answers:
                a_content = answer.a_content.capitalize()
                for option in q_result['q_options']:
                    if option['choose'] == a_content:
                        option['num'] += 1
        q_results.append(q_result)
        i = i + 1
    result = {
        'questionnaire_id': questionnaire.qn_id,
        'questionnaire_title': questionnaire.qn_title,
        'questionnaire_description': questionnaire.qn_description,
        'questions_count': questions_count,
        'q_results': q_results
    }
    return JsonResponse({'errno': 0, 'msg': '问卷分析成功', 'result': result})


@csrf_exempt
@check_identity
@require_http_methods(['GET'])
def get_questions_by_questionnaire(request):
    qn_id = json.loads(request.body.decode('utf-8')).get('qn_id')

    try:
        questionnaire = Questionnaire.objects.get(qn_id=qn_id)
    except Questionnaire.DoesNotExist:
        return JsonResponse({'errno': 3041, 'msg': '问卷不存在'})

    questions = questionnaire.qn_questions.all()

    response_data = {
        'qn_id': questionnaire.qn_id,
        'qn_title': questionnaire.qn_title,
        'qn_description': questionnaire.qn_description,
        'questions': list(questions.values())
    }

    return JsonResponse({'errno': 0, 'msg': '数据筛选成功', 'response_data': response_data})


@csrf_exempt
@check_identity
@require_http_methods(['GET'])
def get_answers_by_question(request):
    q_id = json.loads(request.body.decode('utf-8')).get('q_id')

    try:
        question = Question.objects.get(q_id=q_id)
    except Question.DoesNotExist:
        return JsonResponse({'errno': 3051, 'msg': '问题不存在'})

    answers = question.q_answers.all()

    response_data = {
        'q_id': question.q_id,
        'q_title': question.q_title,
        'q_description': question.q_description,
        'answers': list(answers.values())
    }

    return JsonResponse({'errno': 0, 'msg': '数据筛选成功', 'response_data': response_data})


@csrf_exempt
@check_identity
@require_http_methods(['POST'])
def delete_answer(request):
    a_id = json.loads(request.body.decode('utf-8')).get('a_id')
    answer = Answer.objects.get(a_id=a_id)
    data = {
        'a_id': answer.a_id,
        'a_question': answer.a_question.q_id,
        'a_answersheet': answer.a_answersheet.as_id,
        'a_content': answer.a_content,
        'a_score': answer.a_score,
        'a_comment': answer.a_comment,
    }
    answer.delete()
    return JsonResponse({'errno': 0, 'msg': '数据删除成功', 'deleted_data': data})


@csrf_exempt
@check_identity
@require_http_methods(['GET'])
def generate_chart(request):
    qn_id = json.loads(request.body.decode('utf-8')).get('qn_id')
    questionnaires = Question.objects.filter(qn_id=qn_id).prefetch_related('q_questions')
    questions = questionnaires.first().q_questions.all()

    data = []
    for question in questions:
        if question.q_type == 'single' or question.q_type == 'multiple' or question.q_type == 'judge':
            answers = Answer.objects.filter(a_question=question)
            content_counts = answers.values('a_content').annotate(count=Count('a_content'))
            content_counts_df = pd.DataFrame(list(content_counts))
            title = question.q_title
            data.append((title, content_counts_df))

    figs = []
    for title, content_counts_df in data:
        fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(16, 6))
        fig.suptitle(title, fontsize=16)

        # Generate bar chart
        content_counts_df.plot(kind='bar', x='a_content', y='count', ax=ax1)
        ax1.set_xlabel('Answer Content')
        ax1.set_ylabel('Count')
        ax1.set_title('Bar Chart')

        # Generate pie chart
        content_counts_df.plot(kind='pie', y='count', labels=content_counts_df['a_content'], autopct='%1.1f%%',
                               startangle=90, ax=ax2)
        ax2.set_xlabel('Answer Content')
        ax2.set_ylabel('')
        ax2.set_title('Pie Chart')

        # Save figure to memory
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        figs.append(buf)

        # Close plot to free memory
        plt.close()

    response = JsonResponse({'charts': [base64.b64encode(fig.getvalue()).decode('utf-8') for fig in figs]})
    response['Content-Type'] = 'application/json'
    return response


@csrf_exempt
@transaction.atomic
@require_http_methods(['POST'])
def import_questionnaire(request):
    file = request.FILES['file']  # 获取上传的文件
    ext = file.name.split('.')[-1]  # 获取文件扩展名
    if ext not in ['txt', 'doc']:
        return HttpResponseBadRequest('Invalid file type')  # 文件类型不符合要求

    # 读取文件内容
    file_content = file.read().decode('utf-8')

    # 解析文件内容，按照题目分割
    raw_questions = file_content.split('\n\n')
    questions = []

    # 逐个解析题目
    for raw_question in raw_questions:
        lines = raw_question.strip().split('\n')
        q_type = lines[0].strip()
        q_title = lines[1].strip()
        q_description = lines[2].strip()
        q_option_count = 0
        q_options = None
        q_correct_answer = None

        if q_type == '__single__' or q_type == '__multiple__':
            q_option_count = int(lines[3].strip())
            q_options = []
            for i in range(q_option_count):
                q_options.append(lines[4 + i].strip())
            q_correct_answer = lines[4 + q_option_count].strip()

        elif q_type == '__judge__':
            q_option_count = 2
            q_options = [lines[3].strip(), lines[4].strip()]
            q_correct_answer = lines[5].strip()

        else:
            q_correct_answer = lines[3].strip()

        question = Question(
            q_type=q_type[2:-2],  # 去掉__前缀和__后缀
            q_title=q_title,
            q_description=q_description,
            q_option_count=q_option_count,
            q_options=q_options,
            q_correct_answer=q_correct_answer,
        )
        questions.append(question)

    # 创建问卷对象
    questionnaire = Questionnaire(
        qn_title='imported',  # 设置默认标题
        qn_description='imported',  # 设置默认描述
        qn_createTime=datetime.now(),
        qn_endTime=None,
        qn_status='unpublished',  # 默认为未发布状态
        qn_refillable=True,
    )
    questionnaire.save()

    # 将解析的题目添加到问卷中
    for question in questions:
        question.q_questionnaire = questionnaire
        question.save()

    return JsonResponse({'errno': 0, 'msg': '问卷导入成功'})
