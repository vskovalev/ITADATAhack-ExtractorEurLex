import time
from selenium import webdriver
from pathlib import Path
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium_walker.interface_functions import button_click_by_element
from functions.functions_os.names_extractor_from_folder_by_type \
    import names_extractor_from_folder_by_type



def get_pdfs_by_celex(
    listOfCelex,
    exec_driver_path,
    options,
):
    languagues = [
        "BG",
        "ES",
        "CS",
        "DA",
        "DE",
        "ET",
        "EL",
        "EN",
        "FR",
        "GA",
        "HR",
        "IT",
        "LV",
        "LT",
        "HU",
        "MT",
        "NL",
        "PL",
        "PT",
        "RO",
        "SK",
        "SL",
        "FI",
        "SV",
    ]

    service = Service(executable_path=Path(exec_driver_path))
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://eur-lex.europa.eu/homepage.html")

    wait = WebDriverWait(driver, 120)
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="QuickSearchField" and @placeholder="QUICK SEARCH"]')
        )
    )

    search_button = driver.find_element(
        By.XPATH, '//*[@id="QuickSearchField" and @placeholder="QUICK SEARCH"]'
    )

    search_button.send_keys(listOfCelex[0])

    button_click_by_element(
        element=driver.find_element(
            By.XPATH, '//*[@class="btn btn-primary QuickSearchBtn" and @title="Search"]'
        )
    )

    qid = driver.current_url.split("qid=")[1]
    list_of_celexes_downloaded = []
    with open("files/txts/celex_ids.txt") as f:
        for line in f:
            inner_list = [elt.replace("'", "").strip() for elt in line.split(",")]
            list_of_celexes_downloaded.extend(inner_list)
    set_of_downloaded = set(
        list(
            map(
                lambda x: x.split("_")[1],
                list_of_celexes_downloaded,
            )
        )
    )

    for celex in listOfCelex:
        if celex not in set_of_downloaded:
            for lang in languagues:
                form = f"https://eur-lex.europa.eu/legal-content/{lang}/TXT/PDF/?uri=CELEX:{celex}&qid={qid}"
                driver.get(form)
                try:
                    driver.find_element(By.XPATH, '//*[@class="alert alert-warning"]')
                except:
                    continue
