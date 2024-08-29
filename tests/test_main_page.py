import time

from modules.ui.pages.main_page import MainPage
from selenium.webdriver.common.by import By
from modules.ui.pages.locators import MainPageLocators
from modules.ui.pages.locators import SearchPageLocators


def test_popular_currency(browser, wait):
    main_page = MainPage(browser, wait)
    main_page.open_main_page()

    currency_selector_text = main_page.find_element(By.XPATH, MainPageLocators.CURRENCY_SELECTOR).text
    currency_sign = ''
    if currency_selector_text == 'UAH':
        currency_sign = '₴'
    elif currency_selector_text == 'USD':
        currency_sign = '$'
    elif currency_selector_text == 'EUR':
        currency_sign = '€'

    parent_element = main_page.find_element(By.XPATH, MainPageLocators.PARENT_ELEMENT_XPATH)
    child_elements = parent_element.find_elements(By.XPATH, MainPageLocators.CHILD_ELEMENT_XPATH)
    result = True
    for child in child_elements:
        if currency_sign not in child.text:
            result = False

    assert result


def test_amount_of_product_found(browser, wait):
    main_page = MainPage(browser, wait)
    main_page.open_main_page()

    main_page.set_currency('USD')
    #Незнаю як побороти очікування поки сторінка оновиться, пробував через JavaScript - не спрацювало, тому сліп)
    time.sleep(1)
    main_page.search_for_item('dress')
    main_page.click(By.XPATH, SearchPageLocators.AMOUNT_OF_ELEMENTS)

    parent_element = main_page.find_element(By.XPATH, SearchPageLocators.FOUND_ELEMENTS_CONTAINER)
    child_element = parent_element.find_elements(By.XPATH, './li')
    result_amount_text = main_page.find_element(By.XPATH, MainPageLocators.AMOUNT_OF_RESULTS_FOUND).text
    result_amount = int(''.join([char for char in result_amount_text if char.isdigit()]))

    assert len(child_element) == result_amount
