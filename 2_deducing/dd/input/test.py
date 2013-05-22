from dd import *

import re

# init

case = '<SELECT NAME=priority MULTIPLE SIZE=7>'
circumstances = set( enumerate( case ) )

# test

def test( circumstances ):
	test.n += 1
	s = circ2str( circumstances, len( case ) )
	result = FAIL if re.match( '<SELECT.*>', s ) else PASS
	print( '{0:02} Testing "{1}" -> {2}'.format( test.n, s, result ) )
	return result
test.n = 0
