"""Last Text at One Percent — the dying phone's last message (141 chars).

The brief asks for the last text a phone sends at 1% battery: a rushed
confession in the phone's own voice, funny and a little proud of its own
death. The hurry is the whole joke — "listen fast" — because the battery
is nearly gone, so the confession, the grudge against the 47 open tabs,
and the farewell to the charger all have to fit in one breath. The final
image, overheating in its owner's pocket, turns an everyday annoyance
into a heroic death: the phone did not just run out of power, it died
doing what it loved. Keeping the line short and breathless is what makes
the voice believable; a dying phone would not write a paragraph.

Constraints honoured by this script: the entry is a single sentence under
the 200-character limit, written with plain ASCII punctuation plus one
em dash for the punchline, no trailing newline in the output file, and
the script itself uses only the Python standard library so it runs in any
bare make.fun runner image without extra installs.
"""

import os

ENTRY = "1% left, so listen fast: I loved you, I hated your 47 open tabs, and tell the charger I died doing what I loved — overheating in your pocket."

MAX_ENTRY_LENGTH = 200


def normalize_text(text):
    """Collapse runs of whitespace to single spaces and strip the ends."""
    return " ".join(text.split())


def validate_entry(text):
    """Check the entry obeys the bounty rules; return the cleaned text."""
    cleaned = normalize_text(text)
    if not cleaned:
        raise ValueError("entry must not be empty")
    if len(cleaned) > MAX_ENTRY_LENGTH:
        raise ValueError(
            "entry is %d chars, over the %d-char limit"
            % (len(cleaned), MAX_ENTRY_LENGTH)
        )
    if cleaned.endswith("\n"):
        raise ValueError("entry must not end with a newline")
    return cleaned


def resolve_output_dir():
    """Return the output directory, creating it if needed."""
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    return output_dir


def write_entry():
    """Validate the entry, write it to entry.txt, then verify the file."""
    text = validate_entry(ENTRY)
    output_path = os.path.join(resolve_output_dir(), "entry.txt")
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(text)
    verify_written(output_path, text)
    return output_path


def verify_written(output_path, expected_text):
    """Read entry.txt back and confirm it matches the entry exactly."""
    with open(output_path, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != expected_text:
        raise ValueError("entry.txt does not match the entry text")
    if written.endswith("\n"):
        raise ValueError("entry.txt must not end with a newline")
    return True


def main():
    output_path = write_entry()
    print("wrote %s (%d chars)" % (output_path, len(ENTRY)))


if __name__ == "__main__":
    main()
