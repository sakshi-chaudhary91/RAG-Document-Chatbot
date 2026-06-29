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


# NEW FUNCTION (simple search logic)
def keyword_search(text, query):
    sentences = text.split(".")

    results = []

    for sentence in sentences:
        if query.lower() in sentence.lower():
            results.append(sentence.strip())

    return results[:5]


