#!/usr/bin/env python3

import sys
from collections import Counter
from itertools import groupby


class Hand:
    def __init__(self, hand: str, bid: (int | str)):
        self._hand = []
        for c in hand:
            if c == "T":
                self._hand.append(10)
            elif c == "J":
                self._hand.append(11)
            elif c == "Q":
                self._hand.append(12)
            elif c == "K":
                self._hand.append(13)
            elif c == "A":
                self._hand.append(14)
            else:
                self._hand.append(int(c))

        self._bid = int(bid)

    def score(self) -> int:
        groups = Counter(self._hand)
        if len(groups) == 1:
            # Only one value in list, must be 5 of a kind
            return 7
        if len(groups) == 2:
            # Only two values seen in list, could be 4 of a kind or full house.
            a_count = next(iter(groups.values()))
            if a_count == 4 or a_count == 1:
                return 6
            return 5
        if len(groups) == 3:
            # Only three values seen in list, could be 3 of a kind or two
            # pairs.
            for v in groups.values():
                if v == 3:
                    return 4
            return 3
        if len(groups) == 4:
            return 2

        return 1

    def __lt__(self, other) -> bool:
        if self.score() == other.score():
            for i in range(5):
                if self._hand[i] == other._hand[i]:
                    continue
                return self._hand[i] < other._hand[i]
            return False
        return self.score() < other.score()

    def __repr__(self) -> str:
        return f"Hand(hand={self._hand}, bind={self._bid})"

    @property
    def bid(self) -> int:
        return self._bid


game_input = list(sys.stdin.readlines())

hands = []
for line in game_input:
    hands.append(Hand(line.split()[0], line.split()[1]))

score = 0
for i, h in enumerate(sorted(hands)):
    score += (i + 1) * h.bid

print("Part 1 Solution: {}".format(score))
