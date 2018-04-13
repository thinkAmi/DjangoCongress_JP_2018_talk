"""
WSGI config for myproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from myproject.wsgi_middlewares.multi_middleware import (
    FirstWSGIMiddleware, SecondWSGIMiddleware, ThirdWSGIMiddleware
)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")

application = get_wsgi_application()

# 追加
application = FirstWSGIMiddleware(application)
application = SecondWSGIMiddleware(application)
application = ThirdWSGIMiddleware(application)
