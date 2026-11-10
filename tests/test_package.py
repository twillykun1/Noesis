"""Standalone release package tests; no unpublished helpers."""
import importlib.util
from pathlib import Path
import shutil
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]

class PackageTests(unittest.TestCase):
    def checker(self):
        path = ROOT / 'scripts/check_package.py'
        self.assertTrue(path.is_file(), 'standalone package checker is missing')
        spec = importlib.util.spec_from_file_location('noesis_package', path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    def test_candidate_is_self_contained(self):
        self.assertTrue((ROOT / 'skills/noesis/SKILL.md').is_file(), 'canonical package is missing')
        self.assertTrue((ROOT / 'skills/noesis/references/complex-projects.md').is_file())
        self.assertTrue((ROOT / 'skills/noesis/references/preferences.md').is_file())
        self.assertIn('version: "0.4.0"', (ROOT / 'skills/noesis/SKILL.md').read_text())
        with tempfile.TemporaryDirectory() as tmp:
            package = Path(tmp) / 'noesis'
            shutil.copytree(ROOT / 'skills/noesis', package)
            self.assertEqual(self.checker().check(package), [])

    def test_rejects_unsafe_or_incomplete_package(self):
        checker = self.checker()
        with tempfile.TemporaryDirectory() as tmp:
            package = Path(tmp) / 'noesis'
            shutil.copytree(ROOT / 'skills/noesis', package)
            source = package / 'SKILL.md'
            original = source.read_text()
            for content in ('no frontmatter', original.replace('name: noesis', 'name: other'),
                            original + '\n[escape](../../private.md)',
                            original + '\n[escape][x]\n[x]: ../../private.md',
                            original.replace('description: Use when', 'description: Always'),
                            original.replace('description: Use when', 'description: Use when context:')):
                source.write_text(content)
                self.assertTrue(checker.check(package))
            source.write_bytes(b'\xff')
            self.assertTrue(checker.check(package))
            source.write_text(original)
            (package / 'private.txt').write_text('not distributable')
            self.assertTrue(checker.check(package))
            (package / 'private.txt').unlink()
            (package / 'examples/scenarios.md').unlink()
            (package / 'examples/scenarios.md').symlink_to(source)
            self.assertTrue(checker.check(package))
