from .base import *


MIDDLEWARE = [
    'myproject.middlewares.process_view_middleware.ProcessViewDjangoMiddleware',
]
