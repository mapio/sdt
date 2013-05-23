tot = 0

def add( x ):
	global tot

	tot += x

def value():
	return tot

if __name__ == '__main__': #pragma: no cover
	add( 1 )
	add( 2 )
	print( value() )
