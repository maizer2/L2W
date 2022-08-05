from app.pdf_read import pdf_read

dir_path = "pdf/"
pdf_format = ".pdf"
pdf_name = "Toward Characteristic-Preserving Image-based Virtual Try-On Network"

pdf_file_path = dir_path + pdf_name + pdf_format

if __name__ == "__main__":
    pdf_read(pdf_file_path)