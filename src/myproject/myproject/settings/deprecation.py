from .base import *


MIDDLEWARE = [
    'myproject.middlewares.deprecation_middleware.DeprecationMixinDjangoMiddleware',
]
