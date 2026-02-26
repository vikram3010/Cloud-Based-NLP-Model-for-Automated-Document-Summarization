from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_file):
    reader = PdfReader(pdf_file)
    extracted_text = []

    for page in reader.pages:
        text = page.extract_text()
        if text:  # Avoid appending None
            extracted_text.append(text.strip())

    return '\n'.join(extracted_text)
