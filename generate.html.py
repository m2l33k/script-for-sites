# Malek Aziz Hassayoun 
#https://github.com/m2l33k
import os
import re

# Define paths
books_dir = './assets/books'
images_dir = './assets/images'
output_file = 'test.html'

# Get a list of all book files in the books directory
books = [f for f in os.listdir(books_dir) if f.endswith('.pdf')]

# Extract numerical prefixes and sort the books
def extract_number(filename):
    match = re.match(r'(\d+)\.', filename)
    return int(match.group(1)) if match else float('inf')

books.sort(key=extract_number)

# List of common image file extensions
image_extensions = ['.jpg', '.jpeg', '.png', '.gif']

# Start creating the HTML content
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cybersecurity Books Download</title>
    <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
    <div class="container">
        <h1>Cybersecurity Books Download</h1>
        <ol class="book-list">
"""

# Loop through each book and add it to the HTML content
for book in books:
    # Prepare file paths
    book_name = os.path.basename(book)
    book_title = os.path.splitext(book_name)[0]
    image_file = None
    
    # Check for corresponding image file
    for ext in image_extensions:
        possible_image_file = os.path.join(images_dir, f"{book_title}{ext}")
        if os.path.isfile(possible_image_file):
            image_file = possible_image_file
            break

    # If no image found, use a placeholder
    if image_file is None:
        image_file = 'assets/images/placeholder.png'

    # Prepare download link
    download_link = os.path.join(books_dir, book_name)
    
    # Extract number for guide
    number = extract_number(book_name)

    # Add book information to HTML
    html_content += f"""
        <li class="book-item">
            <img src="{image_file}" alt="{book_name} Cover">
            <p>{number}. {book_name}</p>
            <a href="{download_link}" download="{book_name}" class="download-button">Download</a>
        </li>
    """

# Close the HTML content
html_content += """
        </ol>
    </div>
</body>
</html>
"""

# Write HTML content to a file
with open(output_file, 'w') as file:
    file.write(html_content)

print(f"HTML file '{output_file}' has been generated.")
