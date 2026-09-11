import importlib.util
import json
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

spec = importlib.util.spec_from_file_location('archive_export', Path(__file__).parents[1] / 'scripts/export_weekly_archive_to_sheet.py')
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

class ArchiveGrowthTests(unittest.TestCase):
    def metadata(self, count):
        return SimpleNamespace(returncode=0, stdout=json.dumps({'sheets':[{'properties':{'title':'Weekly Topline','gridProperties':{'columnCount':count}}}]}), stderr='')

    def test_append_after_z_preserves_existing_columns(self):
        with patch.object(mod.subprocess, 'run', side_effect=[self.metadata(26), SimpleNamespace(returncode=0)]) as run:
            mod._ensure_column_capacity(27)
            args = run.call_args.args[0]
            self.assertEqual(args[-5:], ['columns','26','--after','--count','1'])

    def test_existing_capacity_never_mutated(self):
        with patch.object(mod.subprocess, 'run', return_value=self.metadata(28)) as run:
            mod._ensure_column_capacity(28)
            self.assertEqual(run.call_count, 1)

    def test_aa_header_visible_for_idempotency(self):
        headers = ['title'] + ['old']*25 + ['Week ending 9/4/26']
        with patch.object(mod, '_gog_get', return_value=[headers]) as get:
            actual = mod._existing_headers()
            get.assert_called_once_with("'Weekly Topline'!1:1")
        self.assertEqual(mod._find_existing_column_idx(actual, 'Week ending 9/4/26'), 27)
        self.assertEqual(mod._next_empty_column_idx(actual), 28)

    def test_failed_growth_does_not_continue(self):
        with patch.object(mod.subprocess, 'run', side_effect=[self.metadata(26), SimpleNamespace(returncode=1, stderr='failure')]):
            with self.assertRaises(RuntimeError):
                mod._ensure_column_capacity(27)

    def test_readback_normalizes_empty_rows(self):
        self.assertEqual(mod._normalize_column([["week"], [], [], [1]], 5),
                         [["week"], [""], [""], ["1"], [""]])
