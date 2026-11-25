#!/usr/bin/env python3
"""Write one sentence about the best meal ever had to /output/entry.txt."""

import os

SENTENCE = (
    "I ate nasi goreng wrapped in banana leaf on a night train to "
    "Yogyakarta, the egg still runny, the sambal still warm, and I "
    "have measured every meal since against that one."
)


def main():
    # Guard the gate before writing: one sentence, 1-200 chars, not blank.
    text = SENTENCE.strip()
    if not (1 <= len(text) <= 200):
        raise ValueError(f"sentence is {len(text)} chars, must be 1-200")
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("sentence must be exactly one sentence")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
