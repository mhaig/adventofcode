#!/usr/bin/env python
# vim:set fileencoding=utf8: #

import sys
from aoc.grid import Grid

grid = Grid()
grid.build(sys.stdin.read().strip())

low_points = []
for x in range(grid.width):
    for y in range(grid.height):
        if grid[x,y] < min(grid.get_adjacent(x, y)):
            low_points.append(grid[x,y])

risk_level_sum = sum([int(x)+1 for x in low_points])

print('Part 1 Solution: {}'.format(risk_level_sum))
