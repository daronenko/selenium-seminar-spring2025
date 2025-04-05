from base import BaseCase


class TestPeople(BaseCase):
    authorize = True

    USER_NAME = 'Илья Денисенко'

    def test_search(self):
        self.people_page.open()
        found_people = self.people_page.search(self.USER_NAME)
        assert self.USER_NAME in found_people
