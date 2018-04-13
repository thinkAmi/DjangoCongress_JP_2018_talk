def hello_wsgi(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return [b'Hello, WSGI function\n']
