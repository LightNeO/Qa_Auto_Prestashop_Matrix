from modules.ui.pages.main_page import MainPage
from selenium.webdriver.common.by import By


def test_main_page_title(browser, wait):
    main_page = MainPage(browser, wait)
    main_page.open_main_page()

    currency_selector_text = main_page.find_element(By.XPATH, main_page.CURRENCY_SELECTOR).text
    currency_sign = ''
    if currency_selector_text == 'UAH':
        currency_sign = '₴'
    elif currency_selector_text == 'USD':
        currency_sign = '$'
    elif currency_selector_text == 'EUR':
        currency_sign = '€'

    parent_element = main_page.find_element(By.XPATH, main_page.PARENT_ELEMENT_XPATH)
    child_elements = parent_element.find_elements(By.XPATH, main_page.CHILD_ELEMENT_XPATH)
    result = True
    for child in child_elements:
        if currency_sign not in child.text:
            result = False

    assert result
