#!/usr/bin/env python
# vim:set fileencoding=utf8: #

"""
         +
    nw /   \ ne
      + q r +
     w|     |e
      +     +
    sw \   / se
         +

e, se, sw, w, nw, and ne

ne: +q, -r
 e: +q
se: +r
sw: -q, +r
 w: -q
nw: -r
"""

import sys

puzzle_input = sys.stdin.read().strip()

tiles = {}
for line in puzzle_input.split('\n'):
    coordinates = [0, 0]
    # Follow the coordinates to find the tile that gets flipped.
    i = 0
    while i < len(line):
        # First see if the next letter needs to be grabbed as well.
        c = line[i]
        i += 1
        if c in ['n', 's']:
            c += line[i]
            i += 1

        if c == 'ne':
            coordinates[0] += 1
            coordinates[1] -= 1
        elif c == 'e':
            coordinates[0] += 1
        elif c == 'se':
            coordinates[1] += 1
        elif c == 'sw':
            coordinates[0] -= 1
            coordinates[1] += 1
        elif c == 'w':
            coordinates[0] -= 1
        elif c == 'nw':
            coordinates[1] -= 1

    # At the destination tile.  See if it's in the tile dictionary already.
    key = tuple(coordinates)
    if key not in tiles:
        tiles[key] = 'black'
    else:
        if tiles[key] == 'black':
            tiles[key] = 'white'
        else:
            tile[key] = 'black'

print('Part 1 Answer: {}'.format((len([x for x in tiles.values() if x == 'black']))))
