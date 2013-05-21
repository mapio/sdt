from wsgiref.simple_server import make_server
from wsgiref.util import request_uri

def app( environ, start_response ):
	if request_uri( environ ).endswith( '/bug' ):
		response = [ this_is_a_bug ]
	else:
		response = [ '{0}: {1}\n'.format( key, value ).encode( 'utf-8' ) for key, value in environ.items() ]
	start_response( '200 OK', [ ( 'Content-type', 'text/plain; charset=utf-8' ) ] )
	return response

if __name__ == '__main__':
	try:
		from werkzeug.debug import DebuggedApplication
		app = DebuggedApplication( app, evalex = True )
		print( 'Running with Werkzeug debugger...' )
	except ImportError:
		pass
	make_server( '0.0.0.0', 8000, app ).serve_forever()
