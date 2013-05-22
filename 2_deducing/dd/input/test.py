from dd import *

import re

# init

case = '<SELECT NAME=priority MULTIPLE SIZE=7>'
circumstances = set( enumerate( case ) )

def circ2str( circumstances, fill = '.' ):
	d = dict( circumstances )
	x = ''.join( d[ i ] if i in d else fill for i in range( len( case ) ) )
	return x

# test

def test( circumstances ):
	test.n += 1
	s = circ2str( circumstances )
	result = FAIL if re.match( '<SELECT.*>', s ) else PASS
	print( '{0:02} Testing "{1}" -> {2}'.format( test.n, s, result ) )
	return result
test.n = 0
