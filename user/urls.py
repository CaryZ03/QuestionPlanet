from django.urls import path
from .views import *

urlpatterns = [
    path('user_register', user_register),  # 指定register函数的路由为register
    path('user_login', user_login),
    path('user_logout', user_logout),
    path('cancel_account', cancel_account),
    path('change_password', change_password),
    path('check_profile', check_profile),
    path('change_profile', change_profile),
    path('check_created_questionnaires', check_created_questionnaires),
    path('check_filled_questionnaires', check_filled_questionnaires),
    path('ban_user', ban_user),
    path('un_ban_user', un_ban_user),
    path('ban_questionnaire', ban_questionnaire),
    path('un_ban_questionnaire', un_ban_questionnaire),
    path('delete_data', logout),
    path('logout', logout),
    path('logout', logout),
    path('logout', logout),
    path('logout', logout),

]
