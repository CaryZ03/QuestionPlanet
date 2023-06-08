from django.urls import path

from .views import *

urlpatterns = [
    # 填写问卷
    path('fill_questionnaire/<int:qn_id>', fill_questionnaire, name='fill_questionnaire'),
    path('save_answers', save_answers, name='save_answers'),
    path('submit_answers', submit_answers, name='submit_answers'),
    path('save_questionnaire', save_questionnaire, name='save_questionnaire'),
    # 编辑问卷
    path('create_questionnaire', create_questionnaire, name='create_questionnaire'),
    # 管理问卷
    path('copy_questionnaire/<int:qn_id>', copy_questionnaire, name='copy_questionnaire'),
    path('check_questionnaire/<int:qn_id>', check_questionnaire, name='check_questionnaire'),
    path('delete_questionnaire', delete_questionnaire, name='delete_questionnaire'),
    # 管理员操作
    path('change_questionnaire_status', change_questionnaire_status, name='change_questionnaire_status'),
]
