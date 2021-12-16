#!/usr/bin/env python
# vim:set fileencoding=utf8: #

import sys
from aoc.grid import Grid

class Paper(Grid):
    """Docstring for Paper."""

    def __init__(self):
        Grid.__init__(self)

    def __str__(self):
        string = ''
        for y in range(self.height):
            for x in range(self.width):
                try:
                    string += str(self[x, y])
                except:
                    string += '.'
            string += '\n'

        return string.strip()

    def fold_y(self, pos):
        for y in range(pos+1, self.height):
            for x in range(self.width):
                new_y = pos - y + pos
                if (x,y) in self:
                    self[x, new_y] = self.pop((x,y))

    def fold_x(self, pos):
        for x in range(pos+1, self.width):
            for y in range(self.height):
                new_x = pos - x + pos
                if (x,y) in self:
                    self[new_x, y] = self.pop((x,y))

    def do_fold(self, axis, pos):
        if axis == 'x':
            paper.fold_x(pos)
        else:
            paper.fold_y(pos)

        self._resize()

    def _resize(self):
        self._width = max([k[0] for k in self.keys()]) + 1
        self._height = max([k[1] for k in self.keys()]) + 1


paper = Paper()
fold_y = 0
fold_x = 0
folds = []
for line in sys.stdin.readlines():
    if ',' in line:
        x,y = [int(x) for x in line.split(',')]
        paper[x,y] = '#'
    elif 'fold' in line:
        k,v = line.split()[-1].split('=')
        folds.append((k, int(v)))


paper.do_fold(folds[0][0], folds[0][1])

print('Part 1 Solution: {}'.format(list(paper.values()).count('#')))

for f in folds[1:]:
    paper.do_fold(f[0], f[1])

print('Part 2 Solution:')
print(paper)
