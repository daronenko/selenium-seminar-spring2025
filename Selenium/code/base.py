from ui.fixtures import *

import pytest
from _pytest.fixtures import FixtureRequest


class BaseCase:
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config
        
        if self.authorize:
            login_page = request.getfixturevalue('login_page')
            credentials = request.getfixturevalue('credentials')
            login_page.login(
                credentials['email'],
                credentials['password'],
            )
        