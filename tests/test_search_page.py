import time

from modules.ui.pages.main_page import MainPage
from modules.ui.pages.search_page import SearchPage
from selenium.webdriver.common.by import By
from modules.ui.pages.locators import SearchPageLocators


def test_sorting_price(browser, wait):
    search_page = SearchPage(browser, wait)
    search_page.open_search_page('dress')

    search_page.click(By.XPATH, SearchPageLocators.SORT_BY_BTN)
    search_page.click(By.XPATH, SearchPageLocators.HIGH_TO_LOW_OPTION)

    product_list = search_page.get_products_list(By.XPATH, SearchPageLocators.PRODUCTS_PARENT_ELEMENT, SearchPageLocators.PRODUCT_CHILD_ELEMENT)
    currency_sign = search_page.get_expected_currency_sign()

    prices = []
    for product in product_list:
        price = float(product.text.replace(currency_sign, '').replace(',', '').replace(' ', ''))
        prices.append(price)

    assert prices == sorted(prices, reverse=True)


def test_price(browser, wait):
    search_page = SearchPage(browser, wait)
    search_page.open_search_page('dress')

    search_page.click(By.XPATH, SearchPageLocators.SORT_BY_BTN)
    search_page.click(By.XPATH, SearchPageLocators.HIGH_TO_LOW_OPTION)
    search_page.click(By.XPATH, SearchPageLocators.SHOW_ALL_BTN)
    product_list = search_page.get_products_list(By.XPATH, SearchPageLocators.PRODUCTS_PARENT_ELEMENT,
                                                 SearchPageLocators.PRODUCT_CHILD_ELEMENT)
    currency_sign = search_page.get_expected_currency_sign()

    errors = []
    for index, product in enumerate(product_list):
        price = product.text.replace(currency_sign, '').replace(' ', '')
        if '%' in price:
            percent = float(price.replace('%', '').replace('-', ''))
            old_price = float(product_list[index - 1].text.replace(' ', '').replace(currency_sign, '').replace(',', '.'))
            new_price = float(product_list[index - 2].text.replace(' ', '').replace(currency_sign, '').replace(',', '.'))
            expected_new_price = (old_price - (round(old_price / 100 * percent)))
            try:
                assert new_price == expected_new_price, f'New price is {new_price}, but should be {expected_new_price}'
            except AssertionError as e:
                errors.append(str(e))

    if errors:
        print('Errors list:')
        for error in errors:
            print(error)
    else:
        print('No errors')
