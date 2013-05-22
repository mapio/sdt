import re

from dd import *

if __name__ == '__main__':

	# init

	case = '<SELECT NAME=priority MULTIPLE SIZE=7>'
	case_len = len( case )
	circumstances = set( enumerate( case ) )

	def circ2str( circumstances, fill = '.' ):
		d = dict( circumstances )
		x = ''.join( d[ i ] if i in d else fill for i in range( case_len ) )
		return x

	# test

	def test( circumstances ):
		global n
		n += 1
		s = circ2str( circumstances )
		result = FAIL if re.match( '<SELECT.*>', s ) else PASS
		#if 0 < len( circumstances ) < 20: result = UNRESOLVED
		print( '{0:02} Testing "{1}" -> {2}'.format( n, s, result ) )
		return result

	# symplify

	n = 0
	res = simplify( circumstances, test )
	print( 'Found: "{0}"'.format( circ2str( res, '' ) ) )

	# isolate

	n = 0
	res = isolate( set(), circumstances, test )
	print( '\nFound: "{0}" = "{2}" - "{1}"'.format( circ2str( res[0], '' ), circ2str( res[1], '' ), circ2str( res[2], '' ) ) )
