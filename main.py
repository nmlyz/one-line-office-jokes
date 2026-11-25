#!/usr/bin/env python3
"""Write one short office joke to /output/entry.txt.

The joke turns on a mailbox that promises silence. An address
built never to answer does answer, says sorry, and then asks the
sender to stop writing to it. The whole gag sits in that final
reversal: the one address that must stay quiet is the one
talking back.

Only the standard library is used, and the output never changes,
so repeated runs produce identical bytes.
"""

import os
import sys

LINE = "The noreply@ address replied to my email, apologised, and asked me to stop emailing it."

OUTPUT_PATH = "/output/entry.txt"

MAX_CHARS = 199


def check_line(line):
    """Refuse anything that is not one short sentence on one line."""
    if not line:
        raise ValueError("the line is empty")
    if len(line) > MAX_CHARS:
        raise ValueError("the line must stay under 200 characters")
    if "\n" in line or "\r" in line:
        raise ValueError("the line must fit on a single line")
    if line != line.strip():
        raise ValueError("the line must not start or end with blank space")
    if line.count(".") != 1 or not line.endswith("."):
        raise ValueError("the line must be exactly one sentence")


def main():
    check_line(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != LINE:
        raise ValueError("what was read back does not match the line")
    os.chmod(OUTPUT_PATH, 0o644)
    return 0


if __name__ == "__main__":
    sys.exit(main())
