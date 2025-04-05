from base import BaseCase
from ui.pages.people_page import PeoplePage
from ui.fixtures import *

from _pytest.fixtures import FixtureRequest


class TestPeople(BaseCase):
    authorize = True

    USER_NAME = 'Илья Денисенко'

    def test_search(self, request: FixtureRequest):
        people_page = request.getfixturevalue('people_page')
        
        people_page.open()
        found_people = people_page.search(self.USER_NAME)
        
        assert self.USER_NAME in found_people, f"user '{self.USER_NAME}' not found in search results: '{found_people}'"
