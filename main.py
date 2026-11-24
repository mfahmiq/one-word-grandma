"""Write one word to /output/entry.txt: the word grandma would text about AI.

The word: WITCHCRAFT.

Why this word: a grandma faced with a machine that talks back does not
reach for jargon. She reaches for the oldest word she has for a power she
cannot explain. WITCHCRAFT is warm and a little baffled, it is funny with
no caption at all, it is tied to the uncanny machine rather than to any
subject, and it is fresher than the obvious "robot" or "scary". Typed in
capitals, exactly the way grandmas text.

Stdlib only, no network, deterministic: the same bytes on every run.
The entry must be a single word of 1-30 characters.
"""

import os

WORD = "WITCHCRAFT"  # one word, 10 characters, all capitals, like grandma texts

assert WORD and not WORD.isspace(), "entry must not be blank"
assert len(WORD) <= 30, "entry must be at most 30 characters"
assert len(WORD.split()) == 1, "entry must be exactly one word"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD + "\n")


if __name__ == "__main__":
    main()
