from modules.ui.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    MAIN_PAGE_URL = 'http://prestashop.qatestlab.com.ua'
    CURRENCY_SELECTOR = '//*[@id="setCurrency"]/div/strong'
    PARENT_ELEMENT_XPATH = '//*[@id="homefeatured"]'
    CHILD_ELEMENT_XPATH = './/li'
    def open_main_page(self):
        self.open(self.MAIN_PAGE_URL)

