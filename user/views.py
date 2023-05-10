from collections import Counter
from django.shortcuts import render
from django.db.models import Count, Avg, StdDev
from datetime import datetime
from django.http import JsonResponse
from questionnaire.models import *
from user.models import *
from django.views.decorators.http import require_GET
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64
import json


@csrf_exempt
def create_questionnaire(request):
    if request.method == 'POST':
        # 从请求中获取问卷信息和问题数据
        qn_title = request.POST.get('qn_title')
        qn_description = request.POST.get('qn_description')
        qn_end_time_str = request.POST.get('qn_end_time')
        qn_status = request.POST.get('qn_status')
        qn_refillable = request.POST.get('qn_refillable')
        question_data = request.POST.get('question_data')

        # 创建问卷
        questionnaire = Questionnaire.objects.create(
            qn_title=qn_title,
            qn_description=qn_description,
            qn_createTime=datetime.now(),
            qn_endTime=datetime.strptime(qn_end_time_str, '%Y-%m-%d %H:%M:%S'),
            qn_status=qn_status,
            qn_refillable=qn_refillable,
        )

        try:
            # 创建问题并加入问卷中
            question_list = json.loads(question_data)
            for q_data in question_list:
                question = Question.objects.create(
                    q_questionnaire=questionnaire,
                    q_type=q_data.get('q_type'),
                    q_title=q_data.get('q_title'),
                    q_description=q_data.get('q_description'),
                    q_option_count=q_data.get('q_option_count'),
                    q_options=q_data.get('q_options'),
                    q_correct_answer=q_data.get('q_correct_answer'),
                )
                question.save()
                questionnaire.qn_questions.add(question)

            questionnaire.qn_answers.clear()
            questionnaire.save()
            # 返回问卷创建成功的响应
            return JsonResponse({'code': 0, 'message': 'success.'})
        except (json.JSONDecodeError, KeyError):
            return JsonResponse({'code': -1, 'message': 'invalid answer data.'})
    else:
        return JsonResponse({'code': -1, 'message': 'only support POST method.'})


@csrf_exempt
def answer_questionnaire(request):
    if request.method == 'POST':
        # 获取请求参数
        user_id = request.POST.get('user_id')
        questionnaire_id = request.POST.get('questionnaire_id')
        answer_data = request.POST.get('answer_data')

        # 验证用户和问卷是否存在
        if not user_id or not questionnaire_id:
            return JsonResponse({'code': -1, 'message': 'user_id or questionnaire_id is required.'})
        try:
            user = User.objects.get(user_id=user_id)
            questionnaire = Questionnaire.objects.get(qn_id=questionnaire_id)
        except User.DoesNotExist:
            return JsonResponse({'code': -1, 'message': 'user not found.'})
        except Questionnaire.DoesNotExist:
            return JsonResponse({'code': -1, 'message': 'questionnaire not found.'})

        # 创建答卷对象
        answer_sheet = AnswerSheet.objects.create(as_user=user, as_questionnaire=questionnaire)

        # 解析答案数据，创建答案对象
        try:
            answer_list = json.loads(answer_data)
            for answer_item in answer_list:
                q_id = answer_item.get('question_id')
                question = Question.objects.get(q_id=q_id)
                if question.q_correct_answer == answer_item['content']:
                    score = 1
                else:
                    score = 0
                answer = Answer.objects.create(
                    a_user=user,
                    a_question_id=answer_item.get('question_id'),
                    a_content=answer_item.get('content'),
                    a_score=score,
                    a_comment=answer_item.get('comment'),
                )
                answer.save()
                answer_sheet.as_answers.add(answer)
            answer_sheet.as_score = calculate_score(answer_sheet)  # 计算得分
            answer_sheet.save()
            return JsonResponse({'code': 0, 'message': 'success.'})
        except (json.JSONDecodeError, KeyError):
            return JsonResponse({'code': -1, 'message': 'invalid answer data.'})
    else:
        return JsonResponse({'code': -1, 'message': 'only support POST method.'})


def calculate_score(answer_sheet):
    total_score = 0
    for answer in answer_sheet.as_answers.all():
        total_score += answer.a_score
    return total_score


def questionnaire_export(request, qn_id):
    questionnaire = Questionnaire.objects.get(qn_id=qn_id)
    questions_count = Question.objects.filter(q_questionnaire=questionnaire).count()
    answer_sheet_count = AnswerSheet.objects.filter(as_questionnaire=questionnaire).count()
    score_avg = Answer.objects.filter(a_question__q_questionnaire=questionnaire).aggregate(Avg('a_score'))['a_score__avg']
    score_stddev = Answer.objects.filter(a_question__q_questionnaire=questionnaire).aggregate(StdDev('a_score'))['a_score__stddev']
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
    return JsonResponse(result)


