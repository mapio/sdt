from operator import itemgetter
from os import remove, devnull
from shutil import copyfile
from subprocess import check_call, check_output, CalledProcessError

from dd import *

DEV_NULL = open( devnull, 'w' )

# init

case = [ 0, 1, 2, 3, 4, 5 ]
circumstances = set( enumerate( case ) )

# test

def test( circumstances ):
	patches = sorted( map( itemgetter( 1 ), circumstances ) )
	try:
		remove( 'adder' )
	except OSError:
		pass
	copyfile( 'orig.c', 'adder.c' )
	try:
		for num in patches:
			check_call( "patch adder.c patch.{0}".format( num ) , shell = True, stderr = DEV_NULL, stdout = DEV_NULL )
		check_call( "make adder", shell = True, stderr = DEV_NULL, stdout = DEV_NULL )
	except CalledProcessError:
		result = UNRESOLVED
	else:
		result = PASS if check_output( "./adder", shell = True, stderr = DEV_NULL ) == "OK\n" else FAIL
	print( '{0:02} Testing "{1}" -> {2}'.format( test.n, circ2str( circumstances, len( case ) ), result ) )
	return result
