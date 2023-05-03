from django.urls import path
from .views import *

urlpatterns = [
    # 填写问卷
    path('fill_questionnaire', fill_questionnaire),
    path('save_answers', save_answers),
    path('submit_answers', submit_answers),
    path('refill_questionnaire', refill_questionnaire),
    # 编辑问卷
    path('add_question', add_question),
    path('edit_question', edit_question),
    path('delete_question', delete_question),
    path('sort_question', sort_question),
    path('save_questionnaire', save_questionnaire),
    # 管理问卷
    path('create_questionnaire', create_questionnaire),
    path('import_questionnaire', import_questionnaire),
    path('edit_questionnaire', edit_questionnaire),
    path('delete_questionnaire', delete_questionnaire),
    path('sort_questionnaire', sort_questionnaire),
    path('export_questionnaire', export_questionnaire),
    path('submit_questionnaire', submit_questionnaire),
    path('share_questionnaire', share_questionnaire),
    # 管理员操作
    path('ban_questionnaire', ban_questionnaire),
    path('un_ban_questionnaire', un_ban_questionnaire),
]