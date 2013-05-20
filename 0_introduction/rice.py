from re import match
from sys import version_info, exit

if version_info.major != 3: exit( 'Please run with ptyhon3!' )

# Universal funcition

def U( f, x ):
	locals = {}
	exec( f, globals(), locals )
	F = next( iter( locals.values() ) )
	return F( x )

# Curryfication function

def S( f, y ):
	n = match( 'def\s+([^(]+)\s*\(', f ).group( 1 )
	f = f.replace( '\n', '\n\t' )
	g = 'def G( x ):\n\t{0}\n\treturn {1}( x, {2!r} )'.format( f, n, y )
	return g

# Functions needed in the proof of Rice Theorem

e = 'def E( x, f ): return U( U( f, f ), x )'

m = 'def M( x ): return T( S( e, x ) )'

r = S( e, m )

# Example of funcion T

def T( f ):  # functions that returns the source code given as argument
	return 'def G( x ):\n\treturn {0!r}'.format( f )

# output of r, U( r, x ) e U( T( r ), x ) (should be all identical)

print( 'r', '-' * 89, '\n\n', r, '\n' )
print( 'U( r, x )', '-' * 82, '\n\n', U( r, 'x' ), '\n' )
print( 'U( T( r ), x )', '-' * 77, '\n\n', U( T( r ), 'x' ), '\n' )
