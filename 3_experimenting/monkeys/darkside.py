def mp_class( cls ):
	def mp( func ):
		setattr( cls, func.__name__, func )
		return func
	return mp

def mp_i( instance ):
	def mp( func ):
		setattr( instance, func.__name__, func.__get__( instance ) )
		return func
	return mp

class WithoutMethods( object ):
	def __init__( self, value ):
		self.value = value

a = WithoutMethods( 'world!' )
b = WithoutMethods( 'world!' )

@mp_i( b )
def instance_say( self, text ):
	print( text + self.value )

try:
	a.class_say( 'Hello, ' )
except AttributeError as e:
	print( e )

@mp_class( WithoutMethods )
def class_say( self, text ):
	print( text + self.value )

try:
	b.class_say( 'Hello, ' )
except AttributeError as e:
	print( e )

try:
	a.instance_say( 'Hello, ' )
except AttributeError as e:
	print( e )

try:
	b.instance_say( 'Hello, ' )
except AttributeError as e:
	print( e )
