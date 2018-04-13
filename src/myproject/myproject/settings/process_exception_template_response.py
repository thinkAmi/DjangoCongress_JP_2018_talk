from .base import *


MIDDLEWARE = [
    # process_exception
    'myproject.middlewares.process_exception_middleware'
    '.ProcessExceptionDjangoMiddleware',

    # process_template_response
    'myproject.middlewares.process_template_response_middleware'
    '.ProcessTemplateResponseDjangoMiddleware',

]
