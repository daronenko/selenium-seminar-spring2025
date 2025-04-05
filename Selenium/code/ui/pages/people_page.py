from ui.pages.base_url import BASE_URL
from ui.pages.base_page import BasePage
from ui.locators.people_locators import PeoplePageLocators

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC


class PeoplePage(BasePage):
    url = f'{BASE_URL}/people/'
    locators = PeoplePageLocators

    def search(self, name):
        self.find(self.locators.SEARCH_INPUT).send_keys(name, Keys.ENTER)
        self.wait().until(EC.presence_of_all_elements_located(self.locators.SEARCH_RESULTS))

        user_names = []
        search_results = self.find_all(self.locators.SEARCH_RESULTS)

        for raw_user in search_results:
            user_name = raw_user.find_element(*self.locators.SEARCH_RESULT_USER_NAME).text.strip()
            user_names.append(user_name)

        return user_names
        
