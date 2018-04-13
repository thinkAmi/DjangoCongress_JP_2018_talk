from .base import *


MIDDLEWARE = [
    'myproject.middlewares.process_exception_middleware.ProcessExceptionDjangoMiddleware',
]
