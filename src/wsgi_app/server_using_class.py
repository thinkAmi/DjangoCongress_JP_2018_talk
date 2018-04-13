from wsgiref.simple_server import make_server

from wsgi_class import HelloWSGI

if __name__ == '__main__':
    server = make_server('', 15001, HelloWSGI())
    print('Serving on port 15001...')
    server.serve_forever()
