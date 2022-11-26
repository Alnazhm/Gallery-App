from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Image(models.Model):
    image = models.ImageField(
        verbose_name='Картинка',
        default='default_image.png',
        null=False,
        blank=False,
    )
    sign = models.CharField(
        verbose_name='Подпись',
        max_length=200,
        null=False,
        blank=False
    )
    author = models.CharField(verbose_name='Автор',
                              max_length=100,
                              null=False,
                              blank=False,
                              default='No name')
    users = models.ManyToManyField(
        to=User,
        related_name='images'
    )
    created_at = models.DateTimeField(
        verbose_name='Время создания',
        auto_now_add=True)
    updated_at = models.DateTimeField(
        verbose_name='Время изменения',
        auto_now=True)


    def __str__(self):
        return f"{self.image} - {self.sign}- {self.author}"



    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'




