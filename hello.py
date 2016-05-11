def app(environ, start_response):
    status = '200'
    header = [('Content-Type', 'text/plain')]
    start_response(status, header)
    body = environ['QUERY_STRING'].replace('&', '\n')
    return [body]
