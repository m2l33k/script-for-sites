import fitz  # PyMuPDF
from PIL import Image
import os

# Define the directories
books_dir = "assets/books"
images_dir = "assets/images"

# Create the images directory if it doesn't exist
os.makedirs(images_dir, exist_ok=True)

# Loop through all PDF files in the books directory
for filename in sorted(os.listdir(books_dir)):
    if filename.endswith(".pdf"):
        book_path = os.path.join(books_dir, filename)
        # Open the PDF file
        pdf_document = fitz.open(book_path)
        # Get the first page
        first_page = pdf_document.load_page(0)
        # Render the page to a pixmap (image in memory)
        pix = first_page.get_pixmap()
        # Convert pixmap to an image using PIL
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        # Save the image in the images directory with the same name as the PDF file
        image_path = os.path.join(images_dir, f"{os.path.splitext(filename)[0]}.jpg")
        img.save(image_path, "JPEG")
        print(f"Saved screenshot of first page for {filename} as {image_path}")
        # Close the PDF file
        pdf_document.close()
