"""The 3AM Fridge Text — a smart fridge texts its owner at 3am.

Deterministic: writes the same single line on every run.
Pure Python standard library only.
"""

import os

LINE = "It's 3 a.m. You came for water and left with cake. I saw everything. I'm a fridge, not a priest \u2014 but I keep your secrets cold."


def main():
    assert 1 <= len(LINE) <= 140, "gate is 1-140 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
