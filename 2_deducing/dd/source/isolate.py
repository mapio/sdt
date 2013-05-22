from operator import itemgetter
from os import remove, devnull
from shutil import copyfile
from subprocess import check_call, check_output, CalledProcessError

from dd import *

DEV_NULL = open( devnull, 'w' )

if __name__  == '__main__':

	# init

	case = [ 0, 1, 2, 3, 4, 5 ]
	case_len = len( case )
	circumstances = set( enumerate( case ) )

	def circ2str( circumstances, fill = '.' ):
		d = dict( circumstances )
		x = ''.join( str( d[ i ] ) if i in d else fill for i in range( case_len ) )
		return x

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
				print( "Applying patch: ", num )
				check_call( "patch adder.c patch.{0}".format( num ) , shell = True, stderr = DEV_NULL, stdout = DEV_NULL )
			check_call( "make adder", shell = True, stderr = DEV_NULL, stdout = DEV_NULL )
		except CalledProcessError:
			result = UNRESOLVED
		else:
			result = PASS if check_output( "./adder", shell = True, stderr = DEV_NULL ) == "OK\n" else FAIL
		print( "Testing", circ2str( circumstances ), result )
		return result

	# isolate

	result = isolate( set(), circumstances, test )
	print( '\nFound: "{0}" = "{2}" - "{1}"'.format( circ2str( result[ 0 ] ), circ2str( result[ 1 ] ), circ2str( result[ 2 ] ) ) )
