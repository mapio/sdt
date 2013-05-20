from re import match

# Funzione universale

def U( f, x ):
	locals = {}
	exec( f, globals(), locals )
	F = next( iter( locals.values() ) )
	return F( x )

# Funzione di curryficazione

def S( f, y ):
	n = match( 'def\s+([^(]+)\s*\(', f ).group( 1 )
	f = f.replace( '\n', '\n\t' )
	g = 'def G( x ):\n\t{0}\n\treturn {1}( x, {2!r} )'.format( f, n, y )
	return g

# Funzioni costruite nella dimostrazione del teorema di Rice

e = 'def E( x, f ): return U( U( f, f ), x )'

m = 'def M( x ): return T( S( e, x ) )'

r = S( e, m )

# Esempio di funzione T

def T( f ):  # funzione che restituisce codice che ha per argomento
	return 'def F( x ):\n\treturn {0!r}'.format( f )

# output di r, U( r, x ) e U( T( r ), x )

print( 'r', '-' * 89, '\n\n', r, '\n' )
print( 'U( r, x )', '-' * 82, '\n\n', U( r, 'x' ), '\n' )
print( 'U( T( r ), x )', '-' * 77, '\n\n', U( T( r ), 'x' ), '\n' )
