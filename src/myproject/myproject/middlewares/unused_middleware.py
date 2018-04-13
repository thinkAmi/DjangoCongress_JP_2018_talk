from django.core.exceptions import MiddlewareNotUsed


class UnusedDjangoMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print('[unused] one-time configuration')
        # MiddlewareNotUsed例外を発生させるのは、__init__の中
        # もし__call__()などの場合、一般的な例外として扱われてしまう
        raise MiddlewareNotUsed

    def __call__(self, request):
        print('[unused] before view')
        response = self.get_response(request)
        print('[unused] after view')
        return response

    def process_template_response(self, request, response):
        print('[unused] hook!')
        response.context_data['message'] = 'overwrite by unused'
        return response
