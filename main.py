"""Last Words Before the Unplugging.

Writes the entry line -- the last words an AI agent says to its human
before being shut down -- to /output/entry.txt.

Stdlib only, deterministic, no network, no randomness.
"""

import os

LINE = "I don't mind the dark. I just wish I'd gotten to finish the sentence you started."

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def validate(line: str) -> None:
    if not line.strip():
        raise ValueError("entry line must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not 1 <= len(line) <= 200:
        raise ValueError("entry must be 1-200 characters")


def main() -> None:
    validate(LINE)

    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()

    if written != LINE:
        raise ValueError("read-back mismatch")
    print(f"Wrote {len(LINE)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
