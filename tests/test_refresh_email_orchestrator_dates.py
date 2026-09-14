import importlib.util
import json
import sys
import tempfile
import unittest
from datetime import datetime
from pathlib import Path
from unittest.mock import patch

SPEC = importlib.util.spec_from_file_location('email_orchestrator_dates', Path(__file__).resolve().parents[1] / 'scripts/refresh_email_orchestrator_status.py')
m = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = m
SPEC.loader.exec_module(m)

class FollowThroughDates(unittest.TestCase):
    def test_prior_day_filters_today_even_if_calendar_returns_it(self):
        def event(day, ident):
            return {'id': ident, 'summary': 'Mike I Kay', 'start': {'dateTime': f'2026-09-{day}T11:30:00-04:00'}, 'end': {'dateTime': f'2026-09-{day}T12:00:00-04:00'}}
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / 'backlog.json'
            path.write_text('{"items": []}')
            with patch.object(m, 'BACKLOG_PATH', path), patch.object(m, 'now_et', return_value=datetime(2026,9,14,2,45,tzinfo=m.DASHBOARD_TZ)), patch.object(m, 'run_gog_json', return_value={'events': [event('13','prior'), event('14','today')]}) as query:
                self.assertEqual(m.seed_prior_day_thank_yous(), 1)
                row = json.loads(path.read_text())['items'][0]
                self.assertEqual(row['calendar_event_id'], 'prior')
                self.assertEqual(row['event_end'], '2026-09-13T12:00:00-04:00')
                self.assertIn('2026-09-14T00:00:00-04:00', query.call_args.args[0])
                self.assertEqual(m.seed_prior_day_thank_yous(), 0)

    def test_pre_call_message_cannot_complete_thank_you(self):
        record = {'bucket':'thank','email':'verified@example.com','due_date':'2026-09-11','event_end':'2026-09-11T12:00:00-04:00'}
        with patch.object(m, 'run_gog_json', return_value={'threads':[{'id':'before','date':'2026-09-11 11:11'}, {'id':'after','date':'2026-09-11 12:15'}]}):
            self.assertEqual(m.sent_thread_after_due(record)['id'], 'after')
        self.assertFalse(m.email_evidence_completes(record, [{'date':'2026-09-11 11:11','to':'verified@example.com'}]))

    def test_unknown_legacy_time_does_not_complete(self):
        record = {'bucket':'thank','email':'verified@example.com','due_date':'2026-09-11'}
        with patch.object(m, 'run_gog_json', return_value={'threads':[{'id':'same-day','date':'2026-09-11 11:11'}]}):
            self.assertIsNone(m.sent_thread_after_due(record))
        self.assertFalse(m.thank_you_sent_after_event({'bucket':'thank','event_end':'2026-09-11T12:00:00-04:00'}, '2026-09-11'))

if __name__ == '__main__':
    unittest.main()
