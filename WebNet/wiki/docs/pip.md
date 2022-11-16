## Настройка [django](https://www.djangoproject.com/)

`pip install django==4.1.2`


## Настройка [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/install.html)

`pip install django-crispy-forms==1.14.0`

settings.py:
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

settings.py:
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

settings.py:
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

settings.py:
```python
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    ...,
    'channels',  # this
)
```
and:
```python
ASGI_APPLICATION = 'WebNet.routing.application'

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer'
    },
}
```

add file routing.py to configuration package (WebNet/WebNet/):
```python
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chat.routing

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})
```


## Настройка [django-allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)

`pip install django-allauth==0.51.0`

settings.py:
```python
AUTHENTICATION_BACKENDS = [
    ...,
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
    ...,
]
```
and:
```python
INSTALLED_APPS = [
    ...,
    'django.contrib.auth',
    'django.contrib.messages',
    'django.contrib.sites',  # this

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.google',
    ...,
]

SITE_ID = 1
```
and:
```python
# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    },
    'github': {
        'SCOPE': [
            'user',
            'repo',
            'read:org',
        ],
    }
}
```

urls.py:
```python
from django.urls import include

urlpatterns = [
    ...,
    path('accounts/', include('allauth.urls')),
    ...,
]
```


## Настройка [dotenv](https://github.com/theskumar/python-dotenv)

`pip install python-dotenv==0.21.0`

settings.py:
```python
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


## Настройка [django-debug-toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/)

`python -m pip install django-debug-toolbar==3.7.0`

settings.py:
```python
INSTALLED_APPS = [
    ...,
    'debug_toolbar',
    ...,
]
```
and:
```python
MIDDLEWARE = [
    ...,
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    ...,
]
```
and:
```python
INTERNAL_IPS = [
    ...,
    '127.0.0.1',
    ...,
]
```

urls.py:
```python
urlpatterns = [
    ...,
    path('__debug__/', include('debug_toolbar.urls')),
]
```
or:
```python
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
```


## Настройка [jupyter-notebook](https://jupyter.org/install#jupyter-notebook)

`pip install notebook==6.4.12`

хз че это:
settings.py:
```python
# в производстве убрать!
os.environ['DJANGO_ALLOW_ASYNC_UNSAFE'] = 'True'
```

show notebook settings: `python -m pip show notebook`
run the notebook: `python manage.py shell_plus --notebook`

[jupyter-notebooks-themes](https://github.com/dunovank/jupyter-themes#install-with-pip)

`pip install jupyterthemes`

list available themes
onedork | grade3 | oceans16 | chesterish | monokai | solarizedl | solarizedd
`jt -l`

select theme...
`jt -t chesterish`

restore default theme
NOTE: Need to delete browser cache after running jt -r
If this doesn't work, try starting a new notebook session.
`jt -r`

[jupyter autocomplete](https://github.com/codota/jupyter-tabnine) - это не использовал

[nbextensions](https://www.cnblogs.com/qiuxirufeng/p/9609031.html):
установка nbextensions:
`pip install jupyter_contrib_nbextensions`
`jupyter contrib nbextension install --user`

установка nbextensions_configurator:
`pip install jupyter_nbextensions_configurator`
`jupyter nbextensions_configurator enable --user`

поставить галочку на Hinterland в Nbextensions
если на странице нет элемента Hinterland или она неполная:
`jupyter contrib nbextension install --user --skip-running-check`


## Настройка [django-extensions](https://django-extensions.readthedocs.io/en/latest/#)

`pip install django-extensions==3.2.1`

settings.py:
```python
INSTALLED_APPS = [
    ...,
    'django_extensions',
]
```


## Настройка [django-taggit](https://django-taggit.readthedocs.io/en/latest/)

`pip install django-taggit==3.0.0`



## Настройка [pytest-django](https://pytest-django.readthedocs.io/en/latest/)

`pip install pytest-django==4.5.2`

add file pytest.ini to project root:
```
# -- FILE: pytest.ini (or tox.ini)
[pytest]
DJANGO_SETTINGS_MODULE = your_project.settings
# -- recommended but optional:
python_files = tests.py test_*.py *_tests.py
```

запуск всех тестов: `pytest`
запуск тестов находящихся по пути path: `pytest path`
запуск всех тестов в модуле test_some_function: `pytest test_some_function.py`
запуск функции test_one в модуле test_some_function: `pytest test_some_function.py::test_one`


## Настройка [pylint](https://github.com/PyCQA/pylint)

`pip install pylint==2.15.5`
