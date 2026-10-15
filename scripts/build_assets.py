#!/usr/bin/env python3
"""Rebuild the release's demo and social preview with Pillow 11.3.0."""

from pathlib import Path
import shlex
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
BACKGROUND = "#101d30"
FOREGROUND = "#f4f7fb"
ACCENT = "#8ef0ca"


def font(size):
    return ImageFont.load_default(size=size)


def card(size, title, subtitle, lines):
    canvas = Image.new("RGB", size, BACKGROUND)
    draw = ImageDraw.Draw(canvas)
    draw.text((48, 42), "trycopilot.ai", fill=ACCENT, font=font(22))
    draw.text((48, 92), title, fill=FOREGROUND, font=font(42))
    draw.text((48, 158), subtitle, fill=ACCENT, font=font(23))
    y = 226
    for line in lines:
        bounds = draw.textbbox((48, y), line, font=font(22))
        if bounds[2] > size[0] - 35 or bounds[3] > size[1] - 45:
            raise ValueError("Canvas clips the completed session")
        draw.text((48, y), line, fill=FOREGROUND, font=font(22))
        y += 40
    return canvas


def main():
    assets = ROOT / "assets"
    assets.mkdir(exist_ok=True)
    transcript = (ROOT / "evidence/transcripts/selection.txt").read_text().splitlines()
    command = shlex.split(transcript[0][2:])
    lines = ["Task: " + command[-1], "Selected policy:"] + transcript[1:]
    frames = []
    for visible in range(1, len(lines) + 1):
        frames.append(
            card(
                (960, 510),
                "Load the policy for the task",
                "Reconstructed from a real local selection session",
                lines[:visible],
            )
        )
    frames[-1].save(assets / "demo-poster.png", optimize=True)
    frames[0].save(
        assets / "demo.gif",
        save_all=True,
        append_images=frames[1:],
        duration=[900] * (len(frames) - 1) + [3400],
        loop=0,
        disposal=2,
    )
    card(
        (1280, 640),
        "Agent Standards",
        "Task-scoped operating standards for coding agents",
        [
            "Find the situation. Read the relevant policy.",
            "Reviews / Worktrees / Provenance / Credentials",
            "Remote execution / Plans / Task discipline",
            "github.com/trycopilotai/agent-standards",
        ],
    ).save(assets / "social-preview.png", optimize=True)


if __name__ == "__main__":
    main()
