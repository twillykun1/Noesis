"""Official installer integration using local source injection; never downloads."""
import contextlib
import hashlib
import importlib.util
import io
import os
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
INSTALLER = Path(os.environ.get('NOESIS_OFFICIAL_INSTALLER', Path.home() / '.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py'))

def hashes(directory):
    return {p.relative_to(directory).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in directory.rglob('*') if p.is_file()}

@unittest.skipUnless(INSTALLER.is_file(), 'official installer unavailable; local integration not run')
class OfficialInstallTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.repo = self.base / 'repo'
        self.repo.mkdir()
        self.assertTrue((ROOT / 'skills/noesis').is_dir(), 'canonical package is missing')
        shutil.copytree(ROOT / 'skills/noesis', self.repo / 'skills/noesis')
        spec = importlib.util.spec_from_file_location('noesis_official_installer', INSTALLER)
        self.module = importlib.util.module_from_spec(spec)
        with patch.dict(sys.modules, {spec.name: self.module}), patch.object(sys, 'path', [str(INSTALLER.parent)] + sys.path):
            spec.loader.exec_module(self.module)
        self.dest = self.base / 'installed'

    def install(self, path='skills/noesis', extra=()):
        # Only acquisition is substituted. All argument parsing, validation and copy are official.
        with patch.object(self.module, '_prepare_repo', return_value=str(self.repo)), contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            return self.module.main(['--repo', 'twillykun1/Noesis', '--path', path, '--dest', str(self.dest), *extra])

    def test_exact_copy_and_existing_destination_preserved(self):
        self.assertEqual(self.install(), 0)
        self.assertEqual(set(hashes(self.dest / 'noesis')), {'SKILL.md', 'examples/scenarios.md', 'references/review.md', 'references/complex-projects.md', 'templates/decision-record.md'})
        self.assertEqual(hashes(self.dest / 'noesis'), hashes(ROOT / 'skills/noesis'))
        sentinel = self.dest / 'noesis/sentinel'
        sentinel.write_text('keep')
        before = hashes(self.dest)
        self.assertEqual(self.install(), 1)
        self.assertEqual(hashes(self.dest), before)

    def test_unsafe_sources_and_names_rejected(self):
        outside = self.base / 'outside'
        outside.mkdir()
        (outside / 'SKILL.md').write_text('sentinel')
        before = hashes(outside)
        for path, extra in [('../outside', ()), (str(outside), ()), ('skills/noesis', ('--name', '../outside'))]:
            self.assertEqual(self.install(path, extra), 1)
        (self.repo / 'skills/link').symlink_to(outside, target_is_directory=True)
        self.assertEqual(self.install('skills/link'), 1)
        (self.repo / 'skills/noesis/escape').symlink_to(outside / 'SKILL.md')
        self.assertEqual(self.install(), 1)
        self.assertEqual(hashes(outside), before)
        self.assertFalse(self.dest.exists())
