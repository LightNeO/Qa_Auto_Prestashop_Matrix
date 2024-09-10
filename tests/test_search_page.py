from modules.ui.pages.search_page import SearchPage
from selenium.webdriver.common.by import By
from modules.ui.pages.locators import SearchPageLocators
import logging

logger = logging.getLogger(__name__)


def test_sorting_by_price(browser, wait):
    logger.info("Starting test: test_sorting_by_price")
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

    assert prices == sorted(prices, reverse=True), "Not all products are sorted by price."
    logger.info("Test passed: All products are sorted by price.")


def test_discount_price(browser, wait):
    logger.info("Starting test: test_discount_price")
    search_page = SearchPage(browser, wait)
    search_page.open_search_page('dress')

    search_page.click(By.XPATH, SearchPageLocators.SORT_BY_BTN)
    search_page.click(By.XPATH, SearchPageLocators.HIGH_TO_LOW_OPTION)
    search_page.click(By.XPATH, SearchPageLocators.SHOW_ALL_BTN)
    product_list = search_page.get_products_list(By.XPATH, SearchPageLocators.PRODUCTS_PARENT_ELEMENT,
                                                 SearchPageLocators.PRODUCT_CHILD_ELEMENT)
    currency_sign = search_page.get_expected_currency_sign()

    errors = []

    logger.info(f"Checking discount prices for products with currency sign: {currency_sign}")
    for index, product in enumerate(product_list):
        price = product.text.replace(currency_sign, '').replace(' ', '')
        if '%' in price:
            percent = float(price.replace('%', '').replace('-', ''))
            old_price = float(product_list[index - 1].text.replace(' ', '').replace(currency_sign, '').replace(',', '.'))
            new_price = float(product_list[index - 2].text.replace(' ', '').replace(currency_sign, '').replace(',', '.'))
            expected_new_price = (old_price - (round(old_price / 100 * percent)))

            if new_price == expected_new_price:
                success_message = (f'Product {index}: New price {new_price} matches expected price {expected_new_price}.')
                logger.info(success_message)
            else:
                error_message = (f'Product {index}: New price {new_price} does NOT match expected price {expected_new_price}.')
                logger.error(error_message)
                errors.append(error_message)

    if errors:
        logger.error('Discount price validation failed with the following errors:')
        for error in errors:
            logger.error(error)
        assert False, "There are errors in discount price calculations. Check logs for details."
    else:
        logger.info("Test passed: Discount prices are calculated correctly.")
