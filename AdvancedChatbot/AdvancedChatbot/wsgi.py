from main import app as application

# This file serves as a WSGI adapter for gunicorn
# It exports the FastAPI app as a WSGI application

def wsgi_app(environ, start_response):
    """
    Adapter function to convert ASGI app to WSGI
    This enables FastAPI to work with gunicorn's sync worker
    """
    path = environ.get('PATH_INFO', '')
    method = environ.get('REQUEST_METHOD', 'GET')
    
    if method == 'GET' and path == '/health':
        start_response('200 OK', [('Content-Type', 'application/json')])
        return [b'{"status": "ok"}']
    
    # Serve Swagger UI docs at /docs
    if method == 'GET' and (path == '/docs' or path.startswith('/openapi.json')):
        # Redirect to the main uvicorn server for API docs
        start_response('307 Temporary Redirect', [('Location', 'http://localhost:8000' + path)])
        return [b'Redirecting to API documentation']
    
    # For the /convert endpoint, show a simple HTML form
    if method == 'GET' and path == '/':
        start_response('200 OK', [('Content-Type', 'text/html')])
        return [b'''
        <!DOCTYPE html>
        <html>
        <head>
            <title>MarkItDown Converter</title>
            <link href="https://cdn.replit.com/agent/bootstrap-agent-dark-theme.min.css" rel="stylesheet">
            <style>
                .container { max-width: 600px; margin-top: 50px; }
                .form-group { margin-bottom: 20px; }
            </style>
        </head>
        <body data-bs-theme="dark">
            <div class="container">
                <h1 class="mb-4">MarkItDown Converter</h1>
                <div class="card">
                    <div class="card-body">
                        <p class="card-text">Upload a file to convert it to Markdown format.</p>
                        <p class="card-text">Supported formats include: DOCX, HTML, PDF, and more.</p>
                        <form action="/convert" method="post" enctype="multipart/form-data">
                            <div class="form-group">
                                <label for="file">Select file to upload:</label>
                                <input type="file" class="form-control-file" id="file" name="file" required>
                            </div>
                            <button type="submit" class="btn btn-primary">Convert to Markdown</button>
                        </form>
                    </div>
                </div>
                <p class="mt-3">
                    <small class="text-muted">This service uses the Microsoft MarkItDown library.</small>
                </p>
            </div>
        </body>
        </html>
        ''']
    
    # For other routes, return an error
    start_response('400 Bad Request', [('Content-Type', 'application/json')])
    return [b'{"error": "This endpoint is only accessible through the API"}']

# For gunicorn to run
app = wsgi_app