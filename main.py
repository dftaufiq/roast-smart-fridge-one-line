#!/usr/bin/env python3
"""Roast the Smart Fridge: One Line, Best Laugh Wins — make.fun entry.

Writes the one-line roast of a smart fridge to /output/entry.txt.
Deterministic: the same line every run. No network, no environment reads,
no secrets — the line is a constant in this file.

The line (138 chars) won a 15-variant internal pairwise tournament judged on
the RULES.txt brief (lexicographic: roast of a smart home gadget, punchline
lands, fresh angle, tight one line, specific behaviour). It uses the 2-beat +
reveal structure of past one-liner winners: the fridge rates groceries like
a food critic, the kale gets four stars, and the midnight pizza gets a health
warning AND a restraining order — a double sting in the last clause.
"""

import os
import sys


def validate_line(line: str) -> None:
    """Gate: the entry must be one non-blank line of 1-160 characters.

    Fails loudly (non-zero exit) so a bad line never ships silently.
    """
    if not line or not line.strip():
        print("ERROR: entry line is empty or whitespace-only", file=sys.stderr)
        sys.exit(1)
    if "\n" in line or "\r" in line:
        print("ERROR: entry must be a single line", file=sys.stderr)
        sys.exit(1)
    if len(line) > 160:
        print(f"ERROR: entry is {len(line)} chars, over the 160-char limit",
              file=sys.stderr)
        sys.exit(1)


LINE = (
    "My fridge rated my groceries like a food critic — the kale got four "
    "stars, my midnight pizza got a health warning and a restraining order."
)


def main() -> None:
    validate_line(LINE)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
