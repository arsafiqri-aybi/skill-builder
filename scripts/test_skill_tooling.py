#!/usr/bin/env python3
"""Regression tests for Skill Builder's integrated authoring tools."""

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

from build_metadata import write_metadata
from init_skill import init_skill, parse_resources


class SkillToolingTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="skill-builder-tooling-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def test_initializer_creates_minimal_skill(self):
        target = init_skill(
            "Meeting Notes",
            self.root,
            "Create reusable meeting-note workflows when users need structured notes.",
            [],
        )
        self.assertEqual(target.name, "meeting-notes")
        self.assertTrue((target / "SKILL.md").is_file())
        self.assertTrue((target / "agents" / "openai.yaml").is_file())
        self.assertFalse((target / "references").exists())

    def test_initializer_creates_only_requested_resources(self):
        target = init_skill(
            "report-helper",
            self.root,
            "Build report workflows when users need repeatable structured reporting.",
            ["references", "scripts"],
        )
        self.assertTrue((target / "references").is_dir())
        self.assertTrue((target / "scripts").is_dir())
        self.assertFalse((target / "assets").exists())

    def test_initializer_refuses_existing_directory(self):
        target = self.root / "existing"
        target.mkdir()
        with self.assertRaises(FileExistsError):
            init_skill(
                "existing",
                self.root,
                "Build an existing workflow when users request it.",
                [],
            )

    def test_resource_parser_rejects_unknown_resource(self):
        with self.assertRaises(ValueError):
            parse_resources("references,unknown")

    def test_metadata_uses_runtime_identifier(self):
        target = self.root / "sample"
        target.mkdir()
        (target / "SKILL.md").write_text(
            "---\nname: sample\ndescription: Handle sample tasks when requested.\n---\n# Sample\n",
            encoding="utf-8",
        )
        output = write_metadata(target)
        data = yaml.safe_load(output.read_text(encoding="utf-8"))
        self.assertIn("$sample", data["interface"]["default_prompt"])
        self.assertGreaterEqual(len(data["interface"]["short_description"]), 25)

    def test_metadata_rejects_prompt_without_identifier(self):
        target = self.root / "sample"
        target.mkdir()
        (target / "SKILL.md").write_text(
            "---\nname: sample\ndescription: Handle sample tasks when requested.\n---\n# Sample\n",
            encoding="utf-8",
        )
        with self.assertRaises(ValueError):
            write_metadata(target, default_prompt="Handle this task.")

    def test_validate_cli_success_and_failure(self):
        target = init_skill(
            "portable-skill",
            self.root,
            "Create a portable workflow when users request this specific task.",
            [],
        )
        tool = Path(__file__).with_name("validate_skill.py")
        ok = subprocess.run(
            [sys.executable, str(tool), str(target), "--portable"],
            capture_output=True,
            text=True,
        )
        self.assertEqual(ok.returncode, 0, ok.stdout + ok.stderr)

        (target / "SKILL.md").write_text("broken", encoding="utf-8")
        bad = subprocess.run(
            [sys.executable, str(tool), str(target), "--portable"],
            capture_output=True,
            text=True,
        )
        self.assertEqual(bad.returncode, 1)


if __name__ == "__main__":
    unittest.main()
