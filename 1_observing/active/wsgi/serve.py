from werkzeug.serving import run_simple

from wsgiapp import app

if __name__ == '__main__':
	run_simple( '0.0.0.0', 8000, app, use_debugger = True, use_reloader = True )
