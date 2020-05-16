#!/usr/bin/env python
# vim:set fileencoding=utf8: #

import argparse
import sys

import intcode_computer

class Robot(object):
    """Docstring for Robot."""

    def __init__(self, position=(0,0)):
        """
        @todo Document Robot.__init__ (along with arguments).

        position - @todo Document argument position.
        """
        self._x = 0
        self._y = 0

        self._direction = UP

    @property
    def position(self):
        return (self._x, self._y)

    def move(self):
        # Move the robot
        if self._direction == UP:
            self._y -= 1
        elif self._direction == DOWN:
            self._y += 1
        elif self._direction == LEFT:
            self._x -= 1
        elif self._direction == RIGHT:
            self._x += 1
        else:
            raise NotImplemented('Can only move up, down, left, right!')

    def turn_left(self):
        self._direction += 90
        if self._direction >= 360:
            self._direction -= 360
        if self._direction < 0:
            self._direction += 360


    def turn_right(self):
        self._direction -= 90
        if self._direction >= 360:
            self._direction -= 360
        if self._direction < 0:
            self._direction += 360


UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

parser = argparse.ArgumentParser()
parser.add_argument('--part1', action='store_true')
parser.add_argument('file_name')
args = parser.parse_args()

hull_grid = {(0,0): 0}
robot = Robot()

with open(args.file_name, 'r') as f:
    program = f.read()

computer = intcode_computer.IntcodeComputer(program, True)

if not args.part1:
    computer.set_input(1)
while computer.running:

    if computer.need_input:
        computer.set_input(hull_grid.get(robot.position, 0))
    computer.execute_single()
    paint = computer.output
    if paint is not None:
        # First output is paint
        hull_grid[robot.position] = paint

        # Continue computer until direction
        while computer.running:
            computer.execute_single()
            direction = computer.output
            if direction is not None:
                if direction == 0:
                    robot.turn_left()
                else:
                    robot.turn_right()
                robot.move()
                break

print(f'Part 1 Answer: {len(hull_grid)}')

if args.part1:
    sys.exit()

from PIL import Image
width = max(hull_grid.keys(), key=lambda x: x[0])
height = max(hull_grid.keys(), key=lambda x: x[1])
img = Image.new('1', (width[0]+1, height[1]+1))
pixels = img.load()
for k,v in hull_grid.items():
    pixels[k[0], k[1]] = v

img.show()
