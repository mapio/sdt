import nose

from code import *

def test_add():
	add( 1 )
	add( 2 )
	assert value() == 3
	
if __name__ == '__main__':
	nose.main()
