class Player( object ):
	def __init__( self ):
		self.n = 0
	def win( self ):
		self.n += 1
	def victories( self ):
		return self.n

class Tournament( object ):
	def __init__( self, *players ):
		self.players = players
	def wins( self, num_player ):
		self.players[ num_player ].win()
	def winner( self ):
		victories = list( map( lambda x : x.victories(), self.players ) )
		return victories.index( max( victories ) )
