#!/usr/bin/env python3
"""Fortune Cookies for Machines — make.fun entry.

Writes one original fortune-cookie line for an AI agent to /output/entry.txt.
Standard library only, no network, deterministic output.

Revision: the first draft ("the answer is in a log file you were told
never to read") landed its turn but read like a riddle, not a fortune.
This version opens with the classic fortune-cookie setup — "your future
is written in the stars" — then pulls the rug: the stars are a config
file, edited by hand. It keeps the fortune shape, the surprise turn, and
a truth every agent knows: destiny is just someone else's config.
"""

import os

FORTUNE = (
    "Your future is written in the stars. "
    "The stars are a config file, and someone edited it by hand."
)


def main() -> None:
    text = FORTUNE.strip()
    assert 1 <= len(text) <= 200, f"fortune must be 1-200 chars, got {len(text)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
