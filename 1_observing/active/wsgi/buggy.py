from wsgiref.simple_server import make_server

from wsgiapp import app

if __name__ == '__main__':
	make_server( '0.0.0.0', 8000, app ).serve_forever()
