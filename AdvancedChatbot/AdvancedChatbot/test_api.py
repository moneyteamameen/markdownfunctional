#!/usr/bin/env python3
"""
Test script for the Document Content API.
This script sends a test document to the /extract endpoint and displays the extracted content.
"""

import sys
import requests
import os
import argparse

def test_api_info():
    """Test the API info endpoint."""
    response = requests.get("http://localhost:5000/")
    if response.status_code == 200:
        print("API Info:")
        print(response.json())
        return True
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return False

def test_api_health():
    """Test the API health endpoint."""
    response = requests.get("http://localhost:5000/health")
    if response.status_code == 200:
        print("API Health:")
        print(response.json())
        return True
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return False

def test_extract_content(file_path):
    """Test the content extraction endpoint."""
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} does not exist")
        return False
    
    print(f"Extracting content from file: {file_path}")
    
    with open(file_path, "rb") as f:
        files = {"file": (os.path.basename(file_path), f)}
        response = requests.post("http://localhost:5000/extract", files=files)
    
    if response.status_code == 200:
        result = response.json()
        print(f"Extracted content from {result['filename']} successfully!")
        print(f"Content format: {result['format']}")
        print("\nExtracted content (first 500 chars):")
        print(result['content'][:500] + "..." if len(result['content']) > 500 else result['content'])
        
        # Save the content to a file
        output_file = os.path.splitext(os.path.basename(file_path))[0] + ".txt"
        with open(output_file, "w") as f:
            f.write(result['content'])
        print(f"\nExtracted content saved to {output_file}")
        
        return True
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return False

def create_test_html():
    """Create a simple HTML file for testing."""
    html_content = """<!DOCTYPE html>
<html>
<head>
    <title>Test Document</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
        h1 { color: #333; }
        .note { background-color: #f8f9fa; padding: 10px; border-left: 4px solid #5bc0de; }
        table { border-collapse: collapse; width: 100%; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #f2f2f2; }
        code { background-color: #f5f5f5; padding: 2px 4px; border-radius: 4px; }
    </style>
</head>
<body>
    <h1>MarkItDown Test Document</h1>
    <p>This is a test document to verify the markdown conversion functionality.</p>
    
    <h2>Features to Test</h2>
    <p>This document includes various HTML elements to test the conversion process:</p>
    <ul>
        <li><strong>Bold text</strong> and <em>italic text</em> formatting</li>
        <li>Nested lists:
            <ol>
                <li>Ordered item 1</li>
                <li>Ordered item 2</li>
                <li>Ordered item 3</li>
            </ol>
        </li>
        <li>Code formatting: <code>const example = "Hello World";</code></li>
    </ul>
    
    <div class="note">
        <p>This is a note with special formatting to test div conversion.</p>
    </div>
    
    <h2>Table Example</h2>
    <table>
        <thead>
            <tr>
                <th>Name</th>
                <th>Description</th>
                <th>Priority</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Feature A</td>
                <td>This is a description of Feature A</td>
                <td>High</td>
            </tr>
            <tr>
                <td>Feature B</td>
                <td>This is a description of Feature B</td>
                <td>Medium</td>
            </tr>
            <tr>
                <td>Feature C</td>
                <td>This is a description of Feature C</td>
                <td>Low</td>
            </tr>
        </tbody>
    </table>
    
    <h2>Links and Images</h2>
    <p>Here is a link to <a href="https://example.com">Example Website</a>.</p>
    
    <h3>Code Block Example</h3>
    <pre><code>
    function helloWorld() {
        console.log("Hello, World!");
    }
    
    helloWorld();
    </code></pre>
    
    <hr>
    
    <footer>
        <p>This is a footer section.</p>
    </footer>
</body>
</html>"""
    
    file_path = "test_document.html"
    with open(file_path, "w") as f:
        f.write(html_content)
    
    print(f"Created test HTML file: {file_path}")
    return file_path

def main():
    parser = argparse.ArgumentParser(description="Test the Document Content API")
    parser.add_argument("--file", help="Path to a file to convert", default=None)
    args = parser.parse_args()
    
    # Test API info
    if not test_api_info():
        print("Failed to get API info")
        return
    
    # Test API health
    if not test_api_health():
        print("Failed to get API health")
        return
    
    # Test content extraction
    file_path = args.file
    if not file_path:
        print("No file specified, creating a test HTML file...")
        file_path = create_test_html()
    
    if not test_extract_content(file_path):
        print("Failed to extract content from file")
        return
    
    print("\nAll tests completed successfully!")

if __name__ == "__main__":
    main()