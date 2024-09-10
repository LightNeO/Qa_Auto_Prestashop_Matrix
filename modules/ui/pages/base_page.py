from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from modules.ui.pages.locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
import time
import logging

logger = logging.getLogger(__name__)


class BasePage:

    def __init__(self, browser, wait):
        self.driver = browser
        self.wait = wait
        logging.info('Driver initialized')

    def open(self, url):
        self.driver.get(url)
        logging.info(f'Open page: {url}')

    def find_element(self, byDotType, locator):
        logging.info(f'Searching for element: {locator}')
        return self.driver.find_element(byDotType, locator)

    def find_elements(self, byDotType, locator):
        logging.info('Searching for elements')
        return self.driver.find_elements(byDotType, locator)

    def wait_for_page_load(self, timeout=10):
        logging.info(f'Waiting for page to be loaded. Timeout: {timeout}sec')
        self.wait.until(
            lambda driver: driver.execute_script("return document.readyState") == "complete",
            f"Page did not load within {timeout} seconds")

    def wait_for_element_presence(self, byDotType, locator):
        logging.info(f'Waiting for element {locator} to be present')
        value = (byDotType, locator)
        return self.wait.until(EC.presence_of_element_located(value))

    def wait_for_element_clickable(self, byDotType, locator):
        logging.info(f'Waiting for element {locator} to be clickable')
        value = (byDotType, locator)
        return self.wait.until(EC.element_to_be_clickable(value))

    def click(self, byDotType, locator):
        logging.info(f'Click on {locator}')
        element = self.wait_for_element_clickable(byDotType, locator)
        element.click()

    def enter_text(self, byDotType, locator, text):
        logging.info(f'Entering text {text} into {locator}')
        element = self.wait_for_element_presence(byDotType, locator)
        element.clear()
        element.send_keys(text)

    def set_currency(self, currency):
        logging.info(f'Changing currency to {currency}')
        ALLOWED_CURRENCIES = ['USD', 'EUR', 'UAH']
        self.click(By.XPATH, MainPageLocators.CURRENCY_SELECTOR)

        if currency == 'USD':
            self.click(By.XPATH, MainPageLocators.CURRENCY_USD)
        elif currency == 'UAH':
            self.click(By.XPATH, MainPageLocators.CURRENCY_USD)
        elif currency == 'EUR':
            self.click(By.XPATH, MainPageLocators.CURRENCY_USD)
        else:
            raise ValueError(f"Currency '{currency}' is not allowed. Choose from {', '.join(ALLOWED_CURRENCIES)}.")
        self.wait_for_page_load()

    def get_currency_selector_value(self, byDotType, locator):
        logging.info('Getting currency value')
        return self.find_element(byDotType, locator).text

    def get_expected_currency_sign(self):
        currency_selector_text = self.get_currency_selector_value(By.XPATH, MainPageLocators.CURRENCY_SELECTOR)

        logging.info(f'Getting expected currency sign for currency {currency_selector_text}')

        if currency_selector_text == 'UAH':
            expected_currency_sign = '₴'
        elif currency_selector_text == 'USD':
            expected_currency_sign = '$'
        elif currency_selector_text == 'EUR':
            expected_currency_sign = '€'

        return expected_currency_sign

    def get_products_list(self, byDotType, parent_locator, child_locator):
        logging.info(f'Getting product list')
        parent_element = self.find_element(byDotType, parent_locator)
        child_elements = parent_element.find_elements(byDotType, child_locator)
        return child_elements
