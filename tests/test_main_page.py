import time

from modules.ui.pages.main_page import MainPage
from selenium.webdriver.common.by import By
from modules.ui.pages.locators import MainPageLocators
from modules.ui.pages.locators import SearchPageLocators


def test_products_currency(browser, wait):
    main_page = MainPage(browser, wait)
    main_page.open_main_page()

    product_list = main_page.get_products_list()
    currency_sign = main_page.get_expected_currency_sign()

    is_currency_sign_correct = True
    for product in product_list:
        if currency_sign not in product.text:
            is_currency_sign_correct = False

    assert is_currency_sign_correct


def test_amount_of_product_found(browser, wait):
    main_page = MainPage(browser, wait)
    main_page.open_main_page()

    main_page.set_currency('USD')
    # Незнаю як побороти очікування поки сторінка оновиться, пробував через JavaScript - не спрацювало, тому сліп)
    time.sleep(1)
    main_page.search_for_item('dress')
    main_page.click(By.XPATH, SearchPageLocators.SHOW_ALL_BTN)

    parent_element = main_page.find_element(By.XPATH, SearchPageLocators.FOUND_ELEMENTS_CONTAINER)
    child_element = parent_element.find_elements(By.XPATH, './li')
    result_amount_text = main_page.find_element(By.XPATH, MainPageLocators.AMOUNT_OF_RESULTS_FOUND).text
    result_amount = int(''.join([char for char in result_amount_text if char.isdigit()]))

    assert len(child_element) == result_amount

    # Додав чисто для завдання 6
    test_products_currency(browser, wait)



