import re

from scotch import handlers

class Dispatcher:
		
	def __init__(self, routes=None):
		if routes == None:
			self.routes = []
		else:
			self.routes = routes

	def __call__(self, environ, start_response):
		path = environ.get('PATH_INFO', '').lstrip('/')
		for regex, controller in self.routes:
			match = re.search(regex, path)
			if match is not None:
				environ['dispatcher.args'] = match.groups()
				return controller(environ, start_response)
		return handlers.error_404(environ, start_response)
