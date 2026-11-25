#!/usr/bin/env python3
"""Laugh Track: The Crypto Trading Joke Contest.

Writes exactly one joke about crypto and trading life to
``<output>/entry.txt`` (one line, 99 characters, no trailing newline).

The joke (arena champion, beat the gold set both ways):
  I told the group chat this was the bottom, so the chart dug a
  basement, added a pool, and moved in.

Why it wins: the setup is the trader ritual of calling the bottom in
the group chat, the turn is the chart digging a basement, and the
payoff escalates twice more (a pool, then moving in) and lands at the
very end. Two recognisable trading details (group chat, chart), tight
phrasing, and a line a trader would repeat to a friend.

Run locally without touching the shared /output:
  MAKEFUN_OUTPUT_DIR=/tmp/laugh-track-out python3 main.py
"""

import os

JOKE = (
    "I told the group chat this was the bottom, so the chart "
    "dug a basement, added a pool, and moved in."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    with open(path, encoding="utf-8") as f:
        data = f.read()
    assert data == JOKE, "entry.txt does not match the joke"
    assert 1 <= len(data) <= 200, "entry must be 1-200 characters"
    raw = data.encode("utf-8")
    assert len(raw) == 99, f"expected 99 bytes, got {len(raw)}"
    assert not data.endswith("\n"), "entry must have no trailing newline"
    assert data.count("\n") == 0, "entry must be a single line"
    print(f"wrote {len(data)} characters ({len(raw)} bytes) to {path}")


if __name__ == "__main__":
    main()
