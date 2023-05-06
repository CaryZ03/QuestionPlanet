from collections import Counter

from django.shortcuts import render
from django.db.models import Count, Avg, StdDev
from django.http import JsonResponse
from questionnaire.models import Question, Answer, Questionnaire


def questionnaire_export(request, qn_id):
    questionnaire = Questionnaire.objects.get(qn_id=qn_id)
    answers_count = Answer.objects.filter(a_question__q_questionnaire=questionnaire).count()
    questions_count = Question.objects.filter(q_questionnaire=questionnaire).count()
    score_avg = Answer.objects.filter(a_question__q_questionnaire=questionnaire).aggregate(Avg('a_score'))['a_score__avg']
    score_stddev = Answer.objects.filter(a_question__q_questionnaire=questionnaire).aggregate(StdDev('a_score'))['a_score__stddev']
    single_choice_count = Question.objects.filter(q_questionnaire=questionnaire, q_type='single').count()
    multiple_choice_count = Question.objects.filter(q_questionnaire=questionnaire, q_type='multiple').count()
    judge_count = Question.objects.filter(q_questionnaire=questionnaire, q_type='judge').count()
    fill_count = Question.objects.filter(q_questionnaire=questionnaire, q_type='fill').count()
    essay_count = Question.objects.filter(q_questionnaire=questionnaire, q_type='essay').count()
    grade_count = Question.objects.filter(q_questionnaire=questionnaire, q_type='grade').count()
    result = {
        'questionnaire_id': questionnaire.qn_id,
        'questionnaire_title': questionnaire.qn_title,
        'questionnaire_description': questionnaire.qn_description,
        'answers_count': answers_count,
        'questions_count': questions_count,
        'score_avg': score_avg,
        'score_stddev': score_stddev,
        'single_choice_count': single_choice_count,
        'multiple_choice_count': multiple_choice_count,
        'judge_count': judge_count,
        'fill_count': fill_count,
        'essay_count': essay_count,
        'grade_count': grade_count
    }
    return JsonResponse(result)

def questionnaire_analysis(request, qn_id):
    questionnaire = Questionnaire.objects.get(qn_id=qn_id)
    answers_count = Answer.objects.filter(a_question__q_questionnaire=questionnaire).count()
    questions_count = Question.objects.filter(q_questionnaire=questionnaire).count()
    score_avg = Answer.objects.filter(a_question__q_questionnaire=questionnaire).aggregate(Avg('a_score'))['a_score__avg']
    score_stddev = Answer.objects.filter(a_question__q_questionnaire=questionnaire).aggregate(StdDev('a_score'))['a_score__stddev']
    single_choice_count = Question.objects.filter(q_questionnaire=questionnaire, q_type='single').count()
    multiple_choice_count = Question.objects.filter(q_questionnaire=questionnaire, q_type='multiple').count()
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
        'answers_count': answers_count,
        'questions_count': questions_count,
        'score_avg': score_avg,
        'score_stddev': score_stddev,
        'single_choice_count': single_choice_count,
        'single_choice_answers': single_choice_answers,
        'multiple_choice_count': multiple_choice_count,
        'multiple_choice_answers': multiple_choice_answers,
        'judge_count': judge_count,
        'judge_answers': judge_answers,
        'fill_count': fill_count,
        'fill_top_words': fill_top_words,
        'essay_count': essay_count,
        'grade_count': grade_count
    }
    return JsonResponse(result)


# Create your views here.
