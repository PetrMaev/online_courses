from config.settings import EMAIL_HOST_USER
from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_email_course_update(course_title, email):
    send_mail(
        f'Обновления в курсе {course_title}',
        'Перейдите в личный кабинет, чтобы ознакомиться с обновлениями',
        EMAIL_HOST_USER,
        [email]
    )
