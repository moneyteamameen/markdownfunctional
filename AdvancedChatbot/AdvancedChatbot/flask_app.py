"""
Document API - A RESTful API for extracting text from documents.
This service provides endpoints for document content extraction using the markitdown library.
"""

import logging
import io
import os
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from markitdown import MarkItDown, StreamInfo, UnsupportedFormatException, FileConversionException

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)
logger = logging.getLogger(__name__)

# Initialize Flask application
app = Flask(__name__)

# Initialize the MarkItDown converter
try:
    md_converter = MarkItDown()
    logger.info("MarkItDown converter initialized successfully")
except Exception as e:
    logger.error(f"Failed to initialize MarkItDown converter: {str(e)}")
    raise

@app.route('/')
def index():
    """Information about the API"""
    logger.info("API information requested")
    return jsonify({
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
    })

@app.route('/extract', methods=['POST'])
def extract_content():
    """
    Extract content from an uploaded document.
    """
    if 'file' not in request.files:
        logger.error("No file part in the request")
        return jsonify({"detail": "No file part in the request"}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        logger.error("No file selected")
        return jsonify({"detail": "No file selected"}), 400
    
    logger.info(f"Received file: {file.filename}, content-type: {file.content_type}")
    
    try:
        # Read file content
        file_content = file.read()
        
        # Create byte stream from file content
        file_stream = io.BytesIO(file_content)
        
        # Extract filename and extension
        filename = secure_filename(file.filename)
        extension = os.path.splitext(filename)[1].lower() if filename else ""
        content_type = file.content_type
        
        logger.info(f"Processing file: {filename}, extension: {extension}, content-type: {content_type}")
        
        # Create StreamInfo object
        # The StreamInfo constructor doesn't accept content_type as a parameter
        stream_info = StreamInfo(filename=filename, extension=extension)
        
        # Convert file to markdown
        # According to the error, convert_stream only takes 2 arguments (self and stream)
        result = md_converter.convert_stream(file_stream)
        
        # Extract the markdown text from the result object
        # The result is a DocumentConverterResult object, which needs to be converted to a string
        markdown_content = str(result)
        
        logger.info(f"Successfully extracted content from {filename}")
        
        # Return the result
        return jsonify({
            "filename": filename,
            "content": markdown_content,
            "format": "text/plain"
        })
    
    except UnsupportedFormatException as e:
        logger.error(f"Unsupported format: {str(e)}")
        return jsonify({"detail": f"Unsupported file format: {str(e)}"}), 415
    
    except FileConversionException as e:
        logger.error(f"Conversion error: {str(e)}")
        return jsonify({"detail": f"File conversion error: {str(e)}"}), 500
    
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        return jsonify({"detail": f"An unexpected error occurred: {str(e)}"}), 500

@app.route('/health')
def health_check():
    """
    Health check endpoint to verify the API is running.
    """
    logger.debug("Health check requested")
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)