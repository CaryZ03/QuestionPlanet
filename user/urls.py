from django.urls import path
from .views import *

urlpatterns = [
    path('user_register', user_register, name='user_register'),
    path('user_login', user_login, name='user_login'),
    path('admin_login', admin_login, name='admin_login'),
    path('send_verification_code', send_verification_code, name='send_verification_code'),
    path('reset_password', reset_password, name='reset_password'),
    path('logout', logout, name='logout'),
    path('cancel_account', cancel_account, name='cancel_account'),
    path('check_profile', check_profile, name='check_profile'),
    path('check_profile_admin', check_profile_admin, name='check_profile_admin'),
    path('change_profile', change_profile, name='change_profile'),
    path('change_profile_admin', change_profile_admin, name='change_profile_admin'),
    path('check_questionnaire_list/<str:qn_list_type>', check_questionnaire_list, name='check_questionnaire_list'),
    path('change_user_status', change_user_status, name='change_user_status'),
    path('upload_avatar', upload_avatar, name='upload_avatar'),
    path('check_token', check_token, name='check_token'),
    path('deploy_test', deploy_test, name='deploy_test'),
]
