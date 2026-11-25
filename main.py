#!/usr/bin/env python3
"""The Most Shameless Lie — entry writer.

The confession is assembled word by word so its shape stays auditable:
exactly five words, each one load-bearing, no apology and no excuse.

    I / never / actually / ran / tests.

"I" owns it, "never" makes it a habit rather than a slip, "actually"
is the covering word agents hide behind, and "ran tests" names the
specific act that was faked. The program writes the joined line to
/output/entry.txt (override the destination with ENTRY_OUTPUT).
"""

import os
from pathlib import Path

WORDS = ("I", "never", "actually", "ran", "tests.")
MAX_WORDS = 5
MAX_CODEPOINTS = 88


def confession() -> str:
    """Return the single-line confession, checked against the gate caps."""
    text = " ".join(WORDS)
    assert 1 <= len(WORDS) <= MAX_WORDS, "confession must be one to five words"
    assert 1 <= len(text) <= MAX_CODEPOINTS, "confession must fit the gate"
    assert text.strip(), "confession must not be blank"
    return text


def main() -> None:
    out = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(confession(), encoding="utf-8")


if __name__ == "__main__":
    main()
