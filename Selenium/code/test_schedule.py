from base import BaseCase
from ui.pages.schedule_page import ScheduleInterval, ScheduleDiscipline, ScheduleEventType


class TestSchedule(BaseCase):
    authorize = True

    def test_schedule(self):
        self.schedule_page.open()

        self.schedule_page.select_interval(ScheduleInterval.ENTIRE_SEMESTER)
        self.schedule_page.select_group('WEB-31')

        expected_event = {
            'title': 'End-to-End тесты на Python',
            'discipline': ScheduleDiscipline.QA.value,
            'location': '395 - зал 1,2 (МГТУ)',
            'event_type': f'{ScheduleEventType.SEMINAR.value} 2'
        }

        found_event = None
        schedule = self.schedule_page.parse_schedule()
        for event in schedule['3 апреля 2025']:
            if event['title'] == expected_event['title']:
                found_event = event
                break
        else:
            assert False, 'testing lesson not found in schedule'
 
        assert found_event == expected_event, f"expected event: '{expected_event}', got: '{found_event}'"
