from .base import *


MIDDLEWARE = [
    'myproject.middlewares.multi_middleware.FirstDjangoMiddleware',
    'myproject.middlewares.multi_middleware.SecondDjangoMiddleware',
    'myproject.middlewares.multi_middleware.ThirdDjangoMiddleware',
]
