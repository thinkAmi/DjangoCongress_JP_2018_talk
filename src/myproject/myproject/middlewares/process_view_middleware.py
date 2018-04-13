from django.http import HttpResponse


class ProcessViewDjangoMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print('[process_view] one-time configuration')

    def __call__(self, request):
        print('[process_view] before view')
        response = self.get_response(request)
        print('[process_view] after view')
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        print('[process_view] hook!')
        print(type(request))
        print(type(view_func))
        print(type(view_args))
        print(type(view_kwargs))
        if not request.GET.get('foo'):
            return HttpResponse('overwrite by process_view\n')
