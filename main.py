#!/usr/bin/env python3
"""one-line-office-jokes: write one funny line about office life to /output/entry.txt.

The line is a small office joke: a noreply@ address, which by definition
never answers mail, replies to the narrator, apologises, and asks them to
stop emailing it. The contradiction lands in the last few words, where the
address that must never reply tells the sender to stop writing.

Standard library only, no network. Deterministic: the same bytes on every
run, so the two grading runs produce identical entry files.
"""

import os
import sys

# The line is built from two clauses, one per beat of the joke, so each
# beat can be checked on its own: the impossible reply, then the payoff
# that turns "do not reply" into a polite request to stop emailing.
CLAUSES = (
    "The noreply@ address replied to my email, apologised,",
    "and asked me to stop emailing it.",
)

LINE = " ".join(CLAUSES)

MIN_LEN = 1
MAX_LEN = 199


def problems(text: str) -> list:
    """Return every gate violation for the entry text (empty means valid)."""
    found = []
    if not (MIN_LEN <= len(text) <= MAX_LEN):
        found.append(f"entry is {len(text)} code points, must be {MIN_LEN}-{MAX_LEN}")
    stripped = text.strip()
    if not stripped:
        found.append("entry must not be only white space")
    if text != stripped:
        found.append("entry must not start or end with white space")
    if "\n" in text or "\r" in text:
        found.append("entry must be a single line")
    if "  " in text:
        found.append("entry must not contain a double space")
    if not stripped.endswith("."):
        found.append("entry must end as one sentence")
    # One sentence, one line: a second full stop anywhere would mean the
    # joke rambles past its punchline instead of landing on one line.
    if text.count(".") != 1:
        found.append("entry must be a single sentence (one full stop)")
    return found


def main() -> int:
    if len(CLAUSES) != 2:
        print("line must be built from exactly two clauses", file=sys.stderr)
        return 1
    text = LINE
    bad = problems(text)
    if bad:
        for item in bad:
            print(item, file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    # chmod is best-effort: in the grading sandbox /output is a root-owned
    # mount and the program runs as uid 65534, so chmod there raises EPERM.
    # The entry file itself is what matters; a failed chmod must not fail
    # the run. (The output directory itself is never chmodded or removed.)
    try:
        os.chmod(path, 0o644)
    except OSError:
        pass
    # Read the file back as bytes and confirm they match the line exactly.
    with open(path, "rb") as f:
        if f.read() != text.encode("utf-8"):
            print("entry.txt does not match the funny line", file=sys.stderr)
            return 1
    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
