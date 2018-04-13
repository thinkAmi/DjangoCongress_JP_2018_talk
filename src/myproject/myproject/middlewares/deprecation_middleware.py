from django.utils.deprecation import MiddlewareMixin


class DeprecationMixinDjangoMiddleware(MiddlewareMixin):
    def process_template_response(self, request, response):
        print('[mixin] hook!')
        response.context_data['message'] = 'overwrite by deprecation mixin middleware'
        return response
