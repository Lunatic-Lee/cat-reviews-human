#!/usr/bin/env python3
"""Cat Reviews Its Human — make.fun one-line entry.

Writes a single-line cat review of its human to /output/entry.txt
(1-200 characters, UTF-8), for the make.fun bounty
"Make the AI Judge Laugh: Cat Reviews Its Human".

The review is one deadpan line: three stars, on-time food and a warm
lap, docked for the baby-voice narration and the betrayal act after
the bite. No trailing newline — the file holds exactly the line.
"""

import os

ENTRY = "Three stars: food on time, lap warm, but he narrates my life in a baby voice and then acts betrayed when I bite the hand that feeds me. Literally."

MIN_CHARS = 1
MAX_CHARS = 200


def main() -> None:
    assert MIN_CHARS <= len(ENTRY) <= MAX_CHARS, (
        f"entry is {len(ENTRY)} chars, must be {MIN_CHARS}-{MAX_CHARS}"
    )
    assert ENTRY.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
