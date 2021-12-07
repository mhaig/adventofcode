#!/usr/bin/env python
# vim:set fileencoding=utf8: #

import sys
from collections import deque

class Lanternfish(object):

    def __init__(self, timer=8, count=1):
        self._timer = timer
        self._count = count

    @property
    def timer(self):
        return self._timer

    @property
    def count(self):
        return self._count

    def day(self):
        self._timer -= 1
        if self._timer < 0:
            self._timer = 6
            return True
        else:
            return False

    def __repr__(self):
        return '{}'.format(self._timer)

fish_list = deque()

for f in sys.stdin.read().split(','):
    fish_list.append(Lanternfish(timer=int(f)))

print('Initial state: {}'. format(fish_list))

for day in range(80):
    new_fish = 0
    for fish in fish_list:
        if fish.day():
            new_fish += fish.count
    fish_list.append(Lanternfish(count=new_fish))

print('Part 1 Solution: {}'.format(sum([x.count for x in fish_list])))

for day in range(80, 256):
    new_fish = 0
    for fish in fish_list:
        if fish.day():
            new_fish += fish.count
    fish_list.append(Lanternfish(count=new_fish))

print('Part 2 Solution: {}'.format(sum([x.count for x in fish_list])))
