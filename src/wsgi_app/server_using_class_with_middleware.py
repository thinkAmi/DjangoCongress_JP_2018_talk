from wsgiref.simple_server import make_server

from wsgi_class import HelloWSGI
from wsgi_middleware import HelloWSGIMiddleware

if __name__ == '__main__':
    wsgi_app = HelloWSGI()
    app_with_middleware = HelloWSGIMiddleware(wsgi_app)
    server = make_server('', 15002, app_with_middleware)
    print('Serving on port 15002...')
    server.serve_forever()
