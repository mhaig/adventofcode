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

    @property
    def height(self):
        return self._height

    @property
    def width(self):
        return self._width

    def get_row(self, y):
        return [x for k,x in self.items() if k[1] == y]
