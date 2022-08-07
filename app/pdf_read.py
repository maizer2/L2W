from pickle import TRUE
import pdftotext as ptt

# ---------------------------------------------------------------------------------------
# Refine text to word
def page_refine(page):
 
    # 단어를 저장할 변수
    word = None
    # 페이지 내 모든 단어를 저장할 리스트 변수
    page_words = []

    # 어떻게 저장할까?
    # " " 띄어쓰기가 오기 전까지 단어를 저장한다.
    # 띄어쓰기 단어 띄어씌기형식이르모
    ## 띄어쓰기가 나온 기준부터 다음 띄어쓰기가 나올 때까지 단어로서 저장한다.

    # 전체 문자만큼 반복한다.
    for i in range(len(page)):

        # 알파벳 외에는 무시
        ## 대소문자 주의
        if page[i] == " " or page[i] == "a" or page[i] == "b" or page[i] == "c" or page[i] == "d" or page[i] == "e" or page[i] == "f" or page[i] == "g" or page[i] == "h" or page[i] == "i" or page[i] == "j" or page[i] == "k" or page[i] == "l" or page[i] == "m" or page[i] == "n" or page[i] == "o" or page[i] == "p" or page[i] == "q" or page[i] == "r" or page[i] == "s" or page[i] == "t" or page[i] == "u" or page[i] == "v" or page[i] == "w" or page[i] == "x" or page[i] == "y" or page[i] == "z" or page[i] == "A" or page[i] == "B" or page[i] == "C" or page[i] == "D" or page[i] == "E" or page[i] == "F" or page[i] == "G" or page[i] == "H" or page[i] == "I" or page[i] == "J" or page[i] == "K" or page[i] == "L" or page[i] == "M" or page[i] == "N" or page[i] == "O" or page[i] == "P" or page[i] == "Q" or page[i] == "R" or page[i] == "S" or page[i] == "T" or page[i] == "U" or page[i] == "V" or page[i] == "W" or page[i] == "X" or page[i] == "Y" or page[i] == "Z":
        
            # " ", space 문자가 나오면 끝
            ## word 초기화 해야함
            if page[i] == " ":

                # 만약 space 문자가 연속으로 올 경우 None이 들어가는 경우를 방지해주는 조건문
                if word == None:
                    continue
                else:
                    page_words.append(word)

                    # word 변수 초기화
                    word = None

                continue

            # 초기화 후 첫 단어일 경우 첫 문자 넣기 위한 조건문
            if word == None:
                word = page[i]
            else:
                word += page[i]
    
    # 마지막 단어일 경우, space가 없기 때문에 따로 처리해줘야함
    # 마지막 분기 일 경우 마지막 단어 저장
    if word != None:
        page_words.append(word)

    return page_words

# ---------------------------------------------------------------------------------------
# except_reference module
def except_reference(page_word):

    # Reference가 나오는 원소 번호 찾기
    for i in range(len(page_word)):
        if page_word[i] == "References" or page_word[i] == "references":

            # reference 앞 단어까지 리턴
            return page_word[:i], True
        
    return page_word, False
    
# ---------------------------------------------------------------------------------------
# run pdf_read module
def pdf_read(pdf_file_path, reference):

    # refine page str to word
    pdf = ptt.PDF(pdf_file_path)

    # 페이지별로 저장됨
    pages_word = []

    # reference 저장 유무에 따른 변수
    ## 기본은 False이고 True일 경우 다음 페이지부터 저장안함
    endSign = False

    # # page 번호
    # page_number = 1

    for page in pdf:
        
        # 페이지의 모든 단어를 저장할 리스트 변수
        page_word = page_refine(page)

        # 만약 reference 부분을 제외할 경우 모듈 시작
        if reference == True:
            # 페이지 번호 받아야함
            page_word, endSign = except_reference(page_word)

        pages_word.append(page_word)
        # page_number += 1

        if endSign == True:
            break

    return pages_word
    