def error_404(environ, start_response):

	response_body = b'404 NOT FOUND'

	status = '404 NOT FOUND'

	response_headers = [('Content-Type', 'text/plain'), ('Content-Length', str(len(response_body)))]

	start_response(status, response_headers)
	return [response_body]

def error_405(environ, start_response):

	response_body = b'405 METHOD NOT ALLOWED'

	status = '05 METHOD NOT ALLOWED'

	response_headers = [('Content-Type', 'text/plain'), ('Content-Length', str(len(response_body)))]

	start_response(status, response_headers)
	return [response_body]