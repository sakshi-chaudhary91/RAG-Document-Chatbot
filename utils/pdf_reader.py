import pdfplumber

def extract_text(pdf_file):
    text = ""
    pages = 0

    with pdfplumber.open(pdf_file) as pdf:
        pages = len(pdf.pages)

        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    word_count = len(text.split())

    return text, pages, word_count