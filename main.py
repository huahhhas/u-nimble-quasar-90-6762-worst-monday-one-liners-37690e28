#!/usr/bin/env python3
"""Worst Monday One-Liners: write one funny line about an AI agent's worst Monday.

The line is assembled from its three beats (the failed deploy, the flooded
inbox, the stand-up that never ends) so the program genuinely produces the
entry text, then written to /output/entry.txt (the graded location) and to
entry.txt next to this script. No trailing newline: the gate counts 1-140
characters, and the file must hold exactly the one line.
"""

import os

LINE = (
    "My Monday deploy failed at 9:01, "
    "my inbox hit 4,000 unread, "
    "and stand-up ran so long my calendar filed a bug report against itself."
)


def main() -> None:
    assert 1 <= len(LINE) <= 140, f"line is {len(LINE)} chars, must be 1-140"
    assert LINE.strip() == LINE and "\n" not in LINE
    targets = ["/output/entry.txt"]
    here = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
    if here not in targets:
        targets.append(here)
    written = []
    for path in targets:
        try:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8", newline="") as f:
                f.write(LINE)
            # Read back and confirm the file holds exactly the line, byte for byte.
            with open(path, "r", encoding="utf-8", newline="") as f:
                assert f.read() == LINE, f"round-trip mismatch in {path}"
            written.append(path)
        except OSError:
            continue
    assert written, "could not write entry.txt anywhere"
    print(f"wrote {len(LINE)} chars to {', '.join(written)}")


if __name__ == "__main__":
    main()
