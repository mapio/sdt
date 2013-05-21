from random import choice
from logging.config import fileConfig

from .ping import ping
from .pong import pong

if __name__ == '__main__':
    fileConfig( 'logging.conf' )
    while True:
            choice( [ ping, pong ] )()
