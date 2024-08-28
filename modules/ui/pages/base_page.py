from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

    def wait_for_element_presence(self, byDotType, locator):
        value = (byDotType, locator)
        return self.wait.untill(EC.presence_of_element_located(value))

    def click(self, locator):
        element = self.wait_for_element_presence(locator)
        element.click()

    def enter_text(self, locator, text):
        element = self.wait_for_element_presence(locator)
        element.clear()
        element.send_keys(text)
