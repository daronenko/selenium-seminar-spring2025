from ui.pages.login_page import LoginPage
from ui.pages.feed_page import FeedPage
from ui.pages.people_page import PeoplePage
from ui.pages.schedule_page import SchedulePage

import pytest
from _pytest.fixtures import FixtureRequest


class BaseCase:
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config
        
        self.login_page = LoginPage(driver)
        self.feed_page = FeedPage(driver)
        self.people_page = PeoplePage(driver)
        self.schedule_page = SchedulePage(driver)

        if self.authorize:
            credentials = request.getfixturevalue('credentials')
            self.login_page.login(
                credentials['email'],
                credentials['password'],
            )
        