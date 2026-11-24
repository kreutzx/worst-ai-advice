"""Entry for the make.fun 'Worst AI Advice' competition.

Writes the single entry line, verbatim, to /output/entry.txt.
"""

import os

ENTRY_TEXT = "You should diversify your savings: half in one meme coin, half in the same meme coin after it changes its name."


def main():
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    # Exactly one line: the entry text plus a trailing newline.
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT + "\n")


if __name__ == "__main__":
    main()
