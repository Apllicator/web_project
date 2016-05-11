def app(environ, start_response):
    status = '200'
    header = [('Content-Type', 'text/plain')]
    start_response(status, header)
    body = environ.replace('&', '\n')
    return [body]
