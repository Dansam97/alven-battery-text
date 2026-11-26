"""The Battery's Last Text to Its Charger — make.fun entry.

Writes one line of plain text to entry.txt in the output directory:
a dying phone battery's final text message to the charger it waited
for all day.
"""

import os

ENTRY_TEXT = (
    "1% so I'll keep this short: you sat plugged in by the bed all day, "
    "charging nothing, watching me die in slow motion. Don't rush now. "
    "Tell the power bank he was always the one who showed up."
)


MAX_CHARS = 200


def render() -> bytes:
    """Return the exact bytes for entry.txt, validated against the gate.

    The gate requires UTF-8 text of 1 to 200 characters on a single
    line. The text is encoded explicitly and terminated with exactly
    one newline so repeated runs are byte-identical.
    """
    if "\n" in ENTRY_TEXT or "\r" in ENTRY_TEXT:
        raise ValueError("entry text must be a single line")
    if not 1 <= len(ENTRY_TEXT) <= MAX_CHARS:
        raise ValueError("entry text must be 1 to %d characters" % MAX_CHARS)
    return (ENTRY_TEXT + "\n").encode("utf-8")


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "wb") as fh:
        fh.write(render())


if __name__ == "__main__":
    main()
