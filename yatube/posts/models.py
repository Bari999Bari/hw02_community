from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['pk']


class Post(models.Model):
    text = models.TextField(verbose_name='Содержание')
    pub_date = models.DateTimeField(auto_now_add=True,
                                    verbose_name='Дата публикации')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='posts',
                               verbose_name='Автор')
    group = models.ForeignKey(Group,
                              on_delete=models.SET_NULL,
                              related_name='posts',
                              blank=True,
                              null=True,
                              verbose_name='Сообщество')

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Post'
        # плюрал меня устраивает
