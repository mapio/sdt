#include <stdio.h>
#include <stdlib.h>

void *xmalloc( size_t size )
{
	void *p = malloc( size );

	if ( p == NULL ) {
		perror	( "xmalloc" );
		exit( -1 );
	}

	return p;
}

int main( void )
{
	char *p = (char *)xmalloc( -1 );

	*p = 3;

	return 0;
}
