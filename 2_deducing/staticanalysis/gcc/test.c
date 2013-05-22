#include <stdio.h>

int main( void ) {

	int b[ 0 ], x, y;

	b[ 1 ] = 'a';
	printf( "I am for sure a bug %s" );
	printf( "And I am the second one %s", x );

	return 1 + b[ 1 ];
}
