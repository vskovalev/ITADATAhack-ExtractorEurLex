import threading
from selenium_walker.get_pdfs_by_celex import get_pdfs_by_celex
from functions.functions_os.kill_chrome_processes import kill_chrome_processes
from selenium.webdriver.chrome.options import Options


def get_pdfs_by_celex():
    dist_path = r"files\\pdfs"
    waiting_minutes = 10
    exec_driver_path = "selenium_core\\chromedriver.exe"
    # General Options initialization
    options = Options()
    options.add_experimental_option(
        "prefs",
        {
            "download.default_directory": dist_path,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True,
        },
    )
        
    threads = []
    for celexes_list in celex_lists:
        threads.append(
            threading.Thread(
                target=get_pdfs_by_celex, args=(celexes_list, exec_driver_path)
            )
        )
    # start of threads
    for thread in threads:
        thread.start()

    # end of threads
    for thread in threads:
        thread.join()

    # kill all generated threads
    kill_chrome_processes()