@require_GET
def questionnaire_analysis(request, qn_id):
    questionnaire = Questionnaire.objects.get(qn_id=qn_id)
    questions_count = Question.objects.filter(q_questionnaire=questionnaire).count()
    answer_sheet_count = AnswerSheet.objects.filter(as_questionnaire=questionnaire).count()
    score_avg = Answer.objects.filter(a_question__q_questionnaire=questionnaire).aggregate(Avg('a_score'))['a_score__avg']
    score_stddev = Answer.objects.filter(a_question__q_questionnaire=questionnaire).aggregate(StdDev('a_score'))['a_score__stddev']
    single_count = Question.objects.filter(q_questionnaire=questionnaire, q_type='single').count()
    multiple_count = Question.objects.filter(q_questionnaire=questionnaire, q_type='multiple').count()
    judge_count = Question.objects.filter(q_questionnaire=questionnaire, q_type='judge').count()
    fill_count = Question.objects.filter(q_questionnaire=questionnaire, q_type='fill').count()
    essay_count = Question.objects.filter(q_questionnaire=questionnaire, q_type='essay').count()
    grade_count = Question.objects.filter(q_questionnaire=questionnaire, q_type='grade').count()

    # 统计单选、多选和判断题的选项统计
    single_choice_answers = Answer.objects.filter(a_question__q_questionnaire=questionnaire, a_question__q_type='single').values('a_content').annotate(Count('a_content')).order_by('-a_content__count')
    multiple_choice_answers = Answer.objects.filter(a_question__q_questionnaire=questionnaire, a_question__q_type='multiple').values('a_content').annotate(Count('a_content')).order_by('-a_content__count')
    judge_answers = Answer.objects.filter(a_question__q_questionnaire=questionnaire, a_question__q_type='judge').values('a_content').annotate(Count('a_content')).order_by('-a_content__count')

    # 统计填空题的出现频率最高的前三个词
    fill_answers = Answer.objects.filter(a_question__q_questionnaire=questionnaire, a_question__q_type='fill').exclude(a_content='').values_list('a_content', flat=True)
    fill_words = ' '.join(fill_answers).split()
    fill_top_words = dict(Counter(fill_words).most_common(3))

    result = {
        'questionnaire_id': questionnaire.qn_id,
        'questionnaire_title': questionnaire.qn_title,
        'questionnaire_description': questionnaire.qn_description,
        'questions_count': questions_count,
        'answer_sheet_count': answer_sheet_count,
        'score_avg': score_avg,
        'score_stddev': score_stddev,
        'single_choice_count': single_count,
        'single_choice_answers': single_choice_answers,
        'multiple_choice_count': multiple_count,
        'multiple_choice_answers': multiple_choice_answers,
        'judge_count': judge_count,
        'judge_answers': judge_answers,
        'fill_count': fill_count,
        'fill_top_words': fill_top_words,
        'essay_count': essay_count,
        'grade_count': grade_count
    }
    return JsonResponse(result)


@require_GET
def get_questions_by_questionnaire(request):
    qn_id = request.GET.get('qn_id')
    if not qn_id:
        return JsonResponse({'error': 'No qn_id provided'})

    try:
        questionnaire = Questionnaire.objects.get(qn_id=qn_id)
    except Questionnaire.DoesNotExist:
        return JsonResponse({'error': 'Invalid q_id'})

    questions = questionnaire.qn_questions.all()

    response_data = {
        'qn_id': questionnaire.qn_id,
        'qn_title': questionnaire.qn_title,
        'qn_description': questionnaire.qn_description,
        'questions': list(questions.values())
    }

    return JsonResponse(response_data)


@require_GET
def get_answers_by_question(request):
    q_id = request.GET.get('q_id')
    if not q_id:
        return JsonResponse({'error': 'No q_id provided'})

    try:
        question = Question.objects.get(q_id=q_id)
    except Question.DoesNotExist:
        return JsonResponse({'error': 'Invalid q_id'})

    answers = question.q_answers.all()

    response_data = {
        'q_id': question.q_id,
        'q_title': question.q_title,
        'q_description': question.q_description,
        'answers': list(answers.values())
    }

    return JsonResponse(response_data)


@csrf_exempt
def delete_answer(request):
    if request.method == 'POST':
        a_id = request.POST.get('a_id')
        try:
            answer = Answer.objects.get(a_id=a_id)
        except Answer.DoesNotExist:
            return JsonResponse({'error': f'Answer with ID {a_id} does not exist.'})
        data = {
            'a_id': answer.a_id,
            'a_user': answer.a_user.user_id if answer.a_user else None,
            'a_question': answer.a_question.q_id if answer.a_question else None,
            'a_createTime': answer.a_createTime,
            'a_content': answer.a_content,
            'a_score': answer.a_score,
            'a_comment': answer.a_comment,
        }
        answer.delete()
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'Invalid request method. Expected POST.'})


@require_GET
def generate_chart(request, qn_id):
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
        content_counts_df.plot(kind='pie', y='count', labels=content_counts_df['a_content'], autopct='%1.1f%%', startangle=90, ax=ax2)
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
