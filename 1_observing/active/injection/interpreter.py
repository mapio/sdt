from random import choice
from code import interact

from pingpong import ping, pong

if __name__ == '__main__':
	try:
		while True:
			choice( [ ping, pong ] )()
	except KeyboardInterrupt:
		interact( local = locals() )
