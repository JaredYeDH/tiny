"""
tiny.py is a practice project that implements the 
most basic possible web framework in Python.
"""

import re

def wsgiref_server(app, host='', port=8080):
	"""Implements a WSGIref server and serves continuously.
	   Can override default host and port if desired."""
	
	from wsgiref.simple_server import make_server

	print 'Starting wsgiref_server.'

	server = make_server(host, port, app)
	server.serve_forever()

def run_app(app):
	"""Runs a given app with a WSGIref server.
	   The server does this by invoking the 'callable' provided by the app.
	   This is to WSGI specs."""

	print 'wsgiref_server is invoking the WSGI callable object.'

	wsgiref_server(app)

# FIX: Implement requests most stably/generalizably (likely in a class).
# TODO: Add handling of POST (and other) requests.

def request_handler(environ, start_response):
	"""The simplest request handler possible. This runs when the client makes
	   a request. The server has gotten the environ dictionary from the client
	   when the client made the request and is passing it to the request handler
	   for parsing and handling the request. The server also provides the
	   start_response function which is called below."""

	http_pattern = re.compile('HTTP_.*')
	
	# TODO: Store the parsed request data in a class.
	# Storing the useful environ data - the headers - in Python variables.
	path = environ.get('PATH_INFO', '')
	method = environ.get('REQUEST_METHOD', '')
	query_string = environ.get('QUERY_STRING', '')
	content_length = environ.get('CONTENT_LENGTH', '')
	http_headers = {k: environ[k] for k in environ if re.match(http_pattern, k)}

	# FIX: Parse queries more cleanly.

	if query_string != '':
		queries = [query.split('=') for query in query_string.split('&')]
		queries = {q[0]: q[1] for q in queries}
	else:
		queries = None

	# FIX: Implement routing more intelligently than a conditional statement.

	if path not in ['/', '/user', '/environ']:
		# Status, headers represent the HTTP response expected by the client.
		status = '404 NOT FOUND'

		# Important that this remains a list as specified by WSGI specs.
		headers = [('Content-type', 'text/plain')]

		# start_response is used to begin the HTTP response.
		# This sends the response headers to the server, which sends to the client.
		start_response(status, headers)
		
		return ['Not found']
	else:
		# Status, headers represent the HTTP response expected by the client.
		status = '200 OK'

		# Important that this remains a list as specified by WSGI specs.
		headers = [('Content-type', 'text/html')]
		
		# start_response is used to begin the HTTP response.
		# This sends the response headers to the server, which sends to the client.
		start_response(status, headers)

		if path == '/user':
			return ['Here\'s the user trying to access: %s' % (environ.get('USER', ''))]
		elif path == '/environ':
			return [environ_string]
		else:
			return ['Hello %s!' % (queries['name'])]

run_app(request_handler)

# TODO: Response

# TODO: Headers

# TODO: Routing

# TODO: Error handling