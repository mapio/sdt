from functools import wraps
from operator import itemgetter

__all__ = [ 'simplify', 'isolate', 'circ2str', 'PASS', 'FAIL', 'UNRESOLVED' ]

PASS, FAIL, UNRESOLVED = 'PASS', 'FAIL', 'UNRESOLVED'

def memoize( test ):
	cache = {}
	@wraps( test )
	def _test( circumstances ):
		_circumstances = frozenset( circumstances )
		if _circumstances in cache: return cache[ _circumstances ]
		result = test( circumstances )
		cache[ _circumstances ] = result
		return result
	return _test

def circ2str( circumstances, size, fill = '.' ):
	d = dict( circumstances )
	x = ''.join( str( d[ i ] ) if i in d else fill for i in range( size ) )
	return x

def split( circumstances, n ):
	length = len( circumstances )
	aslist = sorted( circumstances, key = itemgetter( 0 ) )
	return [ set( aslist[ i * length // n : ( i + 1 ) * length // n ] ) for i in range( n ) ]

def simplify( circumstances, test ):
	test = memoize( test )
	n = 2
	while n >= 2:
		if n > len( circumstances ): break
		subsets = split( circumstances, n )
		for subset in subsets:
			complement = circumstances - subset
			if test( complement ) == FAIL:
				circumstances = complement
				n = max( n - 1, 2 )
				break
		else:
			if n == len( circumstances ): break
			n = min( n * 2, len( circumstances ) )
	return circumstances

def isolate( passing, failing, test ):
	test = memoize( test )
	n = 2
	while n >= 2:
		delta = failing - passing
		if n > len( delta ): break
		deltas = split( delta, n )
		for delta in deltas:
			addition = passing | delta
			removal = failing - delta
			if test( removal ) == FAIL and n == 2:
				failing = removal
				n = 2
				break
			if test( removal ) == PASS:
				passing = removal
				n = 2
				break
			if test( addition ) == FAIL:
				failing = addition
				n = 2
				break
			if test( removal ) == FAIL:
				failing = removal
				n = max( n - 1, 2 )
				break
			if test( addition ) == PASS:
				passing = addition
				n = max( n - 1, 2 )
				break
		else:
			if n == len( delta ): break
			n = min( n * 2, len( delta ) )
	return ( delta, passing, failing )
