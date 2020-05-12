#!/usr/bin/env python
# vim:set fileencoding=utf8: #

import argparse
from intcode import grid

def calculate_biodiversity(g):

    return int(str(g).replace('\n','')[::-1],2)

parser = argparse.ArgumentParser()
parser.add_argument('file_name')
args = parser.parse_args()

with open(args.file_name, 'r') as f:
    raw = f.read()

g = grid.Grid()
g.build(raw)

print(g)
for k,v in g.items():
    if v == '#':
        g[k[0],k[1]] = 1
    else:
        g[k[0],k[1]] = 0
print(g)

diversity = set()
minute = 1
while True:

    new_grid = grid.Grid()
    # Process the grid.
    for k,v in g.items():
        if v == 0:
            # Empty space, look for one or two adjacent bugs, if there are
            # space becomes a bug.
            if g.get_adjacent(k[0],k[1]).count(1) in [1, 2]:
                new_grid[k[0],k[1]] = 1
            else:
                new_grid[k[0],k[1]] = 0
        else:
            if g.get_adjacent(k[0],k[1]).count(1) == 1:
                new_grid[k[0],k[1]] = 1
            else:
                new_grid[k[0],k[1]] = 0

    bd = calculate_biodiversity(new_grid)
    if bd in diversity:
        print(bd)
        break

    diversity.add(bd)
    g = new_grid
    minute += 1
