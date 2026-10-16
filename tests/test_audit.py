"""Regression checks for defects reproduced during the repository audit."""
import copy
from pathlib import Path
import subprocess
import sys
import unittest
import tempfile
import shutil
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
import build
import physics
import validate as evidence


class EvidenceValidationTests(unittest.TestCase):
    def setUp(self):
        self.data = {name: evidence.load(name) for name in ('meta', 'sources', 'claims', 'timeline', 'audit')}

    def check(self, data=None, *, audit=False):
        return evidence.validate(data=self.data if data is None else data, check_links=False, check_audit=audit)

    def test_missing_id_is_reported_without_crash(self):
        del self.data['sources'][0]['id']
        self.assertTrue(any('missing' in error for error in self.check()))

    def test_wrong_json_shapes_are_reported_without_crash(self):
        for name, value in [('sources', {}), ('claims', [None]), ('timeline', [{'date': None}])]:
            with self.subTest(name=name):
                damaged = copy.deepcopy(self.data)
                damaged[name] = value
                self.assertTrue(self.check(damaged))
        self.assertTrue(self.check(['invalid top-level array']))

    def test_invalid_source_array_and_missing_reference(self):
        self.data['claims'][0]['sources'] = 'S01'
        self.assertTrue(any('array' in error for error in self.check()))
        self.data['claims'][0]['sources'] = ['S999']
        self.assertTrue(any('unresolved source' in error for error in self.check()))

    def test_reporter_cannot_be_a_primary_manufacturer_source(self):
        self.data['claims'][0]['sources'] = ['S06']
        self.assertTrue(any('primary source' in error for error in self.check()))

    def test_blocked_and_stale_citations_cannot_support_active_claims(self):
        for identifier in ('S05', 'S41'):
            with self.subTest(source=identifier):
                self.data['claims'][0]['sources'] = [identifier]
                self.assertTrue(any('inactive/unread' in error for error in self.check()))

    def test_future_event_must_remain_target(self):
        self.data['timeline'][-1]['kind'] = 'observation'
        self.assertTrue(any('future event' in error for error in self.check()))

    def test_dates_and_credentials_are_validated(self):
        self.data['sources'][0]['published'] = 2026
        self.data['sources'][0]['url'] = 'https://user:secret@example.com/source'
        issues = self.check()
        self.assertTrue(any('publication' in error for error in issues))
        self.assertTrue(any('HTTPS' in error for error in issues))

    def test_changed_claim_requires_a_new_review(self):
        self.data['claims'][0]['statement'] = 'An unsupported replacement statement.'
        self.assertTrue(any('stale review of C01' in error for error in self.check(audit=True)))


class RenderingRegressionTests(unittest.TestCase):
    def test_escaped_table_pipe_stays_in_its_cell(self):
        rendered = build.markdown('| A | B |\n|---|---|\n| X \\| Y | Z |', build.ROOT/'docs/testing.md')
        self.assertIn('<td>X | Y</td><td>Z</td>', rendered)

    def test_readme_fragment_is_not_discarded(self):
        target = build.destination('../README.md#explore-locally', build.ROOT/'docs/testing.md')
        self.assertTrue(target.endswith('README.md#explore-locally'))

    def test_protocol_relative_link_and_unsafe_scheme(self):
        self.assertEqual(build.destination('//example.com/a', build.ROOT/'docs/testing.md'), 'https://example.com/a')
        self.assertEqual(build.destination('javascript:alert(1)', build.ROOT/'docs/testing.md'), '#')

    def test_url_encoded_local_paths_and_outside_paths(self):
        self.assertEqual(build.destination('../docs/start%2Dhere.md', build.ROOT/'docs/testing.md'), 'guide-docs-start-here.html')
        with self.assertRaisesRegex(ValueError, 'escapes'):
            build.destination('../../../outside.md', build.ROOT/'docs/testing.md')

    def test_html_in_source_text_is_escaped(self):
        rendered = build.inline('<img src=x onerror=alert(1)>', build.ROOT/'docs/testing.md')
        self.assertNotIn('<img', rendered)
        self.assertIn('&lt;img', rendered)

    def test_mermaid_content_is_preserved_instead_of_replaced(self):
        rendered = build.markdown('```mermaid\nflowchart LR\n A --> B\n```', build.ROOT/'docs/testing.md')
        self.assertIn('A --&gt; B', rendered)
        self.assertNotIn('Stored gas', rendered)

    def test_footer_uses_edition_metadata(self):
        with patch.object(build, 'load', return_value={'cutoff': '2027-01-02', 'repository': 'https://example.com/repo'}):
            self.assertIn('02 Jan 2027', build.shell('Title', 'Body'))

    def test_generated_anchor_failure_is_detected(self):
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            (directory/'index.html').write_text('<a href="chapter.html#missing">Read</a>')
            (directory/'chapter.html').write_text('<h1 id="real">Chapter</h1>')
            self.assertTrue(any('missing generated anchor' in item for item in build.validate_site(directory)))

    def test_rebuild_removes_only_obsolete_owned_pages(self):
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)/'fixture'
            shutil.copytree(build.ROOT, directory, ignore=shutil.ignore_patterns('.git', 'dist', '__pycache__'))
            extra = directory/'docs/audit-fixture.md'
            extra.write_text('# Temporary chapter\n')
            with patch.object(build, 'ROOT', directory), patch.object(build, 'OUT', directory/'site/dist'), patch.object(sys, 'argv', ['build.py']):
                build.main()
                output = build.OUT/'guide-docs-audit-fixture.html'
                self.assertTrue(output.exists())
                unrelated = build.OUT/'user-note.txt'
                unrelated.write_text('Preserve me')
                extra.unlink()
                build.main()
                self.assertFalse(output.exists())
                self.assertEqual(unrelated.read_text(), 'Preserve me')


class OverflowRegressionTests(unittest.TestCase):
    def test_finite_inputs_cannot_return_nonfinite_results(self):
        cases = [(physics.acceleration, (1e-300, 1e300, 1e300)), (physics.drag, (1e300, 1)),
                 (physics.suction, (1e308, 1e308)), (physics.range_estimate, (1e308, 1))]
        for function, args in cases:
            with self.subTest(function=function.__name__), self.assertRaisesRegex(ValueError, 'numerical range'):
                function(*args)

    def test_overflow_cli_has_actionable_error_without_traceback(self):
        result = subprocess.run([sys.executable, str(build.ROOT/'tools/physics.py'), 'range', '--usable-kwh', '1e308', '--wh-per-km', '1'], text=True, capture_output=True)
        self.assertEqual(result.returncode, 2)
        self.assertIn('numerical range', result.stderr)
        self.assertNotIn('Traceback', result.stderr)


if __name__ == '__main__':
    unittest.main()
