#!/usr/bin/env python3
"""The Excuse That Almost Works.

Writes the single line a gamer texts the boss to skip work on GTA 6
launch week to /output/entry.txt. Pure standard library, deterministic:
the same bytes on every run.
"""

import os

# One line, plain words, no setup, no signature. It opens like a real,
# boring IT problem (work laptop froze mid-update, IT is involved) and
# then collapses on its own logic: the thing the laptop is stuck
# downloading is GTA 6 itself, until lunchtime.
EXCUSE = "Sorry boss, my work laptop froze mid-update and IT says it's stuck downloading GTA 6 until lunchtime."


def main():
    # Gate: one line, at most 20 words, 1 to 140 characters, UTF-8.
    assert "\n" not in EXCUSE, "entry must be a single line"
    assert 1 <= len(EXCUSE) <= 140, "entry must be 1-140 characters"
    assert len(EXCUSE.split()) <= 20, "entry must be at most 20 words"
    assert EXCUSE.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
