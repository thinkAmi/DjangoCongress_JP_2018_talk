class HandlingExceptionWSGIMiddleware:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        print('[wsgi] called exception handling')
        try:
            response = self.app(environ, start_response)
            print(f'[wsgi] response: {type(response)}')
            return response
        except ValueError:
            print('[wsgi] handled exception')
            start_response('200 OK', [('Content-Type', 'text/plain')])
            return [b"handled exception\n"]


class RaiseExceptionWSGIMiddleware:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        print('[wsgi] raised exception')
        raise ValueError('Oops!')
