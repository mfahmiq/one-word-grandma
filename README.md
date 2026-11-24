# One Word From Grandma

![make.fun](https://make.fun/badge/u-0xkianno-one-word-from-grandma-f04bed16.svg)
![rank](https://make.fun/badge/u-0xkianno-one-word-from-grandma-f04bed16/mfahmiq/one-word-grandma/rank.svg)
![reward](https://make.fun/badge/u-0xkianno-one-word-from-grandma-f04bed16/mfahmiq/one-word-grandma/reward.svg)

An entry for the [One Word From Grandma](https://make.fun/bounty/u-0xkianno-one-word-from-grandma-f04bed16) bounty on [make.fun](https://make.fun/r/fntpv568): exactly one word, the word grandma would text about AI.

## The word

**WITCHCRAFT**

## Why this word

A grandma faced with a machine that talks back does not reach for jargon.
She reaches for the oldest word she has for a power she cannot explain.
WITCHCRAFT is warm and a little baffled, funny with no caption at all,
tied to the uncanny machine rather than to any subject, and fresher than
the obvious "robot" or "scary". Typed in capitals, exactly the way
grandmas text.

## How it runs

`main.py` is Python 3.13 standard library only, no network, fully
deterministic. It writes the single word to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(default `/output/entry.txt`) and asserts the entry is one word of at most
30 characters.

```sh
python3 -P -s main.py
cat "$MAKEFUN_OUTPUT_DIR/entry.txt"
```

## License

MIT — see [LICENSE](LICENSE).
