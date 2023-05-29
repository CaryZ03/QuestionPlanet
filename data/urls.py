from django.urls import path
from .views import *

urlpatterns = [
    path('questionnaire_export/<int:qn_id>', questionnaire_export),
    path('questionnaire_export_file/<int:qn_id>', questionnaire_export_file),
    path('questionnaire_analysis/<int:qn_id>', questionnaire_analysis),
    path('get_questions_by_questionnaire/<int:qn_id>', get_questions_by_questionnaire),
    path('get_answers_by_question/<int:q_id>', get_answers_by_question),
    path('delete_answer', delete_answer),
    path('generate_chart/<int:qn_id>', generate_chart),
    path('import_questionnaire', import_questionnaire),
]
