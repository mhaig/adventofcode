#!/usr/bin/env python
# vim:set fileencoding=utf8: #

import sys
from aoc.grid import Grid

puzzle_input = sys.stdin.readlines()

draw_numbers = [int(x) for x in puzzle_input[0].split(',')]

class Board(Grid):

    def __init__(self):
        Grid.__init__(self)
        self._won = False

    def build(self, string):
        for y, row in enumerate(string.split('\n')):
            if not row:
                continue

            for x, c in enumerate(row.split()):
                if c:
                    self[x,y] = int(c)

    def all(self):
        l = []
        for y in range(self.height):
            for x in range(self.width):
                l.append(self[x,y])
        return l

    def get_won(self):
        return self._won
    def set_won(self, val):
        self._won = val

boards = []
board_str = ''
for row in puzzle_input[2:]:
    print(row)
    if not row == '\n':
        board_str += row
    else:
        print(board_str)
        b = Board()
        b.build(board_str)
        print(b)
        boards.append(b)
        board_str = ''

print(board_str)
b = Board()
b.build(board_str)
print(b)
boards.append(b)

def winner(drawn, test):
    return all([x in drawn for x in test])

def solve():
    for i in range(1,len(draw_numbers)):
        for b in boards:
            if b.get_won():
                continue

            for r in range(b.height):
                if winner(draw_numbers[0:i], b.get_row(r)):
                    uncalled = sum([x for x in b.all() if x not in draw_numbers[0:i]])
                    print('Part 1 Solution: {}'.format(uncalled * draw_numbers[i-1]))
                    b.set_won(True)

            if b.get_won():
                continue

            for c in range(b.width):
                if winner(draw_numbers[0:i], b.get_column(c)):
                    uncalled = sum([x for x in b.all() if x not in draw_numbers[0:i]])
                    print('Part 1 Solution: {}'.format(uncalled * draw_numbers[i-1]))
                    b.set_won(True)

solve()
