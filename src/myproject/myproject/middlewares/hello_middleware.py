class HelloDjangoMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print('[hello] one-time configuration')

    def __call__(self, request):
        print('[hello] before view')
        response = self.get_response(request)
        print('[hello] after view')
        return response
