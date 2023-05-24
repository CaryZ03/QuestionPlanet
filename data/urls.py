from django.urls import path
from .views import *

urlpatterns = [
    path('questionnaire_export', questionnaire_export),
    path('questionnaire_export_file', questionnaire_export_file),
    path('questionnaire_analysis', questionnaire_analysis),
    path('get_questions_by_questionnaire', get_questions_by_questionnaire),
    path('get_answers_by_question', get_answers_by_question),
    path('delete_answer', delete_answer),
    path('generate_chart', generate_chart),
    path('import_questionnaire', import_questionnaire),
]
