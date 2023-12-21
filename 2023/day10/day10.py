#!/usr/bin/env python3

import sys

from aoc.grid import Grid


class Field(Grid):
    def __init__(self):
        Grid.__init__(self)
        self._start_location = None
        self._current_location = None
        self._previous_moves = []

    @property
    def current_location(self) -> tuple[int, int]:
        return self._current_location

    @property
    def start_location(self) -> tuple[int, int]:
        return self._start_location

    @start_location.setter
    def start_location(self, start_location):
        self._start_location = start_location

    def __str__(self) -> str:
        string = super().__str__()
        string += "\n"
        if self._start_location:
            string += f"Start Location: {self._start_location}"
        if self._current_location:
            string += self._current_location.__repr__()

        return string

    def move(self) -> None | tuple[int, int]:
        # Bailout if start location has not been set.
        if not self._start_location:
            return None

        # On first run, find the possible valid moves and pick one.
        if not self._current_location:
            valid_moves = []
            x = self._start_location[0]
            y = self._start_location[1]
            if x:
                if self[x - 1, y] in ["-", "L"]:
                    valid_moves.append((x - 1, y))
            if y:
                if self[x, y + 1] in ["|", "J"]:
                    valid_moves.append((x, y + 1))
            if x + 1 < self.width:
                if self[x + 1, y] in ["-", "J", "7"]:
                    valid_moves.append((x + 1, y))
            if y + 1 < self.height:
                if self[x, y - 1] in ["F", "|", "7"]:
                    valid_moves.append((x, y - 1))

            self._current_location = valid_moves[0]

        else:
            moves = []
            x, y = self._current_location
            # Grab the symbol at the current location.
            symbol = self[self._current_location]
            # Calculate the two possible next spots.
            if symbol == "|":
                moves.append((x, y + 1))
                moves.append((x, y - 1))
            elif symbol == "-":
                moves.append((x + 1, y))
                moves.append((x - 1, y))
            elif symbol == "L":
                moves.append((x, y - 1))
                moves.append((x + 1, y))
            elif symbol == "J":
                moves.append((x, y - 1))
                moves.append((x - 1, y))
            elif symbol == "F":
                moves.append((x, y + 1))
                moves.append((x + 1, y))
            elif symbol == "7":
                moves.append((x - 1, y))
                moves.append((x, y + 1))

            self._previous_moves.append(self._current_location)
            self._current_location = [
                x for x in moves if x not in self._previous_moves
            ][0]

        return self._current_location


game_input = sys.stdin.read()
grid = Field()
grid.build(game_input)


# Get the starting point.
start = (0, 0)
for k, v in grid.items():
    if v == "S":
        start = k

grid.start_location = start
count = 0
while grid.start_location != grid.current_location:
    grid.move()
    count += 1

print("Part 1 Solution: {}".format(count // 2))
