from datetime import timedelta

from django.utils import timezone
from celery import shared_task

from users.models import CustomUser


# @shared_task
# def check_last_login_user():
#     users = CustomUser.objects.all()
#     month_ago = timezone.now() - timedelta(days=30)
#     for user in users:
#         if user.groups.filter(name='Moderators').not_exists() or user.filter(
#                 is_superuser=True).not_exists():
#             user.filter(last_login__lt=month_ago, is_active=True).update(
#                 is_active=False
#         )
#         else:
#             continue


@shared_task
def check_last_login_user():
    today = timezone.now().today()
    users = CustomUser.objects.all()
    for user in users:
        if user.groups.filter(
                name='Moderators').not_exists() or user.is_superuser != True and today - user.last_login > timedelta(
                days=30):
            user.is_active = False
            user.save()
        else:
            continue
