from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from modules.ui.pages.locators import MainPageLocators
import time


class BasePage:

    def __init__(self, browser, wait):
        self.driver = browser
        self.wait = wait

    def open(self, url):
        self.driver.get(url)

    def find_element(self, byDotType, locator):
        return self.driver.find_element(byDotType, locator)

    def find_elements(self, byDotType, locator):
        return self.driver.find_elements(byDotType, locator)

    def wait_for_page_load(self, timeout=10):
        self.wait.until(
            lambda driver: driver.execute_script("return document.readyState") == "complete",
            f"Page did not load within {timeout} seconds")

    def wait_for_element_presence(self, byDotType, locator):
        value = (byDotType, locator)
        return self.wait.until(EC.presence_of_element_located(value))

    def wait_for_element_clickable(self, byDotType, locator):
        value = (byDotType, locator)
        return self.wait.until(EC.element_to_be_clickable(value))

    def click(self, byDotType, locator):
        element = self.wait_for_element_clickable(byDotType, locator)
        element.click()

    def enter_text(self, byDotType, locator, text):
        element = self.wait_for_element_presence(byDotType, locator)
        element.clear()
        element.send_keys(text)

    def set_currency(self, currency):
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
