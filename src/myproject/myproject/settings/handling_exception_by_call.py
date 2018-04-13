from .base import *


MIDDLEWARE = [
    'myproject.middlewares.exception_middleware.HandlingExceptionDjangoMiddleware',
    'myproject.middlewares.exception_middleware.RaisingExceptionInCallDjangoMiddleware',
]
