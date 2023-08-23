import time
from selenium.webdriver.common.by import By


def button_click_by_element(*, 
                            element,
                            sleep_time=3):
    time.sleep(sleep_time)
    element.click()


def button_click_by_xpath(
    *,
    driver,
    xpath: str,
    sleep_time=5,
):
    '''
    Button click by xpath in selenium webdriver
    '''
    time.sleep(sleep_time)
    button = driver.find_element(By.XPATH, xpath)
    button.click()


def button_click_by_selector(
    *,
    driver,
    css_selector: str,
    sleep_time=5,
):
    '''
    Button click by css selector in selenium webdriver
    '''
    time.sleep(sleep_time)

    button = driver.find_element(By.CSS_SELECTOR, css_selector)
    button.click()