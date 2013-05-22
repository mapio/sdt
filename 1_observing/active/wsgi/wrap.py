from wsgiref.simple_server import make_server
from werkzeug.debug import DebuggedApplication

from wsgiapp import app

if __name__ == '__main__':
	app = DebuggedApplication( app, evalex = True )
	make_server( '0.0.0.0', 8000, app ).serve_forever()
