# -*- coding: utf-8 -*-

from django.urls import path, re_path
from .views import UserPostListView, PostCreateView, PostDetailView

urlpatterns = [
    path('posts/user/<str:username>/', UserPostListView.as_view(), name='user-posts-list'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<slug:slug>/<int:pk>/detail/', PostDetailView.as_view(), name='post-detail'),
]
