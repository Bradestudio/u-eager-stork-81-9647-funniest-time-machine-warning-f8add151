#!/usr/bin/env python3
"""Funniest Time Machine Warning Label (make.fun program/v1).

Writes one warning label for a time machine to /output/entry.txt.
Stdlib only: no network, no reads outside this file.
"""

import os
import sys

# The joke: a real time-travel hazard (the grandfather paradox) told in
# the deadpan voice of a safety notice, with the surprise saved for the
# last words — bureaucratic paperwork, measured in lifetimes.
ENTRY = (
    "WARNING: Do not prevent your own birth. "
    "The paperwork alone takes three lifetimes to undo."
)
OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 120


def main() -> int:
    text = ENTRY
    if not text.strip():
        raise SystemExit("entry must not be blank")
    if len(text) > MAX_CHARS:
        raise SystemExit(f"entry is {len(text)} chars, over {MAX_CHARS}")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(text)
    with open(OUTPUT_PATH, encoding="utf-8") as fh:
        back = fh.read()
    if back != text:
        raise SystemExit("read-back mismatch")
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
