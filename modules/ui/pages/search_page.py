from modules.ui.pages.base_page import BasePage
from modules.ui.pages.locators import SearchPageLocators
from modules.ui.pages.locators import MainPageLocators
from modules.ui.pages.main_page import MainPage
from selenium.webdriver.common.by import By
import logging

logger = logging.getLogger(__name__)


class SearchPage(BasePage):

    def open_search_page(self, search_text):
        self.open(MainPageLocators.MAIN_PAGE_URL)
        self.enter_text(By.ID, MainPageLocators.SEARCH_ID, search_text)
        self.click(By.XPATH, MainPageLocators.SEARCH_BTN)
        logging.info(f'Search page opened for product {search_text}')






