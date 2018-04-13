class HelloWSGIMiddleware:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        response = self.app(environ, start_response)
        response[0] += b'Hello, WSGI middleware\n'
        return response
