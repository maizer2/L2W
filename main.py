from app.pdf_read import pdf_read

# --------------------------------------------------------------------------------------
# Parameter setting
# Filename, except file format
pdf_name = "Toward Characteristic-Preserving Image-based Virtual Try-On Network"
# Choose except reference
reference = True

dir_path = "pdf/"
pdf_format = ".pdf"

pdf_file_path = dir_path + pdf_name + pdf_format

pdf_file_path = open(pdf_file_path, "rb")

# ---------------------------------------------------------------------------------------
# main module
if __name__ == "__main__":
    pages_word = pdf_read(pdf_file_path, reference)

    print(pages_word)