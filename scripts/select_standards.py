#!/usr/bin/env python3
"""Select portable standards by case-insensitive literal triggers."""

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def select(prompt, index):
    text = prompt.casefold()
    matches = []
    for standard in index["standards"]:
        if any(trigger.casefold() in text for trigger in standard["triggers"]):
            matches.append(
                {
                    "id": standard["id"],
                    "path": "standards/" + standard["path"],
                    "title": standard["title"],
                }
            )
    return matches


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="Print a JSON array.")
    parser.add_argument("prompt", help="Task text to match against declared triggers.")
    args = parser.parse_args()
    index = json.loads((ROOT / "standards/index.json").read_text())
    matches = select(args.prompt, index)
    if args.json:
        print(json.dumps(matches, indent=2))
    elif matches:
        for item in matches:
            print(item["path"] + " - " + item["title"])
    else:
        print("No trigger matched. Read standards/index.json for applicable policy.")


if __name__ == "__main__":
    main()
