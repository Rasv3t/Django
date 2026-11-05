from django.db import models
from django.utils import timezone

class Article(models.Model):

    title = models.CharField(max_length=120)
    content = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Артикль'
        verbose_name_plural = 'Артикли'

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя категории')
    slug = models.SlugField(unique=True, help_text='Слаг - это часть URL-адреса ресурса')

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Мои категории'

class Classroom(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=11, unique=True)
    description = models.TextField(blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название записи')
    slug = models.SlugField(max_length=80, unique=True, verbose_name='URL')
    description = models.TextField(verbose_name='Краткое описание')
    text = models.TextField(verbose_name='Полный текст записи')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Время добавления')
    updated = models.DateTimeField(auto_now=True, verbose_name='Время обновления')
    fixed = models.BooleanField(default=False, verbose_name='Прикреплено')

    class Meta:
        ordering = ['-created']
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

