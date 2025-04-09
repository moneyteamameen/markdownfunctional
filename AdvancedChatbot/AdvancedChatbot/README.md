# Document Content API

A RESTful API for extracting text content from various document formats. This service uses the MarkItDown library to process documents and return their content as plain text.

## Features

- Extract text content from documents in various formats (HTML, PDF, etc.)
- Simple API with straightforward endpoints
- Health check endpoint for monitoring
- Detailed error reporting

## API Endpoints

### GET /

Get information about the API, including available endpoints.

**Response:**
```json
{
  "name": "Document Content API",
  "version": "1.0.0",
  "description": "Extract content from various document formats",
  "endpoints": {
    "/extract": {
      "method": "POST",
      "description": "Extract content from an uploaded document",
      "params": "file (multipart/form-data)"
    },
    "/health": {
      "method": "GET",
      "description": "API health check"
    }
  }
}
```

### POST /extract

Extract content from an uploaded document.

**Request:**
- Content-Type: multipart/form-data
- Body: file (the document to extract content from)

**Response:**
```json
{
  "filename": "document.html",
  "content": "The extracted text content...",
  "format": "text/plain"
}
```

**Error Responses:**
- 400 Bad Request: Missing file or filename
- 415 Unsupported Media Type: Unsupported file format
- 500 Internal Server Error: Conversion error or unexpected error

### GET /health

Check the health of the API.

**Response:**
```json
{
  "status": "ok"
}
```

## Testing the API

You can use the included `test_api.py` script to test the API:

```bash
# Test with the default HTML test document
python test_api.py

# Test with a custom document
python test_api.py --file path/to/document.pdf
```

The script will generate a text file with the extracted content.

## Running the API

The API is designed to run with Gunicorn:

```bash
gunicorn --bind 0.0.0.0:5000 --reuse-port --reload main:app
```

## Dependencies

- Flask: Web framework for the API
- MarkItDown: Document conversion library
- Gunicorn: WSGI HTTP Server

## Notes

- The API currently returns the document content in its original format, not converted to Markdown
- For HTML documents, it returns the HTML content
- This is a limitation of the current MarkItDown library implementation