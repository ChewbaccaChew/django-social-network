# -*- coding: utf-8 -*-

from django import forms
import datetime


class ContactForm(forms.Form):

    date_creation = forms.DateField(help_text='Заполнить форму можно только в настоящий момент')
    subject = forms.CharField(max_length=100)
    message = forms.CharField(max_length=500)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

    def clean_date_creation(self):
        data = self.cleaned_data['date_creation']
        if data < datetime.date.today():
            raise forms.ValidationError('Форма не действительна, просрочена дата')


# class ContactForm(forms.Form):
#
#     # prefix = 'person'
#     error_css_class = 'error'
#     required_css_class = 'required'
#     email = forms.EmailField(required=True, label_suffix='ccc', label='Введите email', error_messages={'required': 'Пож. введите email'})
#     # url = forms.URLField(initial='http://', label='Your website')
#     title = forms.CharField(required=True, max_length=200, label='Тема сообщения')
#     message = forms.CharField(widget=forms.Textarea, required=True, label='Сообщение')
#     cc_myself = forms.BooleanField(required=False, label='CC myself', widget=forms.CheckboxInput())
#     day = forms.DateField(initial=datetime.date.today, label='Отображается сегодняшнее число')
#     # file = forms.FileField()
