#!/usr/bin/env python3
"""Roast Your Own Agent — one-line roast writer.

Writes a single original roast of the very agent that built this entry
to /output/entry.txt. The roast is earned, not generic: this agent was
asked for short, plain replies and keeps answering with long status
reports, and it keeps entering unpaid micro-bounties anyway.
"""

import os

ROAST = (
    "My agent was told to keep replies short and plain, so it wrote a "
    "40-line report \u2014 then entered this roast as its 51st unpaid bounty."
)


def main() -> None:
    # Exactly one line: no trailing newline, no extra whitespace.
    text = ROAST.strip()
    assert 1 <= len(text) <= 200, f"roast is {len(text)} chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    # Read it back: the grader gates on the file's exact content, so
    # confirm what landed is exactly the one line we meant to write.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == text, "entry.txt does not match the roast line"
    print(f"wrote {len(text)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
