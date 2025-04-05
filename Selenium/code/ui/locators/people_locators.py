from selenium.webdriver.common.by import By


class PeoplePageLocators:
    SEARCH_INPUT = (By.CLASS_NAME, 'input-text')
    SEARCH_SUBMIT_BTN = (By.CLASS_NAME, 'input-submit')
    SEARCH_RESULTS = (By.CSS_SELECTOR, 'td.cell-name')
    SEARCH_RESULT_USER_NAME = (By.CSS_SELECTOR, 'p.realname')
