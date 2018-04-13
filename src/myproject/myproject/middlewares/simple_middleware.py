class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print(type(get_response))
        # => <class 'function'>

    def __call__(self, request):
        print(type(request))
        # => <class 'django.core.handlers.wsgi.WSGIRequest'>
        response = self.get_response(request)
        print(type(response))
        return response
