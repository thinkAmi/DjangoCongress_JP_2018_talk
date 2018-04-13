class FirstWSGIMiddleware:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        print('[wsgi1] before view')
        response = self.app(environ, start_response)
        print('[wsgi1] after view')
        return response


class SecondWSGIMiddleware:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        print('[wsgi2] before view')
        response = self.app(environ, start_response)
        print('[wsgi2] after view')
        return response


class ThirdWSGIMiddleware:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        print('[wsgi3] before view')
        response = self.app(environ, start_response)
        print('[wsgi3] after view')
        return response
