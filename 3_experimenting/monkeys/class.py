# This function will patch a class adding a given function as a method

def monkey_patch( class_, function ):
	setattr( class_, function.__name__, function  )

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

# ... unless you patch the class!

def say( self, text ):
	print( text + self.value )

monkey_patch( ClassWithNoMethods, say )

# Now you can invoke the method on the instance (even if it was created before the class got patched)

instance.say( 'Hello, ' )
