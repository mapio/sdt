from random import shuffle
from time import sleep
from timeit import Timer

from qsort import qsort, rearrange

class HeavySetItem( object ):
	def __init__( self, data, weight ):
		global obj
		obj = self
		self.data = list( range( n ) )
		shuffle( self.data )
		self.weight = weight
	def __getitem__( self, key ):
		return self.data[ key ]
	def __setitem__( self, key, value ):
		self.data[ key ] = value
		sleep( self.weight )
	def __len__( self ):
		return len( self.data )

def normal():
	qsort( obj )

def insitu():
	perm = list( range( len( obj ) ) )
	qsort( perm, key = lambda i : obj[ i ] )
	rearrange( obj, perm )

def measure( func, n, w ):
	N = 3
	t = Timer( '{0}()'.format( func ), 'from __main__ import {0},HeavySetItem\nHeavySetItem({1},{2})'.format( func, n, w ) )
	return sum( t.repeat( N, 1 ) ) / N

if __name__ == '__main__':
	w = 0.0001
	for n in range( 50, 1000, 50 ):
		print( n, measure( 'normal', n, w ), measure( 'insitu', n, w ) )
