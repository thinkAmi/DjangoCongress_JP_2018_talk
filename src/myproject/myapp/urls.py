from django.urls import path

from . import views

urlpatterns = [
    path('hello', views.HelloView.as_view(), name='hello'),
    path('template', views.HelloTemplateView.as_view(), name='hello_template'),
    path('error', views.ExceptionView.as_view(), name='error')
]
