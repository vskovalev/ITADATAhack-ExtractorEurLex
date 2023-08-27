from selenium_walker.selenium_loops import selenium_loops
from algorithms.functions_treatment.function_pdf_to_txt import function_pdf_to_txt


for counter_of_tries in range(10):
    try:
        print(counter_of_tries)
        selenium_loops()
    except:
        function_pdf_to_txt(part=str(counter_of_tries))