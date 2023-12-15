#!/usr/bin/env python3

import sys
from collections import Counter
from enum import Enum


class Score(Enum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7


class Hand:
    def __init__(self, hand: str, bid: (int | str)):
        self._hand: list[int] = []
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
        self._jokers = False

    def score(self) -> int:
        score = Score.HIGH_CARD
        groups = Counter(self._hand)

        if len(groups) == 1:
            # Only one value in list, must be 5 of a kind
            score = Score.FIVE_OF_A_KIND

        elif len(groups) == 2:
            # Only two values seen in list, could be 4 of a kind or full house.
            score = Score.FULL_HOUSE

            a_count = next(iter(groups.values()))
            if a_count == 4 or a_count == 1:
                # Four of a kind
                score = Score.FOUR_OF_A_KIND

            # If there is a joker there is either one to make it 5 of a kind or
            # there are 3 or 2 which still makes it 5 of a kind
            if self._has_joker():
                score = Score.FIVE_OF_A_KIND

        elif len(groups) == 3:
            # Only three values seen in list, could be 3 of a kind or two
            # pairs.
            score = Score.TWO_PAIR

            if 3 in groups.values():
                # Three of a kind.
                score = Score.THREE_OF_A_KIND
                if groups[1] >= 1:
                    # There is a t least one J, promote to 4 of a kind.
                    score = Score.FOUR_OF_A_KIND
            else:
                if groups[1] == 2:
                    score = Score.FOUR_OF_A_KIND
                elif groups[1] == 1:
                    score = Score.FULL_HOUSE

        elif len(groups) == 4:
            score = Score.ONE_PAIR

            if groups[1] >= 1:
                # The pair is J's, promote to three of a kind.
                score = Score.THREE_OF_A_KIND

        elif self._has_joker():
            score = Score.ONE_PAIR

        return score.value

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

    def _has_joker(self) -> bool:
        if 1 in self._hand:
            return True

        return False

    @property
    def bid(self) -> int:
        return self._bid

    @property
    def jokers(self) -> bool:
        return self._jokers

    @jokers.setter
    def jokers(self, value: bool) -> None:
        self._jokers = value

        for i in range(len(self._hand)):
            if self._hand[i] == 11:
                if value:
                    self._hand[i] = 1
                else:
                    self._hand[i] == 11


game_input = list(sys.stdin.readlines())

hands = []
for line in game_input:
    hands.append(Hand(line.split()[0], line.split()[1]))

score = 0
for i, h in enumerate(sorted(hands)):
    score += (i + 1) * h.bid

print("Part 1 Solution: {}".format(score))

# Reset hands for Jokers
for h in hands:
    h.jokers = True

score = 0
for i, h in enumerate(sorted(hands)):
    score += (i + 1) * h.bid

print("Part 2 Solution: {}".format(score))
