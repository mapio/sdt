from random import choice
from pdb import set_trace

def ping():
	ping.count += 1
	print( 'I am pinging for the {0} time...'.format( ping.count ) )
ping.count = 0

def pong():
	pong.count += 1
	print( 'I am poning for the {0} time...'.format( pong.count ) )
pong.count = 0

if __name__ == '__main__':
	try:
		while True:
			choice( [ ping, pong ] )()
	except KeyboardInterrupt:
		set_trace()

