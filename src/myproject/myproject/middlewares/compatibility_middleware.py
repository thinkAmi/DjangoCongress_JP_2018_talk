from django.utils.deprecation import MiddlewareMixin


class CompatibilityMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        pass

