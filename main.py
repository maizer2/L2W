# from app.pdf_read import pdf_read
import pdfplumber as pp

# --------------------------------------------------------------------------------------

dir_path = "pdf/"
pdf_format = ".pdf"
pdf_name = "Toward Characteristic-Preserving Image-based Virtual Try-On Network"

pdf_file_path = dir_path + pdf_name + pdf_format

# ---------------------------------------------------------------------------------------
# Refine text to word
def page_refine(page):

    print(f"Refine page number : {page.page_number}")
    print(page.extract_text())

# ---------------------------------------------------------------------------------------
# run pdf_read module
def pdf_read(pdf_file_path):

    pdf = pp.open(pdf_file_path)

    pages_word = []

    # pdf.pages() is list type
    pages = pdf.pages

    for page in pages:

        page_word = []
        page_word = page_refine(page)

        pages_word.append(page_word)

        # print("-------------")

# ---------------------------------------------------------------------------------------
# first page parser
def pdf_first(pdf_file_path):

    pdf = pp.open(pdf_file_path)

    first_page = pdf.pages[0]
    print(f"page number : {first_page.page_number}")
    
    first_page_words = first_page.extract_text()
    # print(first_page_words)
    for i in range(len(first_page_words)):
        print(first_page_words[i])
        # print(first_page_words[i])

# ---------------------------------------------------------------------------------------
# main module
if __name__ == "__main__":
    # pdf_read(pdf_file_path)
    pdf_first(pdf_file_path)