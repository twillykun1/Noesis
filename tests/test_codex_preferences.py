"""Check real Codex instruction discovery with fictional, isolated user files.

No model call, credential copy, or modification of the user's CODEX_HOME.
These checks prove prompt assembly only, not later model compliance.
"""
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

CODEX = os.environ.get("NOESIS_CODEX_CLI") or shutil.which("codex")

@unittest.skipUnless(CODEX, "Codex CLI unavailable; native prompt assembly not tested")
class CodexPreferenceLoadingTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="noesis-codex-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.home = self.root / "private-codex-home"
        self.project = self.root / "project"
        self.home.mkdir()
        self.project.mkdir()
        self.env = dict(os.environ, CODEX_HOME=str(self.home))

    def render(self):
        result = subprocess.run(
            [CODEX, "debug", "prompt-input", "Read-only instruction fixture check."],
            cwd=self.project, env=self.env, capture_output=True, text=True,
            timeout=30,
        )
        if result.returncode and "unrecognized subcommand" in result.stderr:
            self.skipTest("This Codex CLI lacks debug prompt-input")
        self.assertEqual(result.returncode, 0, result.stderr)
        return json.dumps(json.loads(result.stdout), ensure_ascii=False)

    def test_user_file_is_loaded_again_after_preference_update(self):
        user_file = self.home / "AGENTS.md"
        user_file.write_text(
            "# Other user guidance\nNOESIS_UNRELATED_KEEP\n"
            "## Noesis communication preferences\nNOESIS_OLD_PREFERENCE\n",
            encoding="utf-8",
        )
        first = self.render()
        self.assertIn("NOESIS_OLD_PREFERENCE", first)
        user_file.write_text(user_file.read_text().replace(
            "NOESIS_OLD_PREFERENCE", "NOESIS_UPDATED_PREFERENCE"), encoding="utf-8")
        second = self.render()
        self.assertIn("NOESIS_UPDATED_PREFERENCE", second)
        self.assertIn("NOESIS_UNRELATED_KEEP", second)
        self.assertNotIn("NOESIS_OLD_PREFERENCE", second)
        self.assertEqual(list(self.project.iterdir()), [])

    def test_active_override_shadows_base_user_file(self):
        (self.home / "AGENTS.md").write_text("NOESIS_BASE_PREFERENCE", encoding="utf-8")
        (self.home / "AGENTS.override.md").write_text("NOESIS_OVERRIDE_PREFERENCE", encoding="utf-8")
        prompt = self.render()
        self.assertIn("NOESIS_OVERRIDE_PREFERENCE", prompt)
        self.assertNotIn("NOESIS_BASE_PREFERENCE", prompt)

    def test_empty_override_falls_back_to_base_user_file(self):
        (self.home / "AGENTS.md").write_text("NOESIS_BASE_PREFERENCE", encoding="utf-8")
        (self.home / "AGENTS.override.md").write_text("", encoding="utf-8")
        self.assertIn("NOESIS_BASE_PREFERENCE", self.render())
