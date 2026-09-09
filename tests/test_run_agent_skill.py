import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest


RUNNER = Path(__file__).resolve().parents[1] / 'scripts/run-agent-skill.sh'


class ScheduledRunnerTest(unittest.TestCase):
    def run_fixture(self, job='niche-intelligence:monday', **overrides):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'scripts').mkdir()
            shutil.copy2(RUNNER, root / 'scripts/run-agent-skill.sh')
            (root / 'scripts/load-env.sh').write_text('load_env() { :; }\n')
            (root / 'scripts/validate_niche_intelligence_integrity.py').write_text('raise SystemExit(0)\n')
            skill = root / '.agents/skills/niche-intelligence'
            skill.mkdir(parents=True)
            (skill / 'headless-monday-prompt.md').write_text('Recover the report.\n')
            binary = root / 'bin'
            binary.mkdir()
            stub = binary / 'codex'
            stub.write_text('''#!/usr/bin/env python3
import json, os, pathlib, sys
record = pathlib.Path(os.environ['PROBE_RECORD'])
rows = json.loads(record.read_text()) if record.exists() else []
rows.append({'model': sys.argv[sys.argv.index('--model') + 1], 'prompt': sys.stdin.read()})
record.write_text(json.dumps(rows))
if os.environ.get('FAIL_FIRST') == '1' and len(rows) == 1:
    print('Selected model is at capacity')
    sys.exit(1)
sys.exit(int(os.environ.get('STUB_EXIT', '0')))
''')
            stub.chmod(0o755)
            curl = binary / 'curl'
            curl.write_text('#!/bin/sh\ntouch "$CURL_RECORD"\n')
            curl.chmod(0o755)
            env = {'PATH': str(binary) + ':/usr/bin:/bin', 'HOME': str(root),
                   'PROBE_RECORD': str(root / 'calls.json'),
                   'CURL_RECORD': str(root / 'curl-called'),
                   'CODEX_HEAVY_MODEL': 'gpt-5.5'}
            env.update(overrides)
            result = subprocess.run(['bash', str(root / 'scripts/run-agent-skill.sh'),
                                     job], env=env,
                                    text=True, capture_output=True, timeout=15)
            calls = json.loads((root / 'calls.json').read_text())
            return result, calls, (root / 'curl-called').exists()

    def test_legacy_heavy_setting_uses_verified_replacement(self):
        result, calls, _ = self.run_fixture()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(calls[0]['model'], 'gpt-6-astra')

    def test_explicit_model_is_preserved(self):
        _, calls, _ = self.run_fixture(CODEX_MODEL='explicit-model')
        self.assertEqual(calls[0]['model'], 'explicit-model')

    def test_legacy_routine_setting_uses_verified_replacement(self):
        result, calls, _ = self.run_fixture(job='test-routine', CODEX_ROUTINE_MODEL='gpt-5.4-mini')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(calls[0]['model'], 'gpt-5.6-luna')

    def test_capacity_fallback_does_not_reuse_rejected_model(self):
        result, calls, _ = self.run_fixture(CODEX_MODEL='capacity-model', FAIL_FIRST='1',
                                          CODEX_FALLBACK_MODEL='gpt-5.5')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual([call['model'] for call in calls], ['capacity-model', 'gpt-6-astra'])

    def test_supervised_failure_does_not_notify(self):
        result, calls, notified = self.run_fixture(SAPLING_NO_NOTIFICATIONS='1',
                                                   SLACK_WEBHOOK_OPERATIONS='https://invalid.test',
                                                   STUB_EXIT='1')
        self.assertEqual(result.returncode, 1)
        self.assertFalse(notified)
        self.assertIn('Do not send Slack, email', calls[0]['prompt'])


if __name__ == '__main__':
    unittest.main()
