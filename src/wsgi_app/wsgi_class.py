class HelloWSGI:
    def __call__(self, environ, start_response):
        start_response('200 OK', [('Content-Type', 'text/plain')])
        return [b'Hello, WSGI class\n']
