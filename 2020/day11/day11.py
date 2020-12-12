#!/usr/bin/env python
# vim:set fileencoding=utf8: #

import sys
from aoc import grid

class SeatLayout(object):
    """Docstring for SeatLayout."""

    def __init__(self, seat_grid):
        """
        @todo Document SeatLayout.__init__ (along with arguments).

        arg - @todo Document argument arg.
        """
        if isinstance(seat_grid, str):
            self._grid = grid.Grid()
            self._grid.build(seat_grid)
        else:
            self._grid = seat_grid


    def round_part1(self):
        g = grid.Grid()
        for k,v in self._grid.items():
            g[k[0],k[1]] = v
            if v == 'L':
                if self._grid.get_adjacent_diagonal(k[0],k[1]).count('#') == 0:
                    g[k[0],k[1]] = '#'
            elif v == '#':
                if self._grid.get_adjacent_diagonal(k[0],k[1]).count('#') >= 4:
                    g[k[0],k[1]] = 'L'

        self._grid = g

    def solve_part1(self):
        # Get a hash of table.
        prev_hash = self._grid.__str__()
        self.round_part1()
        while prev_hash != self._grid.__str__():
            prev_hash = self._grid.__str__()
            self.round_part1()

    def get_occupied_seat_count(self):
        return self._grid.__str__().count('#')

    def __str__(self):
        return self._grid.__str__()

s = SeatLayout(sys.stdin.read())
s.solve_part1()
print('Part 1 Answer: {}'.format(s.get_occupied_seat_count()))
