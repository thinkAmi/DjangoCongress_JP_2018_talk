class FirstDjangoMiddlewareInApp:
    def __init__(self, get_response):
        self.get_response = get_response
        print('[app1] one-time configuration')

    def __call__(self, request):
        print('[app1] before request')
        response = self.get_response(request)
        print('[app1] after request')
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        print('[app1] process view')

    def process_template_response(self, request, response):
        print('[app1] process template response')
        return response


class SecondDjangoMiddlewareInApp:
    def __init__(self, get_response):
        self.get_response = get_response
        print('[app2] one-time configuration')

    def __call__(self, request):
        print('[app2] before request')
        response = self.get_response(request)
        print('[app2] after request')
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        print('[app2] process view')

    def process_template_response(self, request, response):
        print('[app2] process template response')
        return response


class ThirdDjangoMiddlewareInApp:
    def __init__(self, get_response):
        self.get_response = get_response
        print('[app3] one-time configuration')

    def __call__(self, request):
        print('[app3] before request')
        response = self.get_response(request)
        print('[app3] after request')
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        print('[app3] process view')

    def process_template_response(self, request, response):
        print('[app3] process template response')
        return response
