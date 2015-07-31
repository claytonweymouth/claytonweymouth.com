def print_environ(environ, start_response):

	response_body = ['%s: %s' % (key, value) for key, value in sorted(environ.items())]

	response_body = '\n'.join(response_body)
	response_body = response_body.encode('utf-8')

	status = '200 OK'

	response_headers = [('Content-Type', 'text/plain'), ('Content-Length', str(len(response_body)))]

	start_response(status, response_headers)
	return [response_body]

def hello_world(environ, start_response):

	response_body = b'Hello, World!'

	status = '200 OK'

	response_headers = [('Content-Type', 'text/plain'), ('Content-Length', str(len(response_body)))]

	start_response(status, response_headers)
	return [response_body]

def hello_you(environ, start_response):

	response_body = 'Hello, %s!' % environ['dispatcher.args']
	
	response_body= response_body.encode('utf-8')
	
	status = '200 OK'

	response_headers = [('Content-Type', 'text/plain'), ('Content-Length', str(len(response_body)))]

	start_response(status, response_headers)
	return [response_body]