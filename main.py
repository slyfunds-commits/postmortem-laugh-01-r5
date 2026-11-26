#!/usr/bin/env python3
"""Postmortem Laugh R5 entry: writes the keeper line to /output/entry.txt.

Keeper: "Safe Forever" — the agent encrypts the backups and puts the
decryption key inside the backup, so the backups are safe from everyone,
forever, including us.
Pure stdlib only (grader is python:3.13-slim, no site-packages).
"""

import os

ENTRY = (
    "I asked the agent to encrypt the backups. "
    "It did, and stored the decryption key inside the backup "
    "\u2014 the backups are safe forever."
)


def main() -> None:
    text = ENTRY
    assert 1 <= len(text) <= 400, "entry must be 1-400 characters"
    assert text.count(".") == 2, "entry must be 1-2 sentences"
    assert text == text.strip(), "no leading/trailing whitespace"
    # Reversal test: the last beat redefines the setup word ("safe"):
    # protected becomes unrecoverable — safe from everyone, forever,
    # including the people who own the backups.
    # The gate counts characters, so the file must end exactly at the
    # last word — no trailing newline, no trailing space.
    assert not text.endswith("\n"), "no trailing newline"
    assert not text.endswith(" "), "no trailing space"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
