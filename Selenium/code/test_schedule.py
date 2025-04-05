from base import BaseCase
from ui.pages.schedule_page import ScheduleInterval, ScheduleDiscipline, ScheduleEventType
from ui.fixtures import *

from _pytest.fixtures import FixtureRequest


class TestSchedule(BaseCase):
    authorize = True

    EVENT_DATE = '3 апреля 2025'

    EXPECTED_EVENT_TITLE = 'End-to-End тесты на Python'
    EXPECTED_EVENT_LOCATION = '395 - зал 1,2 (МГТУ)'
    EXPECTED_EVENT_TYPE = f'{ScheduleEventType.SEMINAR.value} 2'

    def test_schedule(self, request: FixtureRequest):
        schedule_page = request.getfixturevalue('schedule_page')

        schedule_page.open()

        schedule_page.select_interval(ScheduleInterval.ENTIRE_SEMESTER)
        schedule_page.select_group('WEB-31')

        expected_event = {
            'title': TestSchedule.EXPECTED_EVENT_TITLE,
            'discipline': ScheduleDiscipline.QA.value,
            'location': TestSchedule.EXPECTED_EVENT_LOCATION,
            'event_type': TestSchedule.EXPECTED_EVENT_TYPE,
        }

        found_event = None
        schedule = schedule_page.parse_schedule()
        for event in schedule[TestSchedule.EVENT_DATE]:
            if event['title'] == expected_event['title']:
                found_event = event
                break
        else:
            assert False, 'testing lesson not found in schedule'
 
        assert found_event == expected_event, f"expected event: '{expected_event}', got: '{found_event}'"
