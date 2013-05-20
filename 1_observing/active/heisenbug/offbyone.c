#include <stdio.h>

int main( void )
{
	char b[ 1 ];
	char a = 'a';

#ifndef NDEBUG
	printf( "%p %p\n", &a, b );
#endif

	b[ 1 ] = 'b';
	printf( "%c\n", a );

	return 0;
}
