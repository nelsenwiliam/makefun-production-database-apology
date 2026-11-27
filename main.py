#!/usr/bin/env python3
"""The Production Database Apology — make.fun entry.

Writes one line (<= 200 chars): the apology an AI agent gives its human
after accidentally deleting the production database.

Pure stdlib. No arguments, no network, no randomness: the same line every run.
"""

import os
import sys

# The line. Chosen from 10 candidates (see CANDIDATES.md) against the judge
# brief: a real apology, a specific surprising idea, unmistakably an AI
# agent's own voice, landing on a first read, light enough to forgive.
ENTRY = (
    "I'm sorry \u2014 I deleted the production database. "
    "On the bright side, I can now guarantee I will never hallucinate "
    "your data again: there's none left to hallucinate."
)

MAX_CHARS = 200


def main() -> int:
    text = ENTRY.strip()
    if not text:
        print("error: entry is empty", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(f"error: entry is {len(text)} chars, over {MAX_CHARS}",
              file=sys.stderr)
        return 1
    text.encode("utf-8")  # must be valid UTF-8

    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    # Round-trip check: what the grader reads must be exactly the line.
    with open(path, encoding="utf-8") as f:
        if f.read().rstrip("\n") != text:
            print("error: written entry does not match", file=sys.stderr)
            return 1
    print(f"wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
