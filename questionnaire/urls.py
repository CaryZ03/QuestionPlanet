from django.urls import path
from .views import *

urlpatterns = [
    # 填写问卷
    path('fill/<int:qn_id>', fill_questionnaire),
    path('save_answers', save_answers),
    path('submit_answers', submit_answers),
    # 编辑问卷
    path('save_questionnaire', save_questionnaire),
    # 管理问卷
    path('create_questionnaire', create_questionnaire),
    path('delete_questionnaire', delete_questionnaire),
    # 管理员操作
    path('change_questionnaire_status', change_questionnaire_status),
]