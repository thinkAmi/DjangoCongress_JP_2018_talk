from .base import *

WSGI_APPLICATION = 'myproject.handling_django_exception_wsgi.application'

MIDDLEWARE = [
    'myproject.middlewares.exception_middleware.'
    'RaisingExceptionInProcessTemplateResponseDjangoMiddleware',
]
