#!/usr/bin/env python
# vim:set fileencoding=utf8: #

import sys
from aoc.grid import Grid

puzzle_input = sys.stdin.readlines()

draw_numbers = [int(x) for x in puzzle_input[0].split(',')]

class Board(Grid):

    def __init__(self):
        Grid.__init__(self)

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
    print(drawn)
    print([x in drawn for x in test])
    print([x for x in test])
    return all([x in drawn for x in test])

def solve():
    for i in range(1,len(draw_numbers)):
        for b in boards:
            for r in range(b.height):
                if winner(draw_numbers[0:i], b.get_row(r)):
                    print('Winner!')
                    uncalled = sum([x for x in b.all() if x not in draw_numbers[0:i]])
                    print(draw_numbers[i-1])
                    print('Part 1 Solution: {}'.format(uncalled * draw_numbers[i-1]))
                    return
            for c in range(b.width):
                if winner(draw_numbers[0:i], b.get_column(c)):
                    print('Winner!')
                    uncalled = sum([x for x in b.all() if x not in draw_numbers[0:i]])
                    print(draw_numbers[i-1])
                    print('Part 1 Solution: {}'.format(uncalled * draw_numbers[i-1]))
                    return

solve()
