class FirstDjangoMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print('[django1] one-time configuration')

    def __call__(self, request):
        print('[django1] before view')
        response = self.get_response(request)
        print('[django1] after view')
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        print('[django1] process view')

    def process_template_response(self, request, response):
        print('[django1] process template response')
        return response


class SecondDjangoMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print('[django2] one-time configuration')

    def __call__(self, request):
        print('[django2] before view')
        response = self.get_response(request)
        print('[django2] after view')
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        print('[django2] process view')

    def process_template_response(self, request, response):
        print('[django2] process template response')
        return response


class ThirdDjangoMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print('[django3] one-time configuration')

    def __call__(self, request):
        print('[django3] before view')
        response = self.get_response(request)
        print('[django3] after view')
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        print('[django3] process view')

    def process_template_response(self, request, response):
        print('[django3] process template response')
        return response
