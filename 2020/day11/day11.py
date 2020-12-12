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

    def get_first_seats_diagonal(self, x, y):
        first_seats = []

        # Go up.
        _x = x
        _y = y
        while _y + 1 < self._grid.height:
            first_seats.append(self._grid[x, _y + 1])
            if first_seats[-1] in ['#', 'L']:
                break
            else:
                _y += 1

        # Go up-right diagonal
        _x = x
        _y = y
        while _x + 1 < self._grid.width and _y + 1 < self._grid.height:
            first_seats.append(self._grid[_x + 1, _y + 1])
            if first_seats[-1] in ['#', 'L']:
                break
            else:
                _x += 1
                _y += 1

        # Go right
        _x = x
        _y = y
        while _x + 1 < self._grid.width:
            first_seats.append(self._grid[_x + 1, _y])
            if first_seats[-1] in ['#', 'L']:
                break
            else:
                _x += 1

        # Go down-right diagonal
        _x = x
        _y = y
        while _x + 1 < self._grid.width and (_y - 1) >= 0:
            first_seats.append(self._grid[_x + 1, _y - 1])
            if first_seats[-1] in ['#', 'L']:
                break
            else:
                _x += 1
                _y -= 1

        # Go down.
        _x = x
        _y = y
        while (_y - 1) >= 0:
            first_seats.append(self._grid[x, _y - 1])
            if first_seats[-1] in ['#', 'L']:
                break
            else:
                _y -= 1

        # Go down-left diagonal
        _x = x
        _y = y
        while (_x - 1) >= 0 and (_y - 1) >= 0:
            first_seats.append(self._grid[_x - 1, _y - 1])
            if first_seats[-1] in ['#', 'L']:
                break
            else:
                _x -= 1
                _y -= 1

        # Go left
        _x = x
        _y = y
        while _x - 1 >= 0:
            first_seats.append(self._grid[_x - 1, _y])
            if first_seats[-1] in ['#', 'L']:
                break
            else:
                _x -= 1

        # Go up-left diagonal
        _x = x
        _y = y
        while (_x - 1) >= 0 and (_y + 1) < self._grid.height:
            first_seats.append(self._grid[_x - 1, _y + 1])
            if first_seats[-1] in ['#', 'L']:
                break
            else:
                _x -= 1
                _y += 1

        return first_seats

    def round_part2(self):
        g = grid.Grid()
        for k,v in self._grid.items():
            g[k[0],k[1]] = v
            if v == 'L':
                if self.get_first_seats_diagonal(k[0],k[1]).count('#') == 0:
                    g[k[0],k[1]] = '#'
            elif v == '#':
                if self.get_first_seats_diagonal(k[0],k[1]).count('#') >= 5:
                    g[k[0],k[1]] = 'L'

        self._grid = g

    def solve_part2(self):
        prev_hash = hash(self._grid)
        self.round_part2()
        while prev_hash != hash(self._grid):
            prev_hash = hash(self._grid)
            self.round_part2()

    def __str__(self):
        return self._grid.__str__()

puzzle_input = sys.stdin.read()
s = SeatLayout(puzzle_input)
s.solve_part1()
print('Part 1 Answer: {}'.format(s.get_occupied_seat_count()))

s = SeatLayout(puzzle_input)
s.solve_part2()
print('Part 2 Answer: {}'.format(s.get_occupied_seat_count()))
