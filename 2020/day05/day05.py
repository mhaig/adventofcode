#!/usr/bin/env python
# vim:set fileencoding=utf8: #

import sys

class Ticket(object):
    """Docstring for Ticket."""

    def __init__(self, row, column, seat):
        """
        @todo Document Ticket.__init__ (along with arguments).

        arg - @todo Document argument arg.
        """
        self._row = row
        self._column = column
        self._seat = seat

    def __str__(self):
        return 'row {}, column {}, seat ID {}'.format(self._row, self._column,
                                                      self._seat)

    @staticmethod
    def from_string(string):

        rows = list(range(128))
        columns = list(range(8))
        for c in string:
            if c == 'F':
                rows = rows[:len(rows)//2]
            elif c == 'B':
                rows = rows[len(rows)//2:]
            elif c == 'L':
                columns = columns[:len(columns)//2]
            elif c == 'R':
                columns = columns[len(columns)//2:]

        return Ticket(rows[0], columns[0], rows[0]*8 + columns[0])

    @property
    def seat(self):
        return self._seat

tickets = [Ticket.from_string(t) for t in sys.stdin.readlines()]
print('Part 1 Answer: {}'.format(max([t.seat for t in tickets])))
print('Total seats in airplane: {}, seats we have: {}'.format((128*8), len(tickets)))
sorted_seats = sorted([t.seat for t in tickets])
for i, s in enumerate(sorted_seats):
    if sorted_seats[i+1] - s != 1:
        print('Part 2 Answer: {}'.format(s+1))
        break
