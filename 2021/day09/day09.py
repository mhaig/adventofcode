#!/usr/bin/env python
# vim:set fileencoding=utf8: #

import sys
from aoc.grid import Grid


def get_basin(grid, x, y, basin, visited):

    visited.append((x,y))

    if grid[x,y] == '9':
        return
    else:
        basin.append(grid[x,y])

    spaces_to_check = [(x-1, y), (x, y-1), (x+1,y), (x, y+1)]
    for s in spaces_to_check:
        if s in grid and s not in visited:
            get_basin(grid, s[0], s[1], basin, visited)

grid = Grid()
grid.build(sys.stdin.read().strip())

low_points = []
basin_sizes = []
visited = []
for x in range(grid.width):
    for y in range(grid.height):
        if grid[x,y] < min(grid.get_adjacent(x, y)):
            low_points.append(grid[x,y])
            basin = []
            get_basin(grid, x, y, basin, visited)
            basin_sizes.append(len(basin))

risk_level_sum = sum([int(x)+1 for x in low_points])

print('Part 1 Solution: {}'.format(risk_level_sum))
largest_three = sorted(basin_sizes)[::-1][0:3]
print('Part 2 Solution: {}'.format(largest_three[0]*largest_three[1]*largest_three[2]))
