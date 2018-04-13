from .base import *


MIDDLEWARE = [
    'myproject.middlewares.multi_middleware_in_project.FirstDjangoMiddlewareInProject',
    'myapp.middlewares.multi_middleware_in_app.FirstDjangoMiddlewareInApp',
    'myproject.middlewares.multi_middleware_in_project.SecondDjangoMiddlewareInProject',
    'myapp.middlewares.multi_middleware_in_app.SecondDjangoMiddlewareInApp',
    'myproject.middlewares.multi_middleware_in_project.ThirdDjangoMiddlewareInProject',
    'myapp.middlewares.multi_middleware_in_app.ThirdDjangoMiddlewareInApp',
]
