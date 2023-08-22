import PyPDF2
import re


def function_pdf_celex_extractor() -> None:
    
    pattern_1 = r'[\dA-Z]{10,15}'
    pattern_2 = r'[\dA-Z]{10,15}\(\d{2}\)'
    pattern_3 = r'[\dA-Z]{10,15}\(\d{2}\)[A-Z]{1}\(\d{2}\)'
    pattern_4 = r'[\dA-Z]{10,15}-\d{8}'
    pattern_5 = r'[\dA-Z]{10,15}\(\d{2}\)-\d{8}'
    pattern_6 = r'[\dA-Z]{10,15}\(\d{2}\)[A-Z]{1}\(\d{2}\)-\d{8}'

    patterns = [pattern_1, pattern_2, pattern_3, 
                pattern_4, pattern_5, pattern_6]
                
    result = []

    for chapter in [
        '01', '02', '03', '04', '05', 
        '06', '07', '08', '09', '10', 
        '11', '12', '13', '14', '15', 
        '16', '17', '18', '19', '20']:

        path_for_pdf = f'files\general_pdfs\chapter {chapter}.pdf'
        pdfFileObj = open(path_for_pdf, 'rb')
        pdfReader = PyPDF2.PdfReader(pdfFileObj)

        for page_num, page in enumerate(pdfReader.pages,
                                        start=1):
            text_for_analysis = re.sub("^\s+|\n|\r|\s+$", ' ', page.extract_text())
            # opening the text file in write mode to write the text extracted from the pdf file into it.
            for pattern in patterns:
                result.extend(re.findall(pattern, text_for_analysis))
        with open('files\\txts\\general chapter celex '+chapter+'.txt', 'x') as file:
            print(set(result), file=file)