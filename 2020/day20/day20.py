#!/usr/bin/env python
# vim:set fileencoding=utf8: #

import math
import sys
from tile import Tile
from image import Image

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

    if len(tile._shared_edges) == 2:
        corners.append(tile)

# Find the corner tiles by finding the four tiles with only two shared edges.
part1_answer = 1
for tile in corners:
    part1_answer *= tile._id_num

print(f'Part 1 Answer: {part1_answer}')

# Start creating the final image.
image = Image()
# Take the first corner in the list and put it at 0,0 in the image.
image[0,0] = corners[0]

# Now follow the shared edges to fill in the image.
for x in range(1,int(math.sqrt(len(tiles)))):
    # Find the shared edge of the previous item with only 2 shared edges.
    next_tile = next((t for t in image[x-1,0]._shared_edges if len(t._shared_edges) <= 3), None)
    print(next_tile)
    # print(len(list(next_tile)))
    # quit()
    image[x,0] = next_tile

for y in range(1,int(math.sqrt(len(tiles)))):
    next_tile = next((t for t in image[0,y-1]._shared_edges if len(t._shared_edges) <=3 and t not in image.values()), None)
    print(next_tile)
    image[0,y] = next_tile


print(image)
