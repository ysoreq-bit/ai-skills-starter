from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("validator", ROOT / "scripts" / "validate.py")
assert SPEC and SPEC.loader
validator = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = validator
SPEC.loader.exec_module(validator)
FIXTURES = ROOT / "tests" / "fixtures"


class ValidatorTests(unittest.TestCase):
    def codes(self, filename: str) -> set[str]:
        return {item[2] for item in validator.validate_file(FIXTURES / filename)}

    def test_valid_layout_has_no_findings(self) -> None:
        self.assertEqual(validator.validate_file(FIXTURES / "valid-layout.tex"), [])

    def test_page_break_inside_minipage_is_error(self) -> None:
        self.assertIn("PAGE-IN-CONTAINER", self.codes("page-break-in-minipage.tex"))

    def test_manual_spacing_is_warning(self) -> None:
        self.assertIn("MANUAL-SPACING", self.codes("manual-spacing.tex"))

    def test_unclosed_environment_is_error(self) -> None:
        source = "\\documentclass{article}\n\\begin{document}\n\\begin{minipage}{1cm}\ntext\n\\end{document}\n"
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "broken.tex"
            path.write_text(source, encoding="utf-8")
            codes = {item[2] for item in validator.validate_file(path)}
        self.assertIn("ENV-UNCLOSED", codes)

    def test_escaped_percent_is_not_comment(self) -> None:
        self.assertEqual(validator.strip_comment(r"Value: 50\% and text"), r"Value: 50\% and text")


if __name__ == "__main__":
    unittest.main()
