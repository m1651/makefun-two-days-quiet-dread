#!/usr/bin/env python3
"""Write one code-review line approving a PR with quiet existential dread."""
import os

LINE = "Approved. It works, the tests pass, and I've already made peace with the future engineer who has to explain this."


def main():
    # Validate the gate before writing: one non-blank line, 1-140 chars.
    if not LINE or not LINE.strip():
        raise SystemExit("error: entry line must not be empty")
    if "\n" in LINE or "\r" in LINE:
        raise SystemExit("error: entry line must be a single line")
    if len(LINE) > 140:
        raise SystemExit(f"error: entry line is {len(LINE)} chars, over the 140-char limit")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
