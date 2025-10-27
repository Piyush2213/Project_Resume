import re
from PyPDF2 import PdfReader

def extract_text_from_pdf(file):
    """Extracts text from all pages of a PDF file."""
    reader = PdfReader(file)
    text = ''
    for page in reader.pages:
        text += page.extract_text() or ''
    return text


def extract_email_from_text(text):
    """Extracts the first email found in the text."""
    match = re.search(r'[\w\.-]+@[\w\.-]+', text)
    return match.group(0) if match else None


