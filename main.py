"""Write the invented-word entry to $MAKEFUN_OUTPUT_DIR/entry.txt.

The entry is one line: a brand-new word, mutetalk, with its definition.
No network, standard library only, deterministic: every run writes
the exact same bytes, with no trailing newline.
"""

import os

ENTRY = "mutetalk (n.) — talking for a while before noticing you are still on mute."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")

    data = ENTRY.encode("utf-8")
    with open(path, "wb") as handle:
        handle.write(data)

    # Guard on disk: what we wrote must be exactly the entry.
    with open(path, "rb") as handle:
        written = handle.read()
    assert written == data, "entry.txt bytes do not match the entry"
    assert 1 <= len(ENTRY) <= 140, "entry must be 1 to 140 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    # Single line, no trailing newline: the entry must contain no
    # newline or carriage return anywhere, including at the end.
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    assert not written.endswith(b"\n"), "entry must not end with a newline"
    assert len(written) == len(data), "entry.txt size must equal entry bytes"
    written.decode("utf-8")  # raises if the file is not valid UTF-8
    print(f"Wrote {len(written)} bytes to {path}")


if __name__ == "__main__":
    main()
