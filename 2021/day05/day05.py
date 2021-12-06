#!/usr/bin/env python
# vim:set fileencoding=utf8: #

import math
import sys


from aoc.grid import Grid


class Diagram(Grid):

    def __init__(self):
        Grid.__init__(self)

    def __setitem__(self, key, val):
        if key in self:
            super(Diagram, self).__setitem__(key, self[key] + val)
        else:
            super(Diagram, self).__setitem__(key, val)

    def __str__(self):
        string = ''
        for y in range(self.height):
            for x in range(self.width):
                if (x, y) in self:
                    string += str(self[x, y])
                else:
                    string += '.'
            string += '\n'

        return string


class Point(object):
    def __init__(self, x, y):
        self._x = int(x)
        self._y = int(y)

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def __repr__(self):
        return '{},{}'.format(self._x, self._y)


class Line(object):
    def __init__(self, start, end):
        self._start = start
        self._end = end

        x = self._end.x - self._start.x
        y = self._end.y - self._start.y
        if x:
            x = x // abs(x)
        if y:
            y = y // abs(y)
        self._slope = (x, y)

    @property
    def start(self):
        return self._start

    @property
    def end(self):
        return self._end

    @property
    def slope(self):
        return self._slope

    def __repr__(self):
        return '{} -> {} {}'.format(self._start, self._end, self._slope)


lines = []
diagram = Diagram()
for line in sys.stdin.readlines():
    start = line.split('->')[0].strip()
    end = line.split('->')[1].strip()

    lines.append(Line(Point(start.split(',')[0], start.split(',')[1]),
                      Point(end.split(',')[0], end.split(',')[1])))

    if lines[-1].slope[0] == 0 or lines[-1].slope[1] == 0:
        x = lines[-1].start.x
        y = lines[-1].start.y
        while x != lines[-1].end.x or y != lines[-1].end.y:
            diagram[x,y] = 1
            x += lines[-1].slope[0]
            y += lines[-1].slope[1]
        diagram[x,y] = 1
print('Part 1 Solution: {}'.format(sum([1 for x in diagram.values() if x > 1])))

diagram = Diagram()
for line in lines:
    x = line.start.x
    y = line.start.y
    while x != line.end.x or y != line.end.y:
        diagram[x,y] = 1
        x += line.slope[0]
        y += line.slope[1]
    diagram[x,y] = 1

print('Part 2 Solution: {}'.format(sum([1 for x in diagram.values() if x > 1])))
