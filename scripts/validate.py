#!/usr/bin/env python3
"""Dependency-free structural checks for recurring LaTeX layout failures."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

BEGIN = re.compile(r"\\begin\{([^}]+)\}")
END = re.compile(r"\\end\{([^}]+)\}")
PAGE = re.compile(r"\\(?:newpage|clearpage|pagebreak)\b")
SPACE = re.compile(r"\\(?:vspace\*?|vfill|bigskip|medskip|smallskip)\b|\\\\\s*\[[^]]+\]")
SENSITIVE = {
    "minipage",
    "multicols",
    "multicols*",
    "figure",
    "figure*",
    "table",
    "table*",
    "tikzpicture",
    "tcolorbox",
}


def strip_comment(line: str) -> str:
    """Remove an unescaped TeX comment from one line."""
    for index, char in enumerate(line):
        if char != "%":
            continue
        slashes = 0
        cursor = index - 1
        while cursor >= 0 and line[cursor] == "\\":
            slashes += 1
            cursor -= 1
        if slashes % 2 == 0:
            return line[:index]
    return line


def validate_file(path: Path) -> list[tuple[str, int, str, str]]:
    findings: list[tuple[str, int, str, str]] = []
    stack: list[tuple[str, int]] = []

    for number, original in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = strip_comment(original)
        tokens = [(match.start(), "begin", match.group(1)) for match in BEGIN.finditer(line)]
        tokens += [(match.start(), "end", match.group(1)) for match in END.finditer(line)]

        for _, kind, environment in sorted(tokens):
            if environment == "document":
                continue
            if kind == "begin":
                stack.append((environment, number))
            elif not stack:
                findings.append(("error", number, "ENV-END", f"Unexpected end of {environment}."))
            elif stack[-1][0] == environment:
                stack.pop()
            else:
                expected = stack[-1][0]
                findings.append(
                    ("error", number, "ENV-MISMATCH", f"Expected end of {expected}, found {environment}.")
                )

        active = [environment for environment, _ in stack if environment in SENSITIVE]
        if PAGE.search(line) and active:
            findings.append(
                ("error", number, "PAGE-IN-CONTAINER", "Page transition inside: " + ", ".join(active))
            )
        if SPACE.search(line):
            findings.append(
                ("warning", number, "MANUAL-SPACING", "Review manual vertical spacing and document why it is needed.")
            )

    for environment, opened in reversed(stack):
        findings.append(("error", opened, "ENV-UNCLOSED", f"Environment {environment} is not closed."))

    return findings


def tex_files(targets: list[Path]) -> list[Path]:
    files: list[Path] = []
    for target in targets:
        if target.is_file() and target.suffix.lower() == ".tex":
            files.append(target)
        elif target.is_dir():
            files.extend(sorted(target.rglob("*.tex")))
    return files


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("targets", nargs="+", type=Path)
    parser.add_argument("--strict", action="store_true", help="Treat warnings as failures.")
    args = parser.parse_args()

    files = tex_files(args.targets)
    if not files:
        print("No .tex files found.", file=sys.stderr)
        return 2

    all_findings = []
    for path in files:
        for severity, line, code, message in validate_file(path):
            all_findings.append((severity, path, line, code, message))
            print(f"{severity.upper():7} {path}:{line} [{code}] {message}")

    errors = sum(item[0] == "error" for item in all_findings)
    warnings = sum(item[0] == "warning" for item in all_findings)
    print(f"Checked {len(files)} TeX file(s): {errors} error(s), {warnings} warning(s).")
    return 1 if errors or (args.strict and warnings) else 0


if __name__ == "__main__":
    raise SystemExit(main())
