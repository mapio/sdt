from logging import getLogger

LOGGER = getLogger( __name__ )

count = 0

def ping():
        global count
        count += 1
        LOGGER.info( 'I am pinging for the %s time...', count )
        if count % 10: LOGGER.warn( 'I am pinging too much!' )
        if count % 100: LOGGER.error( 'I am pinging too much!' )
