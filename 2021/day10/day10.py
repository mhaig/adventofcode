#!/usr/bin/env python
# vim:set fileencoding=utf8: #

import sys
import statistics

BALANCE = {'(': ')', '[': ']', '{': '}', '<': '>'}
OPEN = BALANCE.keys()
CLOSE = BALANCE.values()
CORRUPT_SCORE = {')': 3, ']': 57, '}': 1197, '>': 25137}
INCOMPLETE_SCORE = {')': 1, ']': 2, '}': 3, '>': 4}

def check_balance(parentheses, bad, complete):
    if not parentheses or parentheses[0] in CLOSE:
        return parentheses

    if parentheses[0] in OPEN:
        closer = check_balance(parentheses[1:], bad, complete)
        if closer and closer[0] == BALANCE[parentheses[0]]:
            return check_balance(closer[1:], bad, complete)
        elif closer and closer[0] in CLOSE:
            bad.append(closer[0])
        else:
            # Incomplete, line, start completing.
            complete.append(BALANCE[parentheses[0]])
        return parentheses

    return check_balance(parentheses[1:], bad, complete)

corrupt_score = 0
incomplete_score = []
for line in sys.stdin.readlines():
    bad = []
    complete = []
    check_balance(line, bad, complete)
    if bad:
        # Corrupted line!
        corrupt_score += CORRUPT_SCORE[bad[0]]
    elif complete:
        score = 0
        for c in complete:
            score *= 5
            score += INCOMPLETE_SCORE[c]
        incomplete_score.append(score)

print('Part 1 Solution: {}'.format(corrupt_score))
print('Part 2 Solution: {}'.format(statistics.median(incomplete_score)))
