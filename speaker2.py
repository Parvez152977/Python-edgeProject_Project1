import os
import PyPDF2
from pdf2image import convert_from_path
import pytesseract
import pyttsx3


def pdf_to_mp3(pdf_file, mp3_file):
    # Check if the PDF file exists
    if not os.path.isfile(pdf_file):
        print(f"File not found: {pdf_file}")
        return

    # Initialize text variable
    text = ''

    # Read PDF
    try:
        reader = PyPDF2.PdfReader(pdf_file)

        # Process each page
        for i, page in enumerate(reader.pages):
            # Attempt to extract text
            page_text = page.extract_text()

            if page_text:  # If text is found, use it
                text += page_text + ' '
            else:  # If no text is found, convert page to image and use OCR
                print(f"Page {i + 1} is an image; performing OCR.")
                images = convert_from_path(pdf_file, first_page=i + 1, last_page=i + 1)
                for image in images:
                    page_text = pytesseract.image_to_string(image)
                    text += page_text + ' '

    except Exception as e:
        print(f"Error reading PDF file: {e}")
        return

    # Check if any text was extracted
    if not text.strip():
        print("No text found in the PDF file.")
        return

    # Initialize the text-to-speech engine
    engine = pyttsx3.init()
    engine.save_to_file(text, mp3_file)
    engine.runAndWait()
    print(f"Converted '{pdf_file}' to '{mp3_file}'")


# Example usage
pdf_file_path = '/home/parvezalam/Downloads/Brain Rules.pdf'  # Replace with your PDF file path
mp3_file_path = '/home/parvezalam/Desktop/Brain_rules.mp3'  # Desired output MP3 file path

pdf_to_mp3(pdf_file_path, mp3_file_path)
