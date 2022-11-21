# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from pytils.translit import slugify
# from django.template.defaultfilters import slugify
# from django.utils.text import slugify

from ckeditor.fields import RichTextField


class Discussion(models.Model):

    class Meta:
        verbose_name = 'Дискуссия'
        verbose_name_plural = 'Дискуссии'

    title = models.CharField(max_length=200, help_text='Не более 200 символов', db_index=True, verbose_name='Заголовок')
    content = RichTextField(max_length=5000, blank=True, null=True, help_text='Не более 5000 символов')
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=50)

    likes_discussion = models.ManyToManyField(User, related_name='discussion_likes', blank=True, verbose_name='Лайки')
    saves_discussions = models.ManyToManyField(
        User, related_name='discussions_save', blank=True, verbose_name='Сохраненные посты пользователя'
    )

    # автозаполнения поля slug на основе поля title (для формы)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Discussion, self).save(*args, **kwargs)

    def total_likes_discussion(self):
        return self.likes_discussion.count()

    def total_saves_discussion(self):
        return self.saves_discussions.count()

    def get_absolute_url(self):
        return reverse('discussion-detail', kwargs={'slug': self.slug, 'pk': self.pk})

    def __str__(self):
        return self.title
