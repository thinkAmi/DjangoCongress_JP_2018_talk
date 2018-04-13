from django.http import HttpResponse
from myapp.views import HelloTemplateView


class ProcessExceptionDjangoMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print('[process_exception] one-time configuration')

    def __call__(self, request):
        print('[process_exception] before view')
        response = self.get_response(request)
        print('[process_exception] after view')
        return response

    def process_exception(self, request, exception):
        print('[process_exception] hook!')
        print(type(request))
        print(type(exception))
        if request.GET.get('http'):
            print('[process_exception] return HttpResponse')
            return HttpResponse('HttpResponse by process_exception\n')
        elif request.GET.get('template'):
            print('[process_exception] return TemplateResponse')
            return HelloTemplateView(request=request).render_to_response(
                {'message': 'TemplateResponse by process_exception\n'})
        else:
            print('[process_exception] return None')
            return None

    def process_template_response(self, request, response):
        print('[process_exception] hook by template response')
        response.context_data['message'] += 'called process_template_response'
        return response
