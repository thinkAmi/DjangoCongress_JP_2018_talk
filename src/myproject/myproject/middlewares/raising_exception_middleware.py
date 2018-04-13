class RaisingExceptionDjangoMiddlewareInProject:
    def __init__(self, get_response):
        self.get_response = get_response
        print('[project] one-time configuration (raise Exception)')

    def __call__(self, request):
        raise ValueError('raised in project middleware')
