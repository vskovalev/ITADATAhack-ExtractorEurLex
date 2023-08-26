import re
import PyPDF2
import os
from pathlib import Path
from functions.functions_os.names_extractor_from_folder_by_type import names_extractor_from_folder_by_type
from tqdm import tqdm
        
def function_pdf_to_txt(part):
    list_of_pdf_names = names_extractor_from_folder_by_type(path="./files/pdfs")
    str_for_saving = '{'
    print('Save')
    list_of_pdf_names_removed = list_of_pdf_names.copy()

    for name in tqdm(list_of_pdf_names):
        path_for_pdf = f'./files/pdfs/{name}'
        pdfFileObj = open(path_for_pdf, 'rb')
        try:
            pdfReader = PyPDF2.PdfReader(pdfFileObj)
            text_for_save = '{'
            
            for page in pdfReader.pages:
                text_for_save += re.sub("^\s+|\n|\r|\s+$", ' ', page.extract_text())
            str_for_saving+= f"'{name}': '{text_for_save}',\n"
        except:
            list_of_pdf_names_removed.remove(name)

    with open(
        file=f'./files/txts/celex_to_text_part_{part}.txt',
        mode='w',
        encoding='UTF-8') as file:
        print(str_for_saving + '}', file=file)
        
    print('Remove')
    for name in tqdm(list_of_pdf_names_removed):
        path_for_pdf = f'./files/pdfs/{name}'
        os.remove(path_for_pdf)