from ui.pages.base_url import BASE_URL
from ui.pages.base_page import BasePage
from ui.locators.schedule_locators import SchedulePageLocators

from enum import Enum
from collections import defaultdict


class ScheduleInterval(Enum):
    TWO_WEEKS = 'near'
    ENTIRE_SEMESTER = 'semester'


class ScheduleDiscipline(Enum):
    QA = 'Обеспечение качества в разработке ПО'


class ScheduleEventType(Enum):
    LECTURE = 'Лекция'
    SEMINAR = 'Семинар'


class SchedulePage(BasePage):
    url = f'{BASE_URL}/schedule/'
    locators = SchedulePageLocators

    def select_interval(self, interval: ScheduleInterval):
        match interval:
            case ScheduleInterval.TWO_WEEKS:
                self.click(self.locators.TWO_WEEKS_INTERVAL)
            case ScheduleInterval.ENTIRE_SEMESTER:
                self.click(self.locators.ENTIRE_SEMESTER_INTERVAL)
    
    def select_group(self, group: str):
        self.find(self.locators.SCHEDULE)  # wait for locator
        
        self.click(self.locators.GROUP_SELECTOR)
        self.click(self.locators.GROUP_SELECTOR_OPTION(group))

    def parse_schedule(self):
        raw_schedule_items = self.find_all(self.locators.SCHEDULE_ITEM_TYPE)
        
        self.wait().until(lambda item: 'loading' not in item.find_element(*self.locators.SCHEDULE_LOADER).get_attribute('class'))
        self.wait().until(lambda item: item.find_elements(*self.locators.SCHEDULE_ITEM) != raw_schedule_items)
        
        raw_schedule_items = self.driver.find_elements(*self.locators.SCHEDULE_ITEM)

        schedule = defaultdict(list)
        for raw_schedule_item in raw_schedule_items:
            date = raw_schedule_item.find_element(*self.locators.SCHEDULE_ITEM_DATE).text.strip()
            schedule[date].append({
                'discipline': raw_schedule_item.find_element(
                        *self.locators.SCHEDULE_ITEM_DISCIPLINE
                    ).text.strip(),
                'title': raw_schedule_item.find_element(
                        *self.locators.SCHEDULE_ITEM_TITLE
                    ).text.strip(),
                'location': raw_schedule_item.find_element(
                        *self.locators.SCHEDULE_ITEM_LOCATION
                    ).text.strip(),
                'event_type': raw_schedule_item.find_element(
                        *self.locators.SCHEDULE_ITEM_TYPE
                    ).text.strip()
            })

        return schedule
