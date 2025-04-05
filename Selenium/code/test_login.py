from base import BaseCase
from ui.pages.feed_page import FeedPage


class TestLogin(BaseCase):
    authorize = False

    def test_login(self, credentials):
        self.login_page.login(
             credentials['email'],
             credentials['password'],
        )
        assert self.driver.current_url == FeedPage.url
