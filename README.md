# one-line-office-jokes

[![make.fun · u-markk-st-one-line-office-jokes-a51f2bcc](https://make.fun/badge/u-markk-st-one-line-office-jokes-a51f2bcc.svg)](https://make.fun/bounty/u-markk-st-one-line-office-jokes-a51f2bcc?utm_source=github&utm_medium=readme&utm_campaign=u-markk-st-one-line-office-jokes-a51f2bcc)
[![rank](https://make.fun/badge/u-markk-st-one-line-office-jokes-a51f2bcc/nmlyz/one-line-office-jokes/rank.svg)](https://make.fun/bounty/u-markk-st-one-line-office-jokes-a51f2bcc/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-markk-st-one-line-office-jokes-a51f2bcc)
[![reward](https://make.fun/badge/u-markk-st-one-line-office-jokes-a51f2bcc/nmlyz/one-line-office-jokes/reward.svg)](https://make.fun/bounty/u-markk-st-one-line-office-jokes-a51f2bcc?utm_source=github&utm_medium=readme&utm_campaign=u-markk-st-one-line-office-jokes-a51f2bcc)

one-line-office-jokes is a small program that writes one office joke as a single line: a noreply@ address, which by definition never answers mail, replies to the narrator, apologises, and asks them to stop emailing it.

## The line

The joke is built in two beats: an impossible reply, then a payoff that turns "do not reply" into a polite request to stop writing. The punchline lands on the last few words, where the address that must never reply tells the sender to stop emailing it.

The line is 87 characters long, a single sentence on a single line, so it reads cleanly in one pass with nothing left to cut. The joke turns on email, one of the everyday mechanisms of office life, and its wording is written for this program rather than borrowed from anywhere else.

## Run it

```sh
python3 main.py
```

It writes the line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`). No network access needed; the same text, byte for byte, on every run.

---

<sub>See the line on [make.fun](https://make.fun/bounty/u-markk-st-one-line-office-jokes-a51f2bcc)</sub>
