from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Course, Lesson


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Email")
    avatar = models.ImageField(
        upload_to="users/avatars/",
        blank=True,
        null=True,
        verbose_name="Аватар",
        help_text="Загрузите свой аватар",
    )
    phone_number = models.CharField(
        max_length=25,
        blank=True,
        null=True,
        verbose_name="Номер телефона",
        help_text="Введите свой номер телефона",
    )
    country = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Страна",
        help_text="Укажите свою страну",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Payments(models.Model):
    CASH = "cash"
    TRANSFER = "transfer"

    METHOD_CHOICES = [
        (CASH, "Наличные"),
        (TRANSFER, "Перевод"),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Пользователь", related_name="user")
    date = models.DateField(verbose_name="Дата оплаты")
    paid_course = models.ForeignKey(
        Course, on_delete=models.CASCADE, verbose_name="Оплаченный курс", related_name="course"
    )
    paid_lesson = models.ForeignKey(
        Lesson, on_delete=models.CASCADE, verbose_name="Оплаченный урок", related_name="lesson"
    )
    amount = models.IntegerField(verbose_name="Сумма оплаты")
    pay_method = models.CharField(max_length=15, choices=METHOD_CHOICES, verbose_name="Способ оплаты")

    def __str__(self):
        return f"{self.user} - {self.amount}"

    class Meta:
        verbose_name = "платеж"
        verbose_name_plural = "платежи"
