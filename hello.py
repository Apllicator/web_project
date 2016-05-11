def app(environ, start_response):
    status = '200'
    header = [('Content-Type', 'text/plain')]
    status_response(status, header)
    body = ''
    for i in environ.split('&'):
        body += i + '\n'
    return body
