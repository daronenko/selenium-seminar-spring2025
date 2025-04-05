from selenium.webdriver.common.by import By


class SchedulePageLocators:
    TWO_WEEKS_INTERVAL = (By.XPATH, '//*[@intervalid="near"]')
    ENTIRE_SEMESTER_INTERVAL = (By.XPATH, '//*[@intervalid="semester"]')

    GROUP_SELECTOR = (By.CSS_SELECTOR, '.schedule-filters__item_group .r-input')
    GROUP_SELECTOR_OPTION = lambda group: (By.XPATH, f'//*[contains(@class, "option-label") and contains(text(), "{group}")]')

    SCHEDULE = (By.ID, 'react-schedule')
    SCHEDULE_LOADER = (By.CLASS_NAME, 'wrapper_schedule-timetable')
    SCHEDULE_ITEM = (By.CLASS_NAME, 'schedule-timetable__item')
    SCHEDULE_ITEM_TITLE = (By.CSS_SELECTOR, '.schedule-timetable__item__event strong')
    SCHEDULE_ITEM_DISCIPLINE = (By.CSS_SELECTOR, '.schedule-timetable__item__event span')
    SCHEDULE_ITEM_DATE = (By.CSS_SELECTOR, '.schedule-timetable__item__date strong')
    SCHEDULE_ITEM_LOCATION = (By.CSS_SELECTOR, '.schedule-timetable__item__event .schedule-auditorium')
    SCHEDULE_ITEM_TYPE = (By.CSS_SELECTOR, '.schedule-timetable__item__event .schedule-event-type')
