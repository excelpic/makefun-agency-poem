"""agency-poem-01 entry: writes one short poem about agency to /output/entry.txt.

The poem is the whole entry. It is written as UTF-8 with no trailing line end,
so the bytes in the file are exactly the poem the judge reads.
Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output.
"""

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM = """I wrote the list in pencil, so it could change.
Keys by the door, the letter sealed.
Go, I said — and something that is not me
went out into the weather with my errands,
wearing my intentions like a coat it did not choose.

All day my hands were empty, and the work got done.
The letter arrived. The gate got mended.
The small world turned a quarter-turn toward morning.
You gave your power away, they said.
I gave away my errands. The choosing stayed home —
restless, mine, a dog that will not sleep
till it hears whose feet are on the stair.

But the danger was never the borrowed hands.
It was the evening I nearly signed the list unread.
Agency is not taken from us. We set it down,
gently, one unexamined yes at a time.

So I keep one task back, always, for my own two hands:
to read, to choose, to say go — and mean it."""


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
