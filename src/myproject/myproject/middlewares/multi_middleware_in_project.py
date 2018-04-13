class FirstDjangoMiddlewareInProject:
    def __init__(self, get_response):
        self.get_response = get_response
        print('[prj1] one-time configuration')

    def __call__(self, request):
        print('[prj1] before view')
        response = self.get_response(request)
        print('[prj1] after view')
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        print('[prj1] process view')

    def process_template_response(self, request, response):
        print('[prj1] process template response')
        return response


class SecondDjangoMiddlewareInProject:
    def __init__(self, get_response):
        self.get_response = get_response
        print('[prj2] one-time configuration')

    def __call__(self, request):
        print('[prj2] before view')
        response = self.get_response(request)
        print('[prj2] after view')
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        print('[prj2] process view')

    def process_template_response(self, request, response):
        print('[prj2] process template response')
        return response


class ThirdDjangoMiddlewareInProject:
    def __init__(self, get_response):
        self.get_response = get_response
        print('[prj3] one-time configuration')

    def __call__(self, request):
        print('[prj3] before view')
        response = self.get_response(request)
        print('[prj3] after view')
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        print('[prj3] process view')

    def process_template_response(self, request, response):
        print('[prj3] process template response')
        return response
