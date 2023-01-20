# -*- coding: utf-8 -*-

import pytest
import datetime

from django import forms

from forms_app.forms import ContactForm


# # подготавливаем, что тестируем и данные
# @pytest.mark.parametrize(
#     'date_creation, subject, message, sender, cc_myself, validity',
#     [
#         # рабочий вариант
#         ('2023-01-20', 'Test Subject', 'Test Message', 'django@mail.ru', 'cc_myself', True),
#
#         # date_creation дата на будущие дни
#         ('2023-01-21', 'Test Subject', 'Test Message', 'django@mail.ru', 'cc_myself', False),
#
#         # в email нет собаки
#         ('2023-01-20', 'Test Subject', 'Test Message', 'djangomail.ru', 'cc_myself', False),
#
#     ]
# )
#
# def test_valid_contact_form(date_creation, subject, message, sender, cc_myself, validity):
#     form = ContactForm(data={
#         'date_creation': date_creation,
#         'subject': subject,
#         'message': message,
#         'sender': sender,
#         'cc_myself': cc_myself
#     })
#
#     errors_detail = form.errors.as_data()
#     print(errors_detail)
#
#     assert form.is_valid() is validity


# проверка количества символов
max_length_gt_100 = 'n' * 101
max_length_gt_99 = 'n' * 99


@pytest.mark.parametrize(
    'date_creation, valid_date',
    [
        # дата today
        (datetime.date.today(), True),
        # дата past
        ('2023-01-19', False),
        # дата future
        ('2023-01-21', False),

        ('', False),
        (None, False),
    ]
)
@pytest.mark.parametrize(
    'subject, valid_subject',
    [
        ("Hi, Perez!", True),
        (max_length_gt_100, False),
        (max_length_gt_99, True),
    ]
)
@pytest.mark.parametrize(
    'message, valid_message',
    [
        ("Django system", True),
    ]
)
@pytest.mark.parametrize(
    'sender, valid_sender',
    [
        ('django@mail.ru', True),
    ]
)
@pytest.mark.parametrize(
    'cc_myself, valid_cc_myself',
    [
        ('cc_myself', True),
    ]
)
def test_contact_form(date_creation, subject, message, sender, cc_myself,
                      valid_date, valid_subject, valid_message, valid_sender, valid_cc_myself):
    form = ContactForm(
        data={
            "date_creation": date_creation,
            "subject": subject,
            "message": message,
            "sender": sender,
            "cc_myself": cc_myself
        }
    )

    errors_detail = form.errors.as_data()
    print(errors_detail)

    assert form.is_valid() is (valid_date and valid_subject and valid_message and valid_sender and valid_cc_myself)
