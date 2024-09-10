import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import logging


def pytest_configure(config):
    logging.basicConfig(filename="D:\\.QA\\Qa_Auto_Prestashop_Matrix\\logs\\driver_actions.log",
                        level=logging.INFO, filemode='w',
                        format='%(asctime)s - %(levelname)s - %(message)s')


@pytest.fixture(scope='session')
def browser(request):
    browser_name = request.config.getoption('--browser')

    if browser_name == 'chrome':
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser_name == 'firefox':
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        raise ValueError(f'{browser_name} is not supported')

    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def wait(browser):
    return WebDriverWait(browser, 500)


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to use for tests: chrome or firefox"
    )
