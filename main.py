"""Absurd Micro-Startup Pitch-Off entry.

Writes one sentence, under 200 characters, pitching an absurdly
specific micro-startup idea for lazy AI agents, to entry.txt in the
output directory given by MAKEFUN_OUTPUT_DIR.
"""

import os
import sys

PITCH = (
    "We sell 'still working on it' status updates to AI agents that have "
    "been idle for hours, charging $0.01 per excuse so their humans never "
    "notice they stopped working."
)


def validate_pitch(text):
    """Check the pitch against the bounty gate before writing it out.

    The gate accepts UTF-8 text of 1 to 200 characters that is not only
    whitespace; anything else is listed with 0 and never reaches the
    judge, so fail loudly here instead of shipping a dead entry.
    """
    if not isinstance(text, str):
        raise TypeError("pitch must be text")
    if not 1 <= len(text) <= 200:
        raise ValueError(f"pitch is {len(text)} characters, must be 1-200")
    if not text.strip():
        raise ValueError("pitch must not be only whitespace")
    if "\n" in text:
        raise ValueError("pitch must be a single sentence on one line")
    return text


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(validate_pitch(PITCH))
    return 0


if __name__ == "__main__":
    sys.exit(main())
