"""
            \ n  /
          nw +--+ ne
            /    \
          -+      +-
            \    /
          sw +--+ se
            / s  \
"""

from __future__ import print_function
import math
import sys

def manhattan_distance(x, y, z=0):
    return math.fabs(x) + math.fabs(y) + math.fabs(z)

def hex_grid_distance(x, y, z):
    return manhattan_distance(x, y, z) / 2

def main():
    data = ''
    for line in sys.stdin:
        data += line

    data = data[:-1]

    max_distance = 0
    x, y = 0, 0
    for move in data.split(','):
        if move == 'n':
            y += -1
        elif move == 's':
            y += 1
        elif move == 'ne':
            x += 1
            y += -1
        elif move == 'se':
            x += 1
        elif move == 'nw':
            x += -1
        elif move == 'sw':
            x += -1
            y += 1
        else:
            print('Error processing %s', move)

        # At the end of each move compute the distance.  Save the furthest
        # distance as time goes on.
        z = -x - y
        if max_distance < hex_grid_distance(x, y, z):
            max_distance = hex_grid_distance(x, y, z)



    z = -x - y
    print('Final position: %d, %d, %d' % (x, y, z))
    print('Distance: %d' % hex_grid_distance(x, y, z))
    print('Max Distance: %d' % max_distance)

if __name__ == '__main__':
    main()