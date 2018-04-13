from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView


class HelloView(View):
    def get(self, request, *args, **kwargs):
        print('called: HelloView')
        return HttpResponse('Hello world\n')


class HelloTemplateView(TemplateView):
    template_name = 'hello.html'
    extra_context = {'message': 'hello'}

    def get(self, request, *args, **kwargs):
        print('called: HelloTemplateView')
        return super().get(request, args, kwargs)


class ExceptionView(View):
    def get(self, request, *args, **kwargs):
        print('called: ExceptionView')
        raise ValueError('Oops!')
