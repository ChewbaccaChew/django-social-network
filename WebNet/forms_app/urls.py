# -*- coding: utf-8 -*-

from django.urls import path

from . import views

urlpatterns = [
    path('contact/', views.contact_send, name='contact'),
]
