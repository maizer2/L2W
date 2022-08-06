import pdfplumber as pp

# Referce 제외
def rm_ref():
    None

# run pdf_read module
def pdf_read(pdf_file_path):

    pdf = pp.open(pdf_file_path)

    pages_words = []

    # pdf.pages() is list type
    pages = pdf.pages

    for page in pages:

        page_words = []
        page_words = page.extract_words()
        
        print(page_words)
        pages_words.append(page_words)

    # print(page_words)