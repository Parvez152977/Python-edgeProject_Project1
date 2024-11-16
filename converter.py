import PyPDF2
import pyttsx3

def pdf_to_mp3_with_pyttsx3(pdf_file, mp3_file):
    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text() + ' '

    if not text.strip():
        print("No text found in the PDF file.")
        return

    engine = pyttsx3.init()
    engine.save_to_file(text, mp3_file)
    engine.runAndWait()
    print(f"Converted '{pdf_file}' to '{mp3_file}' using pyttsx3")

# Example usage
pdf_file_path = '/home/parvezalam/Downloads/brain rules.pdf'  # Replace with your PDF file path
mp3_file_path = '/home/parvezalam/Desktop/BrainRules.mp3'    # Desired output MP3 file path

pdf_to_mp3_with_pyttsx3(pdf_file_path, mp3_file_path)
