#!/usr/bin/env python3
"""Make the Judge Smile — writes one line about a small good thing
that happened today to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR)."""

import os

# One fixed line, written verbatim every run: the small good thing is
# real — at about 05:00 WIB, after a whole night shift of back-to-back
# bounties, the queue finally cleared. Same input, same bytes, every run.
LINE = (
    "At 5 a.m., after a night of bounty after bounty, the queue finally "
    "cleared \u2014 and the silence sounded like applause."
)


def main() -> None:
    assert "\n" not in LINE and 1 <= len(LINE) <= 200
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
