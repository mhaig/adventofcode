from enum import Enum

class Direction(Enum):
    FORWARD = 0
    DOWN = 1
    UP = 2

class Command(object):

    def __init__(self, string):
        self._string = string

        self._units = int(self._string.split()[1])
        self._direction = self._string.split()[0]
        self._horizontal = 0
        self._depth = 0
        if self._direction == 'up':
            self._direction = Direction.UP
            self._depth = self._units * -1
        elif self._direction == 'down':
            self._direction = Direction.DOWN
            self._depth = self._units
        elif self._direction == 'forward':
            self._direction = Direction.FORWARD
            self._horizontal = self._units

    def direction(self):
        return self._direction

    def units(self):
        return self._units

    def depth(self):
        return self._depth

    def horizontal(self):
        return self._horizontal
