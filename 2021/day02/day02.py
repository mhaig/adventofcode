#!/usr/bin/env python
# vim:set fileencoding=utf8: #

import sys

from command import Command
from submarine import Submarine

commands = [Command(x) for x in sys.stdin.readlines()]

sub = Submarine()

for c in commands:
    sub.execute_command(c)

print('Part 1 Solution: {}'.format(sub.horizontal() * sub.depth()))

sub = Submarine(True)
for c in commands:
    sub.execute_command(c)

print('Part 2 Solution: {}'.format(sub.horizontal() * sub.depth()))
