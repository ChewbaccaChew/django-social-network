from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import Discussion
from .forms import DiscussionCreateForm


class UserDiscussionListView(ListView):
    # Модель Discussion в model.py
    model = Discussion

    # Имя шаблона html
    template_name = 'discussions/user_discussions.html'

    def get_context_data(self, **kwargs):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        queryset = Discussion.objects.filter(author=user)
        context = super().get_context_data(**kwargs)
        context['discussion_user_list'] = queryset.order_by('-date_created')
        return context


class DiscussionDetailView(DetailView):
    model = Discussion
    template_name = 'discussions/discussion_detail.html'
    context_object_name = 'discussion_detail'


@login_required
def discussion_create(request):
    if request.method == 'POST':  # если запрос POST, тогда обрабатываем форму
        form = DiscussionCreateForm(request.POST, request.FILES)

        if form.is_valid():
            new_discussion = form.save(commit=False)
            new_discussion = request.user
            new_discussion.save()
            return redirect(new_discussion.get_absolute_url())

    else:
        form = DiscussionCreateForm()

    return render(request, 'discussions/create_form.html', {'form': form})
