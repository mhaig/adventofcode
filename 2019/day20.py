#!/usr/bin/env python
# vim:set fileencoding=utf8: #

import argparse
from intcode import cell
from intcode import grid

class Cell(cell.Cell):
    """Docstring for Cell."""

    def __init__(self, content):
        """
        @todo Document Cell.__init__ (along with arguments).
        """
        super(Cell, self).__init__()

        self._portal = None
        self._content = content

    @property
    def portal(self):
        return self._portal

    @portal.setter
    def portal(self, value):
        self._portal = value

# Read in the entire map.
parser = argparse.ArgumentParser()
parser.add_argument('file_name')
args = parser.parse_args()

with open(args.file_name, 'r') as f:
    raw_map = f.read()

grid = grid.Grid()

for y, row in enumerate(raw_map.split('\n')):
    if not row:
        continue

    print(y, row)

    for x, c in enumerate(row):
        if c:
            grid[x,y] = Cell(c)

def print_grid(a_grid):

    print_str = ''
    for y in range(a_grid.height):
        for x in range(a_grid.width):
            print_str += str(a_grid[x, y])

        print_str += '\n'

    print(print_str)

print_grid(grid)

# Check each item in grid to see if it should have a portal.
for k,v in grid.items():
    x,y = k
    if v.content == '.':
        # Check and see if a letter is around the open space.
        if grid[x,y-1].content not in ['#', '.']:
            grid[x,y].portal = grid[x,y-2].content + grid[x,y-1].content
            print(f'portal above {grid[x,y].portal}')
        elif grid[x,y+1].content not in ['#', '.']:
            grid[x,y].portal = grid[x,y+1].content + grid[x,y+2].content
            print(f'portal below {grid[x,y].portal}')
        elif grid[x-1,y].content not in ['#', '.']:
            grid[x,y].portal = grid[x-2,y].content + grid[x-1,y].content
            print(f'portal left {grid[x,y].portal}')
        elif grid[x+1,y].content not in ['#', '.']:
            grid[x,y].portal = grid[x+1,y].content + grid[x+2,y].content
            print(f'portal right {grid[x,y].portal}')

# TODO convert this to a BFS that hits every node, see webpage that is open.
# Consider making the map a binary tree instead of a map.
def search(x, y, prev=None):

    global steps

    if grid[x,y].portal == 'AA':
        print('back at start...')

    steps += 1
    if grid[x,y].portal == 'ZZ':
        print(f'Found it! {steps}')
        return True
    elif grid[x,y].content == '#':
        steps -= 1
        return False
    elif grid[x,y].content != '.':
        steps -= 1
        return False
    elif grid[x,y].visited:
        # Need to move back here I think...
        steps -= 1
        return False

    print(f'step {steps} {x},{y}')
    grid[x,y].visited = True

    # See if there is a portal and search it if necessary.
    if grid[x,y].portal:
        for k, v in grid.items():
            if v.portal == grid[x,y].portal and v != grid[x,y]:
                print('visit a portal')
                portal_x = k[0]
                portal_y = k[1]

    if ((x < grid.width-1 and search(x+1, y, (x,y))) or 
            (y > 0 and search(x, y-1, (x,y))) or
            (x > 0 and search(x-1, y, (x,y))) or
            (y < grid.height-1 and search(x, y+1, (x,y))) or
            (grid[x,y].portal and search(portal_x, portal_y, (x,y)))):
        return True

    steps -= 1

    return False

# Get the start position.
for k,v in grid.items():
    if v.portal == 'AA':
        start_x = k[0]
        start_y = k[1]

steps = 0
search(start_x, start_y)
print(steps)
