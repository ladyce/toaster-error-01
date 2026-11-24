#!/usr/bin/env python3
"""The Funniest Toaster Error Message — make.fun entry.

Writes one deadpan toaster error message (<=120 chars) to /output/entry.txt.
The line was chosen by a full 8-candidate pairwise round-robin (7-0) plus a
beat-the-top test against the ai-joke-03 top 3, judged in-session on the
competition's own brief: a real error message a kitchen toaster would show,
fresh surprise from where the obvious toaster puns never go, tight, one clear
appliance voice, landing on a single read.

Winning line (78 chars): the toaster reports, in the flat tone of an error
code, that the bread has been trapped inside it since Tuesday — and that
both of them have been changed by the experience.
"""

import os

ENTRY = "E-13: The bread has been in here since Tuesday. It has seen things. So have I."


def main() -> None:
    assert 1 <= len(ENTRY) <= 120, "entry must be 1-120 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    # Byte length matters for the Size tie-break: keep it ASCII-tight.
    assert len(ENTRY.encode("utf-8")) == len(ENTRY), "entry must stay ASCII"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
