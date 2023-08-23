import re
import PyPDF2
from functions.functions_os.names_extractor_from_folder_by_type import names_extractor_from_folder_by_type

        
def function_pdf_to_csv():
    list_of_pdf_names = names_extractor_from_folder_by_type(path="./files/pdfs")
    list_for_saving = []
    for name in list_of_pdf_names:
        path_for_pdf = f'./files/pdfs/{name}'
        pdfFileObj = open(path_for_pdf, 'rb')
        pdfReader = PyPDF2.PdfReader(pdfFileObj)
        text_for_save = ''
        
        for page in pdfReader.pages:
            text_for_save += re.sub("^\s+|\n|\r|\s+$", ' ', page.extract_text())
        list_for_saving.append(text_for_save+' ||||| ')

    with open('files\\txts\\celex_files.txt', 'x') as file:
        print("".join(list_for_saving), file=file)