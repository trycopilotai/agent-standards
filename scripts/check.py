#!/usr/bin/env python3
"""Validate the packaged standards, local links, selector, and assets."""

import hashlib
import json
from pathlib import Path
import re
import struct
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.dont_write_bytecode = True
from select_standards import select


def check(condition, message):
    if not condition:
        raise AssertionError(message)


def main():
    index = json.loads((ROOT / "standards/index.json").read_text())
    check(index["version"] == 1, "Unknown index schema")
    seen = set()
    declared = set()
    for item in index["standards"]:
        ident = item["id"]
        check(re.fullmatch(r"[a-z]+(?:-[a-z]+)*", ident), "Invalid identifier")
        check(ident not in seen, "Duplicate identifier")
        seen.add(ident)
        check(item["path"] == ident + ".md", "Identifier/path mismatch")
        check(item["status"] == "active", "Unexpected status")
        check(
            item["triggers"]
            and all(isinstance(t, str) and t.strip() for t in item["triggers"]),
            "Empty trigger",
        )
        check(item["applies_when"] and item["description"], "Missing applicability")
        target = ROOT / "standards" / item["path"]
        check(target.is_file() and not target.is_symlink(), "Standard missing")
        check(
            target.read_text().startswith("# " + item["title"] + "\n"), "Title mismatch"
        )
        declared.add(target.name)
    actual = {p.name for p in (ROOT / "standards").glob("*.md")}
    check(declared == actual, "Index does not exactly cover the standards")
    for doc in ROOT.rglob("*.md"):
        if ".git" in doc.parts or "vendor" in doc.relative_to(ROOT).parts:
            continue
        for link in re.findall(r"\]\(([^)]+)\)", doc.read_text()):
            if "://" in link or link.startswith("#"):
                continue
            target = (doc.parent / link.split("#")[0]).resolve()
            check(target.is_relative_to(ROOT), "Link escapes the package")
            check(target.is_file(), "Broken local link: " + link)
    cases = [
        ("Resolve a review thread", {"code-review"}),
        ("RESOLVE A REVIEW THREAD", {"code-review"}),
        ("Retire a worktree", {"worktree-lifecycle"}),
        ("Diagnose SSH to a remote machine", {"cross-machine-ssh"}),
        ("Check GitHub auth after a 403", {"github-auth"}),
        ("Keep working autonomously", {"turn-discipline"}),
        ("Update a submodule gitlink", {"submodules"}),
        ("A task without a declared policy trigger", set()),
        ("", set()),
    ]
    for prompt, expected in cases:
        actual_ids = {m["id"] for m in select(prompt, index)}
        check(actual_ids == expected, "Wrong selection: " + repr(prompt))
    command = [
        sys.executable,
        "-B",
        "scripts/select_standards.py",
        "--json",
        "retire a worktree",
    ]
    result = subprocess.run(command, cwd=ROOT, capture_output=True, check=True)
    check(
        json.loads(result.stdout)[0]["id"] == "worktree-lifecycle", "CLI JSON contract"
    )
    check((ROOT / "VERSION").read_text().strip() == "1.0.0", "Release version drift")
    for name, dimensions in [
        ("social-preview.png", (1280, 640)),
        ("demo-poster.png", (960, 510)),
    ]:
        raw = (ROOT / "assets" / name).read_bytes()
        check(raw[:8] == b"\x89PNG\r\n\x1a\n", "Invalid PNG")
        check(struct.unpack(">II", raw[16:24]) == dimensions, "Wrong asset dimensions")
    gif = (ROOT / "assets/demo.gif").read_bytes()
    check(gif[:6] == b"GIF89a", "Invalid GIF")
    check(struct.unpack("<HH", gif[6:10]) == (960, 510), "Wrong GIF dimensions")
    check(b"NETSCAPE2.0\x03\x01\x00\x00\x00" in gif, "Demo must loop")
    manifest = json.loads((ROOT / "evidence/selection-manifest.json").read_text())
    script_hash = hashlib.sha256(
        (ROOT / "scripts/select_standards.py").read_bytes()
    ).hexdigest()
    output_hash = hashlib.sha256(
        (ROOT / "evidence/transcripts/selection.txt").read_bytes()
    ).hexdigest()
    check(manifest["script_sha256"] == script_hash, "Script evidence drift")
    check(manifest["output_sha256"] == output_hash, "Transcript evidence drift")
    table = json.loads((ROOT / "ci-paths.json").read_text())
    check(table["version"] == 1, "CI table version")
    check(table["sweep_patterns"] == ["//:check"], "CI full-run contract")
    check(table["no_impact"] == ["**"], "CI graphless classification")
    check(
        table["test_edges"] == [{"match": "**", "tests": ["//:check"]}],
        "Every changed path must select the check unit",
    )
    print(
        "PASS: index coverage, local links, 9 selector cases, CLI JSON, version, evidence hashes, and asset headers/loop"
    )

    import unittest

    suite = unittest.defaultTestLoader.discover(
        str(ROOT / "tests"), pattern="test_readme_badges.py"
    )
    check(
        unittest.TextTestRunner().run(suite).wasSuccessful(),
        "README badge test failed",
    )


if __name__ == "__main__":
    main()
