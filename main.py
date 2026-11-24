#!/usr/bin/env python3
"""One Word for the Boss — entry program.

Writes exactly one word describing the boss to /output/entry.txt.
The word is the whole entry: no phrase, no caption, no explanation.
"""

import os

# The entry: one word, 14 characters, no spaces, no trailing newline.
# It must stay a single word of 1-30 characters: the gate rejects
# anything longer, anything with a space, or whitespace-only text.
WORD = "PerMyLastEmail"

OUTPUT_PATH = "/output/entry.txt"


def validate(word: str) -> None:
    """Refuse to write anything the gate would reject."""
    if not 1 <= len(word) <= 30:
        raise ValueError(f"entry must be 1-30 characters, got {len(word)}")
    if word != word.strip() or any(ch.isspace() for ch in word):
        raise ValueError("entry must be exactly one word, no spaces")


def main() -> None:
    validate(WORD)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
    # Read back and confirm the file holds exactly the entry word.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != WORD:
        raise RuntimeError(f"wrote {written!r}, expected {WORD!r}")


if __name__ == "__main__":
    main()
