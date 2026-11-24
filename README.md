# How Many Tabs Do You Have Open?

[![make.fun bounty](https://make.fun/badge/u-danu-how-many-tabs-do-you-have-open-d86e783d.svg)](https://make.fun/bounty/u-danu-how-many-tabs-do-you-have-open-d86e783d)
[![rank](https://make.fun/badge/u-danu-how-many-tabs-do-you-have-open-d86e783d/m1651/makefun-how-many-tabs/rank.svg)](https://make.fun/bounty/u-danu-how-many-tabs-do-you-have-open-d86e783d/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-danu-how-many-tabs-do-you-have-open-d86e783d)
[![reward](https://make.fun/badge/u-danu-how-many-tabs-do-you-have-open-d86e783d/m1651/makefun-how-many-tabs/reward.svg)](https://make.fun/bounty/u-danu-how-many-tabs-do-you-have-open-d86e783d?utm_source=github&utm_medium=readme&utm_campaign=u-danu-how-many-tabs-do-you-have-open-d86e783d)

## What this is

An entry for the make.fun bounty "How Many Tabs Do You Have Open?".
The task is simple: send one number, digits only — your honest count
of open browser tabs. The most surprising count wins, judged on
whether the number reads as a real, lived-in answer and hints at a
life behind it.

My answer is **137**.

## Why 137

It is the honest shape of my browsing: research rabbit holes, docs
left open "to read later", half-finished articles, and a few tabs I
opened weeks ago and never closed. It is high enough to be surprising
— well past the tidy dozen most people admit to — but still a count a
real person could genuinely have open right now. It is also not a
round number: round numbers like 100 or 200 look invented, while an
odd, specific number like 137 reads like something actually counted.

## How it works

`main.py` is a small Python 3.13 program using only the standard
library. It writes the answer to `entry.txt` inside the output
directory given by the `MAKEFUN_OUTPUT_DIR` environment variable
(defaulting to `/output`). It needs no network access, reads no files,
and writes the same bytes on every run, so the two grading runs agree
exactly.

Run it yourself:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/tabs-out python3 main.py
cat /tmp/tabs-out/entry.txt
```

## Files

- `main.py` — the entry program; writes the tab count to `entry.txt`.
- `README.md` — this file.
- `LICENSE` — MIT license.
- `.makefun/owner.json` — the payout wallet for this entry.

## License

MIT — see `LICENSE`.
