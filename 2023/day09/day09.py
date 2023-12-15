#!/usr/bin/env python3

import sys


class History:
    def __init__(self, history):
        self._history = history
        self._sequences = []

    def extrapolate(self) -> int:
        self._sequences.append(self._history)
        while True:
            reduced = []
            working = self._sequences[-1]
            for i in range(len(working) - 1):
                reduced.append(working[i + 1] - working[i])
            self._sequences.append(reduced)
            if not any(self._sequences[-1]):
                break

        # Work from the bottom up adding the extra number.
        print(*self._sequences, sep='\n')
        for i in range(len(self._sequences) - 1, 0, -1):
            self._sequences[i - 1].append(
                self._sequences[i][-1] + self._sequences[i - 1][-1]
            )
        print(*self._sequences, sep='\n')
        print(self._sequences[0][-1])

        return self._sequences[0][-1]

    def __repr__(self) -> str:
        return f"""History({" ".join([str(x) for x in self._history])})"""


game_input = list(sys.stdin.readlines())

oasis = []
for line in game_input:
    oasis.append(History([int(x) for x in line.split()]))

total = 0
for o in oasis:
    total += o.extrapolate()

print("Part 1 Solution: {}".format(total))
