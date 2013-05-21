from random import choice
from pdb import set_trace

from pingpong import ping, pong

if __name__ == '__main__':
	try:
		while True:
			choice( [ ping, pong ] )()
	except KeyboardInterrupt:
		set_trace()

