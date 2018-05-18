from .base import *


MIDDLEWARE = [
    'myproject.middlewares.process_view_template_middleware.ProcessViewTemplateDjangoMiddleware',
]
