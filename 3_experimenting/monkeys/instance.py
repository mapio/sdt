# This function will patch an instance of a class adding a given function as if it where a method

def monkey_patch( instance, function ):
	setattr( instance, function.__name__, function.__get__( instance ) )

# A class with just an attribute, but no methods

class ClassWithNoMethods( object ):
	def __init__( self, value ):
		self.value = value

# An instance of such class

instance = ClassWithNoMethods( 'world!' )

# Calling "say" on the instance result in an exception...

try:
	instance.say( 'Hello, ' )
except AttributeError as e:
	print( e )

# ... unless you patch the instance!

def say( self, text ):
	print( text + self.value )

monkey_patch( instance, say )

# Now you can invoke as if the instance had such method

instance.say( 'Hello, ' )
