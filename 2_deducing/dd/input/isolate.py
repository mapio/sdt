from dd import *

from test import *

if __name__ == '__main__':

	test.n = 0
	res = isolate( set(), circumstances, test )
	size = len( case )
	print( '\nFound: "{0}" = "{2}" - "{1}"\n'.format( circ2str( res[0], size, '' ), circ2str( res[1], size, '' ), circ2str( res[2], size, '' ) ) )
