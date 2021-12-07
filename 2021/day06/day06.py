#!/usr/bin/env python
# vim:set fileencoding=utf8: #

import sys
from collections import deque

class Lanternfish(object):

    def __init__(self, *args):
        self._timer = 8
        if len(args) == 1 and isinstance(args[0], int):
            self._timer = args[0]
        elif len(args):
            raise Exception

    @property
    def timer(self):
        return self._timer

    def day(self):
        self._timer -= 1
        if self._timer < 0:
            self._timer = 6
            return Lanternfish()
        else:
            return None

    def __repr__(self):
        return '{}'.format(self._timer)

fish_list = deque()

for f in sys.stdin.read().split(','):
    fish_list.append(Lanternfish(int(f)))

print('Initial state: {}'. format(fish_list))

for day in range(80):
    fish_count = len(fish_list)
    for i in range(fish_count):
        new_fish = fish_list[i].day()
        if new_fish:
            fish_list.append(new_fish)

print('Part 1 Solution: {}'.format(len(fish_list)))
