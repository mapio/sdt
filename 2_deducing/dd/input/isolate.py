from dd import *

from test import *

if __name__ == '__main__':

	test.n = 0
	res = isolate( set(), circumstances, test )
	print( '\nFound: "{0}" = "{2}" - "{1}"'.format( circ2str( res[0], '' ), circ2str( res[1], '' ), circ2str( res[2], '' ) ) )
