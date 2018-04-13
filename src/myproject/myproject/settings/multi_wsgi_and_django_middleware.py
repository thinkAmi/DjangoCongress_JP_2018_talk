from .base import *

MIDDLEWARE = [
    'myproject.middlewares.multi_middleware.FirstDjangoMiddleware',
    'myproject.middlewares.multi_middleware.SecondDjangoMiddleware',
]

WSGI_APPLICATION = 'myproject.double_wsgi.application'
