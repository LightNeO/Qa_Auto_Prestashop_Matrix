class MainPageLocators:
    MAIN_PAGE_URL = 'http://prestashop.qatestlab.com.ua'
    CURRENCY_SELECTOR = '//*[@id="setCurrency"]/div/strong'
    PRODUCTS_PARENT_ELEMENT = '//*[@id="homefeatured"]'
    PRODUCT_CHILD_ELEMENT = './/li'
    CURRENCY_USD = '//*[@id="first-currencies"]/li[2]'
    CURRENCY_UAH = '//*[@id="first-currencies"]/li[1]'
    CURRENCY_EUR = '//*[@id="first-currencies"]/li[3]'
    SEARCH_ID = 'search_query_top'
    SEARCH_BTN = '//*[@id="searchbox"]/button'
    AMOUNT_OF_RESULTS_FOUND = '//*[@id="center_column"]/h1/span[2]'


class SearchPageLocators:
    SHOW_ALL_BTN = '//*[@id="pagination"]/form/div/button'
    FOUND_ELEMENTS_CONTAINER = '//*[@id="center_column"]/ul'
    SORT_BY_BTN = '//*[@id="uniform-selectProductSort"]'
    HIGH_TO_LOW_OPTION = '//*[@id="selectProductSort"]/option[3]'
    PRODUCTS_PARENT_ELEMENT = '//*[@id="center_column"]/ul'
    PRODUCT_CHILD_ELEMENT = './/li/div/div/div/span'
