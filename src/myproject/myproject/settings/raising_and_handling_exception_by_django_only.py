from .base import *


MIDDLEWARE += [
    'myproject.middlewares.handling_exception_middleware.HandlingExceptionDjangoMiddlewareInProject',
    'myproject.middlewares.raising_exception_middleware.RaisingExceptionDjangoMiddlewareInProject',
    # 'myproject.middlewares.raising_exception_middleware.RaisingExceptionDjangoMiddlewareInProject',
]
