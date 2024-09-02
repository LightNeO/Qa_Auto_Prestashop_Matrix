from modules.ui.pages.base_page import BasePage
from modules.ui.pages.locators import MainPageLocators
from selenium.webdriver.common.by import By

class MainPage(BasePage):

    def open_main_page(self):
        self.open(MainPageLocators.MAIN_PAGE_URL)

    def search_for_item(self, name):
        self.enter_text(By.ID, MainPageLocators.SEARCH_ID, name)
        self.click(By.XPATH, MainPageLocators.SEARCH_BTN)

    def get_currency_selector_value(self):
        return self.find_element(By.XPATH, MainPageLocators.CURRENCY_SELECTOR).text

    def get_products_list(self):
        parent_element = self.find_element(By.XPATH, MainPageLocators.PRODUCTS_PARENT_ELEMENT)
        child_elements = parent_element.find_elements(By.XPATH, MainPageLocators.PRODUCT_CHILD_ELEMENT)
        return child_elements

    def get_expected_currency_sign(self):
        currency_selector_text = self.get_currency_selector_value()

        if currency_selector_text == 'UAH':
            expected_currency_sign = '₴'
        elif currency_selector_text == 'USD':
            expected_currency_sign = '$'
        elif currency_selector_text == 'EUR':
            expected_currency_sign = '€'

        return expected_currency_sign
