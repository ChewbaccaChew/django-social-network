# -*- coding: utf-8 -*-
import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError

from .forms import ContactForm


def contact_send(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            date_creation = form.cleaned_data['date_creation']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            recipients = ['web-webovich@mail.ru']
            cc_myself = form.cleaned_data['cc_myself']

            if cc_myself:
                recipients.append(message)
            else:
                date_created_today = datetime.date.today()
                form = ContactForm(initial={'date_creation': date_created_today})

            try:
                send_mail(subject, message, sender, recipients, date_creation)

            except BadHeaderError:
                return HttpResponse('Неверное заполнение')

            form = ContactForm()
            messages.success(request, 'Сообщение успешно отправлено!')

        else:
            messages.error(request, 'Error')

    return render(request, 'forms_app/email.html', {'form': form})
