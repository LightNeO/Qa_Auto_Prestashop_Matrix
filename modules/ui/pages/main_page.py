from modules.ui.pages.base_page import BasePage
from modules.ui.pages.locators import MainPageLocators
from selenium.webdriver.common.by import By

class MainPage(BasePage):

    def open_main_page(self):
        self.open(MainPageLocators.MAIN_PAGE_URL)

    def search_for_item(self, name):
        self.enter_text(By.ID, MainPageLocators.SEARCH_ID, 'dress')
        self.click(By.XPATH, MainPageLocators.SEARCH_BTN)

