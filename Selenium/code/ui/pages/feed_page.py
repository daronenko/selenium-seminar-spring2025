from ui.pages.base_url import BASE_URL
from ui.pages.base_page import BasePage

from selenium.webdriver.support import expected_conditions as EC


class FeedPage(BasePage):
    url = f'{BASE_URL}/feed/'
