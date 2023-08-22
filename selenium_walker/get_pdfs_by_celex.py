from selenium import webdriver

def get_pdfs_by_celex(
    listOfCelex,
    exec_driver_path,
    options,
):
    
    languagues = ['BG', 'ES', 'CS', 
                  'DA', 'DE', 'ET',
                  'EL', 'EN', 'FR',
                  'GA', 'HR', 'IT',
                  'LV', 'LT', 'HU',
                  'MT', 'NL', 'PL', 
                  'PT', 'RO', 'SK', 
                  'SL', 'FI', 'SV']
    form = f'https://eur-lex.europa.eu/legal-content/{lang}/TXT/PDF/?uri=CELEX:{celex}&qid={qid}'
    driver = webdriver.Chrome(executable_path=exec_driver_path,
                                      chrome_options=options)
    driver.get("https://eur-lex.europa.eu/homepage.html")
    