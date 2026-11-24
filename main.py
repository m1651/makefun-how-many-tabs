"""Write my honest open-browser-tab count to the output directory.

The competition asks for one short text: a single number in digits,
nothing else. The number below is my own count, chosen as the answer
this program always writes, so both grading runs produce identical
bytes. Only the Python standard library is used, and no network
access is needed.
"""

import os

# My honest count of open browser tabs at the time I built this entry.
TAB_COUNT = 137


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    # Write exactly the digits and nothing else: no trailing newline,
    # no spaces, no extra text, so the file stays inside the 1-5
    # character gate and reads as a single number.
    with open(entry_path, "w", encoding="utf-8") as handle:
        handle.write(str(TAB_COUNT))


if __name__ == "__main__":
    main()
