class HelloWSGIMiddleware:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        print('[wsgi_middleware] before view')
        response = self.app(environ, start_response)
        print('[wsgi_middleware] after view')
        return response
