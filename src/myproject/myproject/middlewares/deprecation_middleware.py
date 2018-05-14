from django.utils.deprecation import MiddlewareMixin


class DeprecationMixinDjangoMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print('[mixin] process_request')

    def process_response(self, request, response):
        print('[mixin] process_response')
        return response

    def process_template_response(self, request, response):
        print('[mixin] process_template_response')
        response.context_data['message'] = 'overwrite by deprecation mixin middleware'
        return response
