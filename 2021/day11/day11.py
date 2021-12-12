#!/usr/bin/env python
# vim:set fileencoding=utf8: #

import sys
from aoc.grid import Grid

def get_over_ten(grid):
    over_ten = []
    for key, value in grid.items():
        if value > 9:
            over_ten.append(key)

    return over_ten

def step(grid):
    for x in range(grid.width):
        for y in range(grid.height):
            grid[x,y] = int(grid[x,y]) + 1

grid = Grid()
grid.build(sys.stdin.read())

print(grid)

total_flashes = 0

def entire_step(grid):

    step(grid)

    flash_list = []

    # Get list of squares that can flash
    for _ in range(25):
        over_ten = get_over_ten(grid)
        for l in over_ten:
            if l in flash_list:
                continue

            # flash(grid, l[0], l[1], [])
            flash_list.append(l)
            x = l[0]
            y = l[1]
            spaces_to_add = [(x-1, y),
                             (x, y-1),
                             (x+1, y),
                             (x, y+1),
                             (x+1, y+1),
                             (x-1, y-1),
                             (x+1, y-1),
                             (x-1, y+1)]
            for s in spaces_to_add:
                if s in grid:
                    grid[s] += 1


    for f in flash_list:
        grid[f] = 0

    return len(flash_list)

total_flashes = 0
for s in range(100):
    total_flashes += entire_step(grid)

print('Part 1 Solution: {}'.format(total_flashes))

s = 100
while sum(grid.values()) != 0:
    entire_step(grid)
    s += 1

print('Part 2 Solution: {}'.format(s))
