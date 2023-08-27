import threading
import time
import numpy as np
from selenium_walker.get_pdfs_by_celex import get_pdfs_by_celex
from algorithms.functions_os.kill_chrome_processes import kill_chrome_processes
from selenium.webdriver.chrome.options import Options
from selenium_walker.get_celexes import get_seria_of_celexes
from pathlib import Path


def selenium_loops():
    dist_path = "C:\\Users\\vkovalev\\Desktop\\New folder (2)\\files\\pdfs"
    waiting_minutes = 10
    exec_driver_path = "selenium_core\\chromedriver.exe"
    # General Options initialization
    options = Options()
    options.add_experimental_option(
        "prefs",
        {
            "download.default_directory": dist_path,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True,
            "download.prompt_for_download": False,  # To auto download the file
            "download.directory_upgrade": True,
            "plugins.always_open_pdf_externally": True,  # It will not show PDF directly in chrome
        },
    )
    options.add_argument("--kiosk")
    threads = []
    celex_lists = get_seria_of_celexes().CELEX_ID.drop_duplicates().to_list()
    celex_lists_size = len(celex_lists) 
    number_threads = 5

    celex_lists_splited = []
    for i, j in zip(
            list(map(lambda x: int(x), np.arange(0, celex_lists_size, celex_lists_size / number_threads))),
            list(map(lambda x: int(x), np.arange(0, celex_lists_size, celex_lists_size / number_threads)))[1:],
        ):
        celex_lists_splited.append(
            celex_lists[i:j]
            )
        last_index = j
        
    celex_lists_splited.append(celex_lists[last_index:])

    for celexes_list in celex_lists_splited:
        threads.append(
            threading.Thread(
                target=get_pdfs_by_celex, args=(celexes_list, exec_driver_path, options)
            )
        )

    # start of threads
    for thread in threads:
        thread.start()

    time.sleep(waiting_minutes * 60)
    # end of threads
    for thread in threads:
        thread.join()

    # kill all generated threads
    kill_chrome_processes()
