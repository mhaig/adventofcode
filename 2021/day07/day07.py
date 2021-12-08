#!/usr/bin/env python
# vim:set fileencoding=utf8: #

import sys

crab_positions = [int(x) for x in sys.stdin.read().split(',')]
fuel = {}
for x in range(min(crab_positions),max(crab_positions)+1):
    if x in fuel:
        continue
    fuel[x] = sum([abs(cp - x) for cp in crab_positions])

print('Part 1 Solution: {}'.format(min(fuel.values())))

fuel = {}
for x in range(min(crab_positions),max(crab_positions)+1):
    if x in fuel:
        continue
    fuel[x] = sum([sum(range(1, abs(cp-x)+1)) for cp in crab_positions])

print('Part 2 Solution: {}'.format(min(fuel.values())))
