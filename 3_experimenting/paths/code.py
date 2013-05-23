def path( a, b ):
	if a:
		x = 1
	else:
		x = 0
	if b:
		y = 2 * x
	else:
		y = 2 / x

def branch( x ):
	y = 2
	while x > 0:
		x -= 1
		y //= 2
	z = 1 / y
