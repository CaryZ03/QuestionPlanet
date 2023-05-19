import re
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.http.response import JsonResponse
import json
from user.models import User, Admin
from questionnaire.models import Questionnaire
from user.views import login_required, not_login_required, admin_required
from random import randint
import smtplib
from email.mime.text import MIMEText
from email.header import Header


# path('fill_questionnaire', fill_questionnaire),
# path('save_answers', save_answers),
# path('submit_answers', submit_answers),
# path('refill_questionnaire', refill_questionnaire),
# # 编辑问卷
# path('add_question', add_question),
# path('edit_question', edit_question),
# path('delete_question', delete_question),
# path('sort_question', sort_question),
# path('save_questionnaire', save_questionnaire),
# # 管理问卷
# path('create_questionnaire', create_questionnaire),
# path('import_questionnaire', import_questionnaire),
# path('edit_questionnaire', edit_questionnaire),
# path('delete_questionnaire', delete_questionnaire),
# path('sort_questionnaire', sort_questionnaire),
# path('export_questionnaire', export_questionnaire),
# path('submit_questionnaire', submit_questionnaire),
# path('share_questionnaire', share_questionnaire),
# # 管理员操作
# path('ban_questionnaire', ban_questionnaire),
@csrf_exempt
@admin_required
@require_http_methods(['POST'])
def ban_questionnaire(request):
    qnid = request.body.get('qnid')
    ban = request.body.get('ban')
    if not Questionnaire.objects.filter(qn_id=qnid).exists():
        return JsonResponse({'errno': 1131, 'msg': "问卷不存在"})
    else:
        qn = Questionnaire.objects.get(qn_id=qnid)
        if ban:
            qn.status = "banned"
            qn.save()
            return JsonResponse({'errno': 0, 'msg': "问卷封禁成功"})
        else:
            qn.status = "unpublished"
            qn.save()
            return JsonResponse({'errno': 0, 'msg': "问卷解封成功"})
