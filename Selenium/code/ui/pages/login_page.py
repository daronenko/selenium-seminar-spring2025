from ui.pages.base_url import BASE_URL
from ui.pages.base_page import BasePage
from ui.pages.feed_page import FeedPage
from ui.locators.login_locators import LoginPageLocators

from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):
    url = f'{BASE_URL}/'
    locators = LoginPageLocators

    def login(self, email, password):
        self.click(self.locators.LOGIN_BTN)
        self.click(self.locators.CONTINUE_WITH_CREDS_BTN)
        self.find(self.locators.EMAIL_INPUT).send_keys(email)
        self.find(self.locators.PASSWORD_INPUT).send_keys(password)
        self.click(self.locators.SUBMIT_BTN)

        self.wait().until(EC.url_to_be(FeedPage.url))
