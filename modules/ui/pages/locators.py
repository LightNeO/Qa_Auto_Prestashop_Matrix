class MainPageLocators:
    MAIN_PAGE_URL = 'http://prestashop.qatestlab.com.ua'
    CURRENCY_SELECTOR = '//*[@id="setCurrency"]/div/strong'
    PARENT_ELEMENT_XPATH = '//*[@id="homefeatured"]'
    CHILD_ELEMENT_XPATH = './/li'
    CURRENCY_USD = '//*[@id="first-currencies"]/li[2]'
    CURRENCY_UAH = '//*[@id="first-currencies"]/li[1]'
    CURRENCY_EUR = '//*[@id="first-currencies"]/li[3]'
    SEARCH_ID = 'search_query_top'
    SEARCH_BTN = '//*[@id="searchbox"]/button'
    AMOUNT_OF_RESULTS_FOUND = '//*[@id="center_column"]/h1/span[2]'


class SearchPageLocators:
    AMOUNT_OF_ELEMENTS = '//*[@id="pagination"]/form/div/button'
    FOUND_ELEMENTS_CONTAINER = '//*[@id="center_column"]/ul'
