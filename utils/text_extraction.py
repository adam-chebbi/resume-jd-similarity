import pdfplumber

def extract_text_from_pdf(file_path):
    """Extract text from a PDF file."""
    with pdfplumber.open(file_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text.strip()
