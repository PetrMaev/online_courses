from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название курса')
    preview = models.ImageField(
        upload_to='materials/images/',
        blank=True,
        null=True,
        verbose_name='Изображение',
        help_text='Загрузите изображение'
    )
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    title = models.CharField(max_length=225, verbose_name='Название урока')
    description = models.TextField(verbose_name='Описание')
    preview = models.ImageField(
        upload_to='materials/images/',
        blank=True,
        null=True,
        verbose_name='Изображение',
        help_text='Загрузите изображение'
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='courses',
        verbose_name='Курс обучения'
    )
    video_link = models.TextField(
        blank=True,
        null=True,
        verbose_name='Ссылка на видео'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
