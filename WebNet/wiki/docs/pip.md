## Настройка [django](https://www.djangoproject.com/)

`pip install django==4.1.2`

## Настройка [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/install.html)

`pip install django-crispy-forms==1.14.0`

settings:
```python
INSTALLED_APPS = [
    ...,
    'crispy_forms',
]
```
and:
```python
CRISPY_TEMPLATE_PACK = 'uni_form'
```

## Настройка [django-cleanup](https://github.com/un1t/django-cleanup)

`pip install django-cleanup==6.0.0`

settings:
```python
INSTALLED_APPS = [
    ...,
    'django_cleanup.apps.CleanupConfig',  # the package must be the last one,
]
```

## Настройка [pillow](https://pillow.readthedocs.io/en/stable/installation.html#windows-installation)

`pip install pillow==9.2.0`

## Настройка [django-ckeditor](https://github.com/django-ckeditor/django-ckeditor)

`pip install django-ckeditor==6.5.1`

settings:
```python
INSTALLED_APPS = [
    ...,
    'ckeditor',
]
```
and:
```python
CKEDITOR_CONFIG = {
    'default': {
        'width': 'auto',
    },
}
```

## Настройка [django-channels](https://channels.readthedocs.io/en/stable/)

`python -m pip install -U channels==3.0.5`

## Настройка [django-allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)

`pip install django-allauth==0.51.0`

## Настройка [dotenv](https://github.com/theskumar/python-dotenv)

`pip install python-dotenv==0.21.0`

settings:
```python
from pathlib import Path

from dotenv import load_dotenv

# Loading ENV
env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)
```
and:
```python
import os

SECRET_KEY = os.getenv('SECRET_KEY')
```

add file .env to project root:
```
SECRET_KEY = 'your_key'
```

## Настройка [django-braces](https://django-braces.readthedocs.io/en/latest/)

`pip install django-braces==1.15.0`

## Настройка [mkdocs](https://www.mkdocs.org/)

`pip install mkdocs==1.4.0`

## Настройка [mkdocs-awesome-pages-plugin](https://github.com/lukasgeiter/mkdocs-awesome-pages-plugin/)

`pip install mkdocs-awesome-pages-plugin==2.8.0`

## Настройка [mkdocs-material](https://squidfunk.github.io/mkdocs-material/getting-started/)

`pip install mkdocs-material==8.5.6`
