from datetime import timedelta

from django.utils import timezone
from celery import shared_task

from users.models import CustomUser


@shared_task
def check_last_login_user():
    today = timezone.now().today()
    users = CustomUser.objects.all()
    for user in users:
        if (
            user.is_staff != True
            or user.is_superuser != True
            and user.last_login is not None
            and today - user.last_login > timedelta(days=30)
        ):
            user.is_active = False
            user.save()
        else:
            continue
