"""Daily maintenance must preserve the approved expanded habits and overflow."""
import contextlib
import importlib.util
import io
import os
from pathlib import Path
import re
from types import SimpleNamespace
import unittest
from unittest.mock import patch

os.environ.setdefault('TRACKER_SHEET_ID', 'offline-test')
spec = importlib.util.spec_from_file_location('tracker_daily', Path(__file__).parents[1] / 'scripts/task_tracker.py')
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def frame(header=22, notes=92):
    rows = [[] for _ in range(notes + 3)]
    rows[4] = [True, 'Habit']
    rows[18] = [True, 'Focus']
    rows[header - 1] = m.DAY_HEADERS[:]
    rows[notes - 1] = ['NOTES']
    rows[notes] = ['Keep my notes']
    return rows


class Client:
    sheet_id = 'offline-test'
    def __init__(self, grids):
        self.grids = grids
        self.writes = []
    def get_metadata(self):
        return {'sheets': [{'properties': {'title': name, 'sheetId': i, 'gridProperties': {'rowCount': len(rows)}}} for i, (name, rows) in enumerate(self.grids.items())]}
    def get_values(self, address):
        name, cells = address.split('!')
        rows = self.grids.get(name.strip("'"), [])
        match = re.fullmatch(r'([A-Z]+)(\d*):([A-Z]+)(\d*)', cells)
        c1, r1, c2, r2 = match.groups()
        return [row[ord(c1)-65:ord(c2)-64] for row in rows[int(r1 or 1)-1:int(r2 or len(rows))]]
    def values_update(self, address, values):
        self.writes.append((address, values))
    def batch_update(self, requests):
        self.writes.extend(requests)


class DailyLayoutTests(unittest.TestCase):
    def test_legacy_expanded_and_overflow(self):
        c = Client({'Sun': frame(20, 71), 'Thu': frame(22, 105)})
        self.assertEqual(m._require_day_task_layout(c, ['Sun', 'Thu']), {'Sun': (21,70), 'Thu': (23,104)})

    def test_reject_malformed_and_ambiguous_before_write(self):
        variants = [frame(), frame(), frame(), frame()]
        variants[0][21] = ['Task']
        variants[1][19] = m.DAY_HEADERS[:]
        variants[2][91] = []
        variants[3][94] = ['NOTES']
        for rows in variants:
            c = Client({'Thu': rows})
            with self.assertRaises(SystemExit):
                m._require_day_task_layout(c, ['Thu'])
            self.assertEqual(c.writes, [])

    def test_carry_dry_run_includes_overflow_excludes_habits_focus_done_notes(self):
        src, dst = frame(22, 100), frame(20, 71)
        src[22] = [True, 'Done']
        src[90] = [False, 'Overflow']
        src[91] = [False, 'Duplicate']
        dst[20] = [False, 'duplicate']
        c = Client({'Wed': src, 'Thu': dst})
        output = io.StringIO()
        with patch.object(m, 'SheetsClient', return_value=c), contextlib.redirect_stdout(output):
            self.assertEqual(m.cmd_carry_forward_day(SimpleNamespace(date='2026-09-10', from_day='Wed', to_day='Thu', dry_run=True)), 0)
        text = output.getvalue()
        self.assertIn('Would move: 2', text)
        self.assertIn('Thu slot 2: Overflow', text)
        self.assertIn('already exists on Thu', text)
        for excluded in ['Habit', 'Focus', 'Keep my notes', ': Done']:
            self.assertNotIn(excluded, text)
        self.assertEqual(c.writes, [])

    def test_pack_writes_only_detected_task_region(self):
        rows = frame(22,100)
        rows[90] = [True, 'Done', 'Work', 'G&B', 'Metadata']
        c = Client({'Wed': rows})
        m._pack_day_tab_checked_rows(c, 'Wed')
        address, values = c.writes[0]
        self.assertEqual(address, "'Wed'!A23:E99")
        self.assertEqual(values[0], [True, 'Done', 'Work', 'G&B', 'Metadata'])
        self.assertEqual(len(values),77)

    def test_report_uses_same_overflow_boundary(self):
        rows = frame(22,100)
        rows[90] = [False, 'Overflow']
        c = Client({'Wed': rows})
        output = io.StringIO()
        with patch.object(m, 'SheetsClient', return_value=c), contextlib.redirect_stdout(output):
            m.cmd_report(SimpleNamespace())
        self.assertIn('Wed (1 incomplete)', output.getvalue())
        self.assertIn('Overflow', output.getvalue())
        self.assertNotIn('Keep my notes', output.getvalue())

    def test_sync_checks_overflow_preserves_recurring(self):
        rows = frame(22,100)
        rows[90] = [True,'Overflow']
        rows[91] = [True,'Recurring']
        c = Client({'Wed': rows, 'To Do': [m.TODO_HEADERS, ['Not Completed','Overflow'], ['On-going','Recurring','','','','','Weekly Recurring Wed']]})
        output = io.StringIO()
        with patch.object(m, 'snapshot_ranges', return_value='offline'), contextlib.redirect_stdout(output):
            m.cmd_sync_done_status(SimpleNamespace(dry_run=True), _client=c)
        self.assertIn('Slots checked TRUE: 2', output.getvalue())
        self.assertIn('To Do rows WOULD sync: 1', output.getvalue())
        self.assertEqual(c.writes, [])


if __name__ == '__main__':
    unittest.main()
