from tournament import *	

from ludibrio.stub import Stub
from ludibrio.mock import Mock
from ludibrio.matcher import *

def test_tournament():
	t = Tournament( Player(), Player() )
	t.wins( 1 )
	t.wins( 1 )
	t.wins( 0 )
	assert t.winner() == 1

def test_with_stub():
	with Stub() as first_player:
		first_player.victories() >> 1
	with Stub() as second_player:
		second_player.victories() >> 2
	t = Tournament( first_player, second_player )
	assert t.winner() == 1

def test_with_mock():
	with Mock() as player:
		player.win()
		player.victories() >> 1
	t = Tournament( player )
	t.wins( 0 )
	assert t.winner() == 0

