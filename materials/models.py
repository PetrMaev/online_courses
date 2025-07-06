from django.db import models
from django.core.validators import URLValidator


class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name="Название курса")
    preview = models.ImageField(
        upload_to="materials/images/",
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="Загрузите изображение",
    )
    description = models.TextField(verbose_name="Описание")
    owner = models.ForeignKey(
        'users.CustomUser',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Владелец",
    )
    is_subscribe = models.BooleanField(default=False, verbose_name="Подписка на курс активна\неактивна")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "курс"
        verbose_name_plural = "курсы"


class Lesson(models.Model):
    title = models.CharField(max_length=225, verbose_name="Название урока")
    description = models.TextField(verbose_name="Описание")
    preview = models.ImageField(
        upload_to="materials/images/",
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="Загрузите изображение",
    )
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="lessons", verbose_name="Курс обучения")
    video_link = models.URLField(
        max_length=500,
        blank=True,
        null=True,
        validators=[URLValidator(schemes="https")],
        verbose_name="Ссылка на видео"
    )
    owner = models.ForeignKey(
        'users.CustomUser',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Владелец",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "урок"
        verbose_name_plural = "уроки"


class Subscribe(models.Model):
    user = models.ForeignKey(
        "users.CustomUser",
        on_delete=models.CASCADE,
        verbose_name="Пользователь"
    )
    course = models.ForeignKey(
        "Course",
        on_delete=models.CASCADE,
        related_name="courses",
        verbose_name="Название курса"
    )

    def __str__(self):
        return Course.title

    class Meta:
        verbose_name = "подписка"
        verbose_name_plural = "подписки"
