import PyPDF2
from gtts import gTTS
import os

def pdf_to_mp3(pdf_file, mp3_file, lang='en'):
    # Check if the PDF file exists
    if not os.path.isfile(pdf_file):
        print(f"File not found: {pdf_file}")
        return

    # Read PDF
    try:
        with open(pdf_file, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ''

            # Extract text from each page
            for page in reader.pages:
                text += page.extract_text() + ' '
    except Exception as e:
        print(f"Error reading PDF file: {e}")
        return

    # Check if any text was extracted
    if not text.strip():
        print("No text found in the PDF file.")
        return

    # Convert text to speech
    try:
        tts = gTTS(text=text, lang=lang)
        # Ensure the output directory exists
        os.makedirs(os.path.dirname(mp3_file), exist_ok=True)
        tts.save(mp3_file)
        print(f"Converted '{pdf_file}' to '{mp3_file}'")
    except Exception as e:
        print(f"Error converting text to speech: {e}")

# Example usage
pdf_file_path = '/home/parvezalam/Downloads/brain rules.pdf'  # Replace with your PDF file path
mp3_file_path = '/home/parvezalam/Desktop/Brain_rules.mp3'  # Desired output MP3 file path

pdf_to_mp3(pdf_file_path, mp3_file_path)
