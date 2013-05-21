from logging import getLogger

LOGGER = getLogger( __name__ )

count = 0

def pong():
        global count
        count += 1
        LOGGER.info( 'I am ponging for the %s time...', count )
        if count % 100: LOGGER.error( 'I am ponging too much!' )
