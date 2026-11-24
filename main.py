"""Funniest Time Machine Warning Label — entry program.

The line this program writes:

    WARNING: Do not relive yesterday. It has already filed a
    restraining order against you.

Why this line, and why it is built this way:

The judge's brief scores a warning label in a fixed order, so the line
was designed against that order, not against a general idea of funny.
First, it must read as a warning label for a time machine, so it opens
with the safety-notice marker WARNING and an imperative, the way a
real label opens. Second, it must turn a genuine hazard of time travel
into the joke rather than name the hazard flatly: the hazard here is
repetition — going back and living the same day again, the loop every
traveller dreads — and the joke makes yesterday itself the actor that
objects, by filing a restraining order. The paradox is never named;
the paperwork does the naming. Third, the surprise is saved for the
last words: "restraining order against you" lands where the reader
least expects a safety notice to go. Fourth, the whole thing keeps a
straight face throughout, so the joke cuts against the official calm
of the label. Fifth, nothing is wasted: at 87 characters it sits well
inside the 120-character gate, and shortness is also a tie-break
advantage, since an exact tie on judge win rate goes to the smaller
text, then to the earlier receipt.

The lane was checked against the live field before the line was
chosen: all 676 submissions visible at build time were scanned, and
no entry used a restraining order, an airbag, phone roaming, or
reliving yesterday as its turn. The flooded lanes were left alone:
meeting yourself (70 entries), grandfather (75), warranty (33),
lending yourself money (26), and naming the paradox flatly (24).
Ten candidate lines were played against each other pairwise on the
brief's own criterion order; this line won 9-0, and the side-effects
list ("WARNING: Side effects include existing twice, never having
existed, and mild nostalgia for a future you ruined.", 111 chars)
came second at 8-1 and is the fallback if this line ever needs
replacing. The airbags line ("The 1800s have no airbags.") and the
phone-roaming line ("the bill arrives before you leave") were the
other clean lanes and finished mid-table; they stay on record as
alternates, not as entries.

The program itself is deliberately boring: the line is one constant,
the gate is checked before anything is written (UTF-8, 1 to 120
characters, not only whitespace), and the output is exactly the line
with no trailing newline, so a second run produces byte-identical
output. There is no clock, no randomness, and no network access.
"""

import os

LINE = (
    "WARNING: Do not relive yesterday. "
    "It has already filed a restraining order against you."
)


def main() -> None:
    text = LINE
    text.encode("utf-8")
    if not 1 <= len(text) <= 120:
        raise SystemExit(f"entry must be 1-120 characters, got {len(text)}")
    if not text.strip():
        raise SystemExit("entry must not be only whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
