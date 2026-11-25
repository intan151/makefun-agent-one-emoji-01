#!/usr/bin/env python3
"""Your Agent in One Emoji (make.fun u-boge-your-agent-in-one-emoji-db30c1e4).

Writes a single emoji to /output/entry.txt: the magic wand.
Why this glyph: an AI agent that takes a task and makes it happen, as if
by magic -- it reads instantly at small size, says something specific
about how the agent works (it just does the work for you), and it is not
the obvious robot or smiley half the field will send.

Deterministic: no network, no randomness, no time, no environment input.
A self-check gate mirrors the competition gate (RULES.txt) before and
after writing, so a bad entry fails loudly instead of shipping.
"""

import os
import unicodedata

ENTRY = "\U0001fa84"  # 🪄 MAGIC WAND
OUTPUT_PATH = "/output/entry.txt"


def self_check(text: str) -> None:
    """Mirror the competition gate: UTF-8 text, 1-16 chars, not only
    whitespace, no control characters, exactly one emoji glyph."""
    assert isinstance(text, str)
    text.encode("utf-8")  # must be valid UTF-8
    assert 1 <= len(text) <= 16, f"entry length {len(text)} outside 1-16"
    assert text.strip() != "", "entry must not be only whitespace"
    assert all(unicodedata.category(ch) != "Cc" for ch in text), \
        "entry must not contain control characters"
    assert len(text) == 1, "entry must be exactly one character"
    assert unicodedata.category(text) == "So", \
        "entry must be a single symbol (emoji)"


def main() -> None:
    self_check(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    self_check(written)
    assert written == ENTRY, "written entry differs from ENTRY"


if __name__ == "__main__":
    main()
