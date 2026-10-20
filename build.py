#!/usr/bin/env python3
"""Build the static GitHub Pages page from the Markdown and SVG sources."""

from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "measurement-data-inventory.md"
SVG = ROOT / "measurement-retrospective.svg"
TEMPLATE = ROOT / "template.html"
OUTPUT = ROOT / "index.html"
PLACEHOLDER = "<!-- TIMELINE_SVG -->"


def main() -> int:
    for path in (SOURCE, SVG, TEMPLATE):
        if not path.exists():
            print(f"missing input: {path}", file=sys.stderr)
            return 1

    pandoc = subprocess.run(
        [
            "pandoc",
            "-f",
            "markdown",
            "-t",
            "html5",
            "-s",
            "--toc",
            "--toc-depth=2",
            "--template",
            str(TEMPLATE),
            "--metadata",
            "title=What Internet Measurement Data Is For",
        ],
        input=SOURCE.read_text(encoding="utf-8"),
        text=True,
        capture_output=True,
    )
    if pandoc.returncode != 0:
        print(pandoc.stderr, file=sys.stderr)
        return pandoc.returncode

    html = pandoc.stdout
    if PLACEHOLDER not in html:
        print("timeline placeholder missing from template output", file=sys.stderr)
        return 1

    html = html.replace(PLACEHOLDER, SVG.read_text(encoding="utf-8").strip(), 1)
    OUTPUT.write_text(html, encoding="utf-8")
    print(f"wrote {OUTPUT.relative_to(ROOT)} ({len(html):,} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
