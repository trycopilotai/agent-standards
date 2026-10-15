#!/usr/bin/env python3
"""Run the complete repository checks for the managed CI unit."""

from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def main():
    if sys.version_info < (3, 11):
        print("Full CI requires Python 3.11 or later.", file=sys.stderr)
        return 2
    if any(unit != "//:check" for unit in sys.argv[1:]):
        print("Unknown CI unit; expected //:check.", file=sys.stderr)
        return 2
    lint = ROOT / "vendor/lint/lint.py"
    if not lint.is_file():
        print("Initialize vendor/lint before running CI.", file=sys.stderr)
        return 2
    for command in [
        [sys.executable, "-B", "scripts/check.py"],
        [sys.executable, "-B", str(lint), "--cwd", str(ROOT), "--all"],
    ]:
        result = subprocess.run(command, cwd=ROOT)
        if result.returncode:
            return result.returncode
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
