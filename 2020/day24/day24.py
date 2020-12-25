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

def get_blacks():
    return [k for k,v in tiles.items() if v == 'black']

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

print('Part 1 Answer: {}'.format((len(get_blacks()))))

def get_adjacent_colors(q, r):
    adjacent = []
    for i,j in [[1, -1], [1, 0], [0,1], [-1, 1], [-1, 0], [0,-1]]:
        if (q+i, r+j) in tiles:
            adjacent.append(tiles[q+i, r+j])
        else:
            adjacent.append('white')

    return adjacent

def get_adjacent_whites(q, r):
    adjacent = []
    for i,j in [[1, -1], [1, 0], [0,1], [-1, 1], [-1, 0], [0,-1]]:
        if (q+i, r+j) in tiles:
            if tiles[q+i, r+j] == 'white':
                adjacent.append([q+i, r+j])
        else:
            adjacent.append([q+i, r+j])
    return adjacent

def process_day(day):

    new_tiles = dict(tiles)
    # Get location of all the black tiles.
    black_tiles = get_blacks()

    # First process rules for the black tiles.
    for l in black_tiles:
        adjacent_colors = get_adjacent_colors(l[0], l[1])
        num_blacks = len([x for x in adjacent_colors if x == 'black'])
        if num_blacks == 0 or num_blacks > 2:
            new_tiles[tuple(l)] = 'white'

        # Get the white tiles adjacent to this black tile.
        white_tile_locations = get_adjacent_whites(l[0], l[1])
        for w in white_tile_locations:
            # For each white tile, see if it has exactly two black adjacent.
            adjacent_colors = get_adjacent_colors(w[0], w[1])
            if len([x for x in adjacent_colors if x == 'black']) == 2:
                new_tiles[tuple(w)] = 'black'

    return new_tiles

for x in range(100):
    tiles = process_day(x)

print('Part 2 Answer: {}'.format(len(get_blacks())))
