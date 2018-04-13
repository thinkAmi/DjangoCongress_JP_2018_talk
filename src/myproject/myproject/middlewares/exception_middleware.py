class HandlingExceptionDjangoMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print('[handle] one-time configuration')

    def __call__(self, request):
        print('[handle] before view')
        try:
            response = self.get_response(request)
            print('[handle] after view')
            print(f'[handle] {type(response)}')
        except ValueError:
            print('[handle] handling by django middleware')
            response = None
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        print('[handle] process view')

    def process_template_response(self, request, response):
        print('[handle] process template response')
        return response

    def process_exception(self, request, exception):
        print('[handle] called process_exception')


class RaisingExceptionInCallDjangoMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print('[call] one-time configuration')

    def __call__(self, request):
        print('[call] before view')
        raise ValueError('raised by __call__')


class RaisingExceptionInProcessViewDjangoMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print('[view] one-time configuration')

    def __call__(self, request):
        print('[view] before view')
        return self.get_response(request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        print('[view] process view')
        raise ValueError('raised by process_view')


class RaisingExceptionInProcessTemplateResponseDjangoMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print('[template] one-time configuration')

    def __call__(self, request):
        print('[template] before view')
        return self.get_response(request)

    def process_template_response(self, request, response):
        print('[template] process template response')
        raise ValueError('raised by process_template_response')


class RaisingExceptionInProcessExceptionDjangoMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print('[exception] one-time configuration')

    def __call__(self, request):
        print('[exception] before view')
        return self.get_response(request)

    def process_exception(self, request, exception):
        print('[exception] called process_exception')
        raise ValueError('raised by process_exception')
