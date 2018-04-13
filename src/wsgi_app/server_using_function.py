from wsgiref.simple_server import make_server

from wsgi_function import hello_wsgi

if __name__ == '__main__':
    server = make_server('', 15000, hello_wsgi)
    print('Serving on port 15000...')
    server.serve_forever()
