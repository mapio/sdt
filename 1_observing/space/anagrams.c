#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

#define MAX_WORDS 300000
#define MAX_LENGTH 1000

struct { char *orig, *sig; } word[ MAX_WORDS + 1 ];

int cmp_char( const void *px, const void *py )
{
	char x = *(char *)px, y = *(char *)py;

	if ( x < y ) return -1;
	else if ( x > y ) return 1;
	return 0;
}

int cmp_ind( const void *px, const void *py )
{
	int x = *(int *)px, y = *(int *)py;
	
	return strcmp( word[ x ].sig, word[ y ].sig );
}

int main( int argc, char *argv[] ) {

	int i, j, perm[ MAX_WORDS + 1 ], n = 0, prev, m = argc == 2 ? atoi( argv[ 1 ] ) : 1;
	char buffer[ MAX_LENGTH + 1 ];
	FILE *in, *out;
	
	in = fopen( "/usr/share/dict/words", "r" );
	out = fopen( "anagrams.txt", "w" );

	while ( n < MAX_WORDS && fgets( buffer, MAX_LENGTH, in ) != NULL ) {
		int l = strlen( buffer ) - 1;
		if ( l == 0 ) continue;
		buffer[ l ] = '\0';
		word[ n ].orig = strdup( buffer );
		for ( i = 0; i < l; i++ ) buffer[ i ] = tolower( buffer[ i ] );
		qsort( buffer, l, sizeof( char ), cmp_char );
		word[ n ].sig = strdup( buffer );
		n++;
	}

	for ( i = 0; i < n; i++ ) perm[ i ] = i;
	qsort( perm, n, sizeof( int ), cmp_ind );

	for ( prev = 0, i = 1; i <= n; i++ )
		if ( i == n || strcmp( word[ perm[ prev ] ].sig, word[ perm[ i ] ].sig ) ) {
			if ( i - prev >= m ) {
				for ( j = prev; j < i; j++ ) fprintf( out, "%s\t", word[ perm[ j ] ].orig );
				fprintf( out, "\n" );
			}
			prev = i;
		}

	return 0;
}
