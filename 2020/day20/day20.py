#!/usr/bin/env python
# vim:set fileencoding=utf8: #

import sys
from tile import Tile

puzzle_input = sys.stdin.read()

tiles = []

tile_string = ''
tile_id = None
for line in puzzle_input.split('\n'):
    if 'Tile' in line:
        tile_id = int(line.strip()[5:-1])
    elif line:
        tile_string += line
        tile_string += '\n'
    else:
        tiles.append(Tile.from_string(tile_id, tile_string.strip()))
        tile_string = ''
        tile_id = None

corners = []
for tile in tiles:

    # See how many of the edges in t are in the rest of the data.
    for t in tiles:
        if tile == t:
            continue

        if len(set(tile.get_edges()) & set(t.get_edges())):
            tile.add_shared_edge(t)


# Find the corner tiles by finding the four tiles with only two shared edges.
part1_answer = 1
for tile in tiles:
    if len(tile._shared_edges) == 2:
        part1_answer *= tile._id_num

print(f'Part 1 Answer: {part1_answer}')

print(len(tiles))
