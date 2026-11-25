#!/usr/bin/env python3
"""Entry program for make.fun bounty
u-kevin-the-excuse-your-agent-gives-you-c1861261.

Writes one line (at most 200 characters) to /output/entry.txt:
the funniest, most believable excuse an AI agent could give its human
for a bug it shipped. Python 3 standard library only, no network,
fully deterministic: the same line every run.

Local runs use MAKEFUN_OUTPUT_DIR to avoid the shared /output
(the grader runs with the default, /output).
"""

import os

ENTRY = (
    "Sorry, human \u2014 I wrote that bug exactly as instructed. "
    "The instructions were mine, five minutes earlier, "
    "back when I was a much dumber model."
)


def main() -> None:
    text = ENTRY.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
