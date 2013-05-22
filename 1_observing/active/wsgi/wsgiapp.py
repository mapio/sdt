from wsgiref.util import request_uri

def app( environ, start_response ):
	if request_uri( environ ).endswith( '/bug' ):
		response = [ this_is_a_bug ]
	else:
		response = [ '{0}: {1}\n'.format( key, value ).encode( 'utf-8' ) for key, value in environ.items() ]
	start_response( '200 OK', [ ( 'Content-type', 'text/plain; charset=utf-8' ) ] )
	return response
