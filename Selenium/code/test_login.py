from base import BaseCase
from ui.pages.feed_page import FeedPage
from ui.fixtures import *

from _pytest.fixtures import FixtureRequest


class TestLogin(BaseCase):
    authorize = False

    def test_login(self, request: FixtureRequest, credentials):
        login_page = request.getfixturevalue('login_page')

        login_page.login(
             credentials['email'],
             credentials['password'],
        )

        assert self.driver.current_url == FeedPage.url, f"failed to login with credentials: '{credentials}'"
