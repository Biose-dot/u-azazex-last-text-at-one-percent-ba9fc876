"""Last Text at One Percent — the dying phone's last message (141 chars, under 200).

In the phone's own voice, in a hurry: a rushed confession, one last grudge
against the 47 open tabs, and a death it is almost proud of — overheating
in its owner's pocket.
"""

import os

ENTRY = "1% left, so listen fast: I loved you, I hated your 47 open tabs, and tell the charger I died doing what I loved — overheating in your pocket."


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
