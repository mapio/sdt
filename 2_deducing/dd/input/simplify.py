from dd import *

from test import *

if __name__ == '__main__':

	test.n = 0
	res = simplify( circumstances, test )
	print( '\nFound: "{0}"\n'.format( circ2str( res, len( case ), '' ) ) )
