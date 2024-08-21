# sites  Books generator  Project

This project generates a simple HTML page listing downloadable cybersecurity books. It automatically generates images from the first page of each PDF book and displays them alongside download links.

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Directory Structure](#directory-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Automated PDF Image Generation:** Extracts the first page of each PDF as an image.
- **Dynamic HTML Generation:** Creates an HTML file listing all the books with their corresponding images and download links.
- **Sorting:** Books are automatically sorted by numerical prefixes in their filenames.

## Prerequisites

Ensure you have the following software installed on your machine:

- Python 3.x
- pip (Python package installer)
- Virtualenv (recommended)

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/m2l33k/script-for-sites.git
   cd script-for-sites 
you can move this script to any project you want to create 

2. Create and Activate a Virtual Environment:

bash

python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate 

Install Required Python Packages: 
Pillow
PyMuPDF

Usage

    Prepare the Book Files:

    Place your PDF books in the assets/books directory.

    Run the Image Generation Script:

    This script will create images from the first page of each PDF and save them in the assets/images directory.

    bash

python generate_images.py

Generate the HTML File:

After generating the images, run the following command to create the test.html file listing all books with images and download links.

bash

    python generate_html.py

    Open the HTML File:

    Open test.html in a web browser to see the generated list of books.

Directory Structure

Here’s the structure of the project:

graphql

cybersecurity-books-download/
│
├── assets/
│   ├── books/             # Directory where PDF books are stored
│   ├── images/            # Directory where generated images are stored
│   └── css/
│       └── style.css      # Custom CSS styles for the HTML page
│
├── generate_images.py     # Script to generate images from PDF files
├── generate_html.py       # Script to generate the HTML file
├── requirements.txt       # List of required Python packages
└── README.md              # This README file

Contributing

Contributions are welcome! Please fork this repository and submit a pull request for any improvements or new features.
License

This project is licensed under the MIT License. See the LICENSE file for more details.

markdown


### Steps for Activation on a New Machine

1. **Clone the repository** to the new machine using the GitHub URL.
2. **Navigate** to the project directory.
3. **Create a virtual environment** to isolate dependencies.
4. **Activate the virtual environment** and install dependencies using `pip`.
5. **Add your PDF files** to the `assets/books` directory.
6. **Run the scripts** `generate_images.py` and `generate_html.py` to generate the image files and the HTML page.
7. **Open the generated HTML file** in your browser to view the list of books with images and download links.


By following these steps, you'll be able to set up and run the project on any machine quickly.

