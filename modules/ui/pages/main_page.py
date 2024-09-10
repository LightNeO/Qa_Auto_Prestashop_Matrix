from modules.ui.pages.base_page import BasePage
from modules.ui.pages.locators import MainPageLocators
from selenium.webdriver.common.by import By
import logging

logger = logging.getLogger(__name__)


class MainPage(BasePage):

    def open_main_page(self):
        self.open(MainPageLocators.MAIN_PAGE_URL)
        logging.info('Main page opened')

    def search_for_item(self, name):
        logging.info(F'Searching for product {name}')
        self.enter_text(By.ID, MainPageLocators.SEARCH_ID, name)
        self.click(By.XPATH, MainPageLocators.SEARCH_BTN)
