<!DOCTYPE html>
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
</html>