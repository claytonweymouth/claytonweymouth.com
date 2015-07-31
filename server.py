from scotch import applications, handlers, dispatcher

HOST = 'localhost'
PORT = 8080

routes = [
	('^$',              applications.hello_world),
	('environ/?(.*)$',  applications.print_environ),
	('hello/?(.*)$',    applications.hello_you),
]

dispatch = dispatcher.Dispatcher(routes)

if __name__ == "__main__":
    from wsgiref.simple_server import make_server
    server = make_server(HOST, PORT, dispatch)
    print('Starting up HTTP server on port %i...' % PORT)
    server.serve_forever()
