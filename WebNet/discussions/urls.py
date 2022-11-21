# -*- coding: utf-8 -*-

from django.urls import path
from .views import UserDiscussionListView, DiscussionDetailView, discussion_create

urlpatterns = [
    path('user/<str:username>/', UserDiscussionListView.as_view(), name='user-discussions-list'),
    path('<slug:slug>/<int:pk>/detail/', DiscussionDetailView.as_view(), name='discussion-detail'),
    path('new/', discussion_create, name='discussion-create'),
]
