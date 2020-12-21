#!/usr/bin/env python
# vim:set fileencoding=utf8: #

class Grid(dict):
    """Docstring for Grid."""

    def __init__(self, *args):
        dict.__init__(self, args)
        self._height = 0
        self._width = 0

    def __setitem__(self, key, val):
        dict.__setitem__(self, key, val)
        if key[0] >= self._width:
            self._width = key[0] + 1
        if key[1] >= self._height:
            self._height = key[1] + 1

    def __str__(self):
        string = ''
        for y in range(self.height):
            for x in range(self.width):
                string += str(self[x, y])
            string += '\n'

        return string

    def __hash__(self):
        return hash(self.__str__())

    @property
    def height(self):
        return self._height

    @property
    def width(self):
        return self._width

    def get_row(self, y):
        return [x for k,x in self.items() if k[1] == y]

    def get_column(self, x):
        return [v for k,v in self.items() if k[0] == x]

    def build(self, string):
        for y, row in enumerate(string.split('\n')):
            if not row:
                continue

            for x, c in enumerate(row):
                if c:
                    self[x,y] = c

    def get_adjacent(self, x, y):

        adjacent = []
        if x:
            adjacent.append(self[x-1, y])
        if y:
            adjacent.append(self[x,y-1])
        if x + 1 < self.width:
            adjacent.append(self[x+1, y])
        if y + 1 < self.height:
            adjacent.append(self[x, y+1])

        return adjacent

    def get_adjacent_diagonal(self, x, y):
        adjacent = self.get_adjacent(x, y)

        if x+1 < self.width and y+1 < self.height:
            adjacent.append(self[x+1, y+1])
        if x and y:
            adjacent.append(self[x-1,y-1])
        if x+1 < self.width and y:
            adjacent.append(self[x+1, y-1])
        if x and y+1 < self.height:
            adjacent.append(self[x-1, y+1])

        return adjacent
