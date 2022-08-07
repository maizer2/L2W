from app.pdf_read import pdf_read
from app.word_translate import word_translation
from app.word_preprocessing import word_prepreocesor

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

    # pdf reader
    pages_word = pdf_read(pdf_file_path, reference)

    # 단어 전처리
    word = word_prepreocesor(pages_word)
    
    # 단어 번역
    pages_word = word_translation(word)