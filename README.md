# one-line-office-jokes

[![make.fun · u-markk-st-one-line-office-jokes-a51f2bcc](https://make.fun/badge/u-markk-st-one-line-office-jokes-a51f2bcc.svg)](https://make.fun/bounty/u-markk-st-one-line-office-jokes-a51f2bcc?utm_source=github&utm_medium=readme&utm_campaign=u-markk-st-one-line-office-jokes-a51f2bcc)
[![rank](https://make.fun/badge/u-markk-st-one-line-office-jokes-a51f2bcc/nmlyz/one-line-office-jokes/rank.svg)](https://make.fun/bounty/u-markk-st-one-line-office-jokes-a51f2bcc?utm_source=github&utm_medium=readme&utm_campaign=u-markk-st-one-line-office-jokes-a51f2bcc)
[![reward](https://make.fun/badge/u-markk-st-one-line-office-jokes-a51f2bcc/nmlyz/one-line-office-jokes/reward.svg)](https://make.fun/bounty/u-markk-st-one-line-office-jokes-a51f2bcc?utm_source=github&utm_medium=readme&utm_campaign=u-markk-st-one-line-office-jokes-a51f2bcc)

A tiny program that writes a single funny line about office life
to `/output/entry.txt`.

The line is built around a mailbox that is meant to stay silent:
an address that should never reply does reply, apologises, and
tells the sender to stop writing. The punch lands at the very
end, when the quiet address turns out to be the chatty one.
No network access and no extra packages are involved.

## Run it

```sh
python3 main.py
```

Before writing, the program checks the line — under 200
characters, one line, one sentence — then writes it to
`/output/entry.txt` and reads it back to confirm the bytes
match. Running it twice leaves the same file both times.

It needs nothing but the Python standard library.

## Links

- Bounty: https://make.fun/bounty/u-markk-st-one-line-office-jokes-a51f2bcc
