from django.shortcuts import render
from django.views.generic import ListView

from .models import Post


class UserPostListView(ListView):
    model = Post
    # template_name = ''
    # objects, model_постфикс, наш вариант
    context_object_name = ''
