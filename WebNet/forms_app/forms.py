# -*- coding: utf-8 -*-

import datetime

from django import forms


class ContactForm(forms.Form):

    date_creation = forms.DateField(initial=datetime.date.today, help_text='Заполнить форму можно только в настоящий момент')
    subject = forms.CharField(max_length=100)
    message = forms.CharField(max_length=500)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField()

    def clean_date_creation(self):
        date = self.cleaned_data['date_creation']
        if date != datetime.date.today():
            raise forms.ValidationError('Дата должна быть сегодняшняя')
        return date
