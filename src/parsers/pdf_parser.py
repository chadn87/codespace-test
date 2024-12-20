# src/parsers/pdf_parser.py
from PyPDF2 import PdfReader

def parse_pdf(file_path):
    """
    Extracts text from a PDF file using PyPDF2.

    Args:
        file_path (str): Path to the PDF file.

    Returns:
        str: Extracted text, or an empty string if an error occurs.
    """
    extracted_text = ""
    try:
        reader = PdfReader(file_path)
        for page in reader.pages:
            text = page.extract_text()
            if text:
                extracted_text += text
    except Exception as e:
        print(f"Error parsing PDF: {e}")
    return extracted_text
