from django.urls import path
from .views import *

urlpatterns = [
    path('user_register', user_register),
    path('user_login', user_login),
    path('send_verification_code', send_verification_code),
    path('reset_password', reset_password),
    path('check_profile', check_profile),
    path('change_profile', change_profile),
    path('check_created_questionnaires', check_created_questionnaires),
    path('check_filled_questionnaires', check_filled_questionnaires),
    path('logout', logout),
    path('check_profile_admin', check_profile_admin),
    path('change_profile_admin', change_profile_admin),
    path('admin_login', admin_login),
    path('cancel_account', cancel_account),
    path('ban_user', ban_user),
    path('un_ban_user', un_ban_user),
]
