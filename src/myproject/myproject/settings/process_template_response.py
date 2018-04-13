from .base import *


MIDDLEWARE = [
    'myproject.middlewares.process_template_response_middleware.ProcessTemplateResponseDjangoMiddleware',
]
