from dd import *

from test import *

if __name__ == '__main__':

	test.n = 0
	res = simplify( circumstances, test )
	print( 'Found: "{0}"'.format( circ2str( res, '' ) ) )
