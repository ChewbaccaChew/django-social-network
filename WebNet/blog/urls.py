# -*- coding: utf-8 -*-

from django.urls import path, re_path
from .views import UserPostListView

urlpatterns = [
    path('posts/user/<str:username>/', UserPostListView.as_view(), name='user-posts-list'),
]
