from django.contrib.auth import get_user_model
from django.db import models
from constants import m_length
from core.models import BaseModel, BaseTitle


User = get_user_model()


class Location(BaseModel):
    """Местоположение"""

    name = models.CharField(m_length, verbose_name='Название места')

    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'


class Category(BaseModel, BaseTitle):
    """Категория"""

    description = models.TextField(verbose_name='Описание')
    slug = models.SlugField(verbose_name='Идентификатор',
                            unique=True,
                            help_text=(
                                'Идентификатор страницы для URL; '
                                'разрешены символы латиницы, '
                                'цифры, дефис и подчёркивание.'
                            ),)

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Post(BaseModel, BaseTitle):

    def get_published_posts(self, cls):
        return cls.objects.select_related(
            "category",
            "location",
            "author",
        ).filter

    text = models.TextField(verbose_name='Текст')
    pub_date = models.DateTimeField(verbose_name='Дата и время публикации',
                                    help_text=(
                                        'Если установить дату и время '
                                        'в будущем — можно делать отложенные '
                                        'публикации.'),)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор публикации',
        related_name='posts',
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Местоположение',
        related_name='posts',
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='posts',
        verbose_name='Категория',
    )

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'

    def str(self):
        return self.title

    def get_published_categories(self, cls):
        return cls.objects.filter(
            is_published=True
        )
