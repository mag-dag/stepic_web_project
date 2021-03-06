# gunicorn configuration file for "hello" python application

bind = "0.0.0.0:8080"
workers = 1

def app(environ, start_response):
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    start_response(status, headers)
    body = [bytes(i + '\n', 'ascii') for i in environ['QUERY_STRING'].split('&')]    
    return body
