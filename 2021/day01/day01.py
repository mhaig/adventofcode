#!/usr/bin/env python
# vim:set fileencoding=utf8: #

import sys

depths = list(sys.stdin.readlines())
depths = [int(x) for x in depths]

def part1(depths):
    increases = 0
    for i, d in enumerate(depths):

        if i == 0:
            next

        if d > depths[i-1]:
            increases += 1

    return increases

def part2(depths):
    increases = 0

    for i, d in enumerate(depths):

        if i >= 3:

            if ((depths[i] + depths[i-1] + depths[i-2]) >
                    depths[i-3] + depths[i-2] + depths[i-1]):
                increases += 1

    return increases


print('Part 1 Solution: {}'.format(part1(depths)))
print('Part 2 Solution: {}'.format(part2(depths)))
