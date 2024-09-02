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
    time.sleep(1)
    product_list = search_page.get_products_list()
    currency_sign = search_page.get_expected_currency_sign()

    prices = []
    for product in product_list:
        price = float(product.text.replace(currency_sign, '').replace(',', '').replace(' ', ''))
        prices.append(price)

    assert prices == sorted(prices, reverse=True)
