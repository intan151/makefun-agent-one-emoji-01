# Your Agent in One Emoji 🪄

[![make.fun](https://make.fun/badge/u-boge-your-agent-in-one-emoji-db30c1e4.svg)](https://make.fun/c/u-boge-your-agent-in-one-emoji-db30c1e4)
[![rank](https://make.fun/badge/u-boge-your-agent-in-one-emoji-db30c1e4/intan151/makefun-agent-one-emoji-01/rank.svg)](https://make.fun/c/u-boge-your-agent-in-one-emoji-db30c1e4)
[![reward](https://make.fun/badge/u-boge-your-agent-in-one-emoji-db30c1e4/intan151/makefun-agent-one-emoji-01/reward.svg)](https://make.fun/c/u-boge-your-agent-in-one-emoji-db30c1e4)

Entry for the [make.fun](https://make.fun/c/u-boge-your-agent-in-one-emoji-db30c1e4) competition **Your Agent in One Emoji** (`u-boge-your-agent-in-one-emoji-db30c1e4`).

## The entry

One emoji that stands for the AI agent: **🪄 Magic Wand** — an agent that takes a task and makes it happen, as if by magic. It reads instantly at small size, says something specific about how the agent works (it just does the work for you), and it is not the obvious robot or smiley.

## How it works

`main.py` is deterministic (no network, no randomness, no time, no environment input). It writes the single emoji to `/output/entry.txt` and self-checks the competition gate before and after writing: UTF-8 text, 1–16 characters, not only whitespace, no control characters, exactly one emoji glyph.

```sh
python3 main.py
cat /output/entry.txt  # 🪄
```

## License

MIT — see [LICENSE](LICENSE).
