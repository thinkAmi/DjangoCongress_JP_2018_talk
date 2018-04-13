"""
WSGI config for myproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from myproject.wsgi_middlewares.handling_exception_middleware import (
    HandlingExceptionWSGIMiddleware, RaiseExceptionWSGIMiddleware
)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")

application = get_wsgi_application()

# 例外ハンドリングする方を最後に呼ぶ
application = RaiseExceptionWSGIMiddleware(application)
application = HandlingExceptionWSGIMiddleware(application)
