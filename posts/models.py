from django.db import models
from django.utils import timezone

class Post(models.Model):

    title = models.CharField(max_length=120)
    content = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Моя модель'
        verbose_name_plural = 'Мои модели'
