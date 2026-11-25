#!/usr/bin/env python3
"""The meeting that should have been one line.

Writes the single sentence that could have replaced an entire
pointless meeting to /output/entry.txt (stdlib only).
"""

import os
from pathlib import Path

LINE = (
    "Nothing has changed since the email, nothing will be decided in this "
    "room, and the only action item is this sentence, which just "
    "cancelled the meeting."
)


def main() -> None:
    # The gate requires 1-200 characters of UTF-8 text; fail loudly
    # instead of writing an invalid entry.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars"
    assert LINE.strip() == LINE and "\n" not in LINE
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
