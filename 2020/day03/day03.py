#!/usr/bin/env python
# vim:set fileencoding=utf8: #

import sys
from functools import reduce

class Map(object):
    """Docstring for Map."""

    def __init__(self, map_lines):
        """
        @todo Document Map.__init__ (along with arguments).

        map_string - @todo Document argument map_string.
        """
        self._map_lines = map_lines
        self._map = ''.join(map_lines).replace('\n', '')
        self._max_x = len(self._map_lines[0]) - 1
        self._max_y = len(self._map_lines)

    def get_index(self, x, y):
        """Calculate index into map based on a desired x,y coordinate."""
        # First wrap x if necessary.
        new_x = x
        while new_x >= self._max_x:
            new_x -= self._max_x

        if y*self._max_x + new_x > len(self._map):
            print('overflow at {}, {} ({}, {}) = {}, max = {}'.format(x, y, new_x, y, y*self._max_x + new_x, len(self._map)))
        return y*self._max_x + new_x

    def __str__(self):
        string = '{}x{}\n'.format(self._max_x, self._max_y)
        for y in range(self._max_y):
            for x in range(self._max_x):
                string += self._map[self.get_index(x, y)]
            string += '\n'

        return string

    def get_square(self, x, y):
        return self._map[self.get_index(x, y)]

    def get_trees(self, right, down):
        """Given the slope right, down, count trees on slope."""
        trees = 0
        x = right
        y = down
        while y <= self._max_y-1:
            if self.get_square(x, y) == '#':
                trees += 1

            x += right
            y += down

        return trees


input_map = Map(sys.stdin.readlines())

print('Part 1 Solution: {}'.format(input_map.get_trees(3, 1)))

ans = reduce(lambda x, y: x * y,
             [input_map.get_trees(slope[0], slope[1]) for slope in [[1, 1],
                                                                    [3, 1],
                                                                    [5, 1],
                                                                    [7, 1],
                                                                    [1, 2]]])
print('Part 2 Solution: {}'.format(ans))
