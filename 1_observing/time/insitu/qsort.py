def _part( a, f, t, key ):
	i = f
	j = t - 2
	pivot = key( a[ t - 1 ] )
	while True:
		while key( a[ i ] ) < pivot: i += 1
		while key( a[ j ] ) >= pivot and j > f: j -= 1
		if i >= j: break
		a[ i ], a[ j ] = a[ j ], a[ i ]
	a[ t - 1 ], a[ i ] = a[ i ], a[ t - 1 ]
	return i

def _qsort( a, f, t, key ):
	if f + 1 >= t: return
	p = _part( a, f, t, key )
	_qsort( a, f, p, key )
	_qsort( a, p + 1, t, key )

def qsort( a, key = lambda x : x ):
	_qsort( a, 0, len( a ), key )

def rearrange( obj, perm ):
	for i in range( len( perm ) ):
		if perm[ i ] > 0: # start perm cycle
			first_obj, j = obj[ i ], i
			while True:
				p = perm[ j ]
				perm[ j ] = -1
				if p == i: # end perm cycle
					obj[ j ] = first_obj # [old] p -> j
					break
				obj[ j ], j = obj[ p ], p # p -> j
