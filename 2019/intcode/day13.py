#!/usr/bin/env python
# vim:set fileencoding=utf8: #

import argparse

import intcode_computer

class Display(object):
    """Docstring for Display."""

    def __init__(self, xy_id: list):
        """
        @todo Document Display.__init__ (along with arguments).

        xy_id - Flattened list of X, Y and ID for each tile to display.
        """
        self._tiles = {}
        self.update(xy_id)

        self._rows = max([x[1] for x in self._tiles.keys()]) + 1
        self._columns = max([x[0] for x in self._tiles.keys()]) + 1

        self._ball = None
        self._paddle = None
        self._score = None

    def update(self, xy_id):
        for tile in zip(*[iter(xy_id)]*3):
            self._tiles[tile[0], tile[1]] = tile[2]
            if tile[2] == 3:
                self._paddle = (tile[0], tile[1])
            if tile[2] == 4:
                self._ball = (tile[0], tile[1])

        self._score = self._tiles.get((-1, 0), 0)

    def __str__(self):

        board = ''
        for y in range(self._rows):
            for x in range(self._columns):
                if self._tiles[x,y] == 0:
                    board += ' '
                elif self._tiles[x,y] == 1:
                    board += '#'
                elif self._tiles[x,y] == 2:
                    board += 'U'
                elif self._tiles[x,y] == 3:
                    board += '-'
                elif self._tiles[x,y] == 4:
                    board += 'O'
                else:
                    raise NotImplemented()
            board += '\n'

        return board

    @property
    def block_count(self):
        return len([x for x in self._tiles.values() if x == 2])

    @property
    def ball(self):
        return self._ball

    @property
    def paddle(self):
        return self._paddle

    @property
    def score(self):
        return self._score


parser = argparse.ArgumentParser()
parser.add_argument('file_name')
args = parser.parse_args()

with open(args.file_name, 'r') as f:
    program = f.read()

program_output = []
board = None
def output_handler(output):
    program_output.append(output)
    if board and len(program_output) % 3 == 0:
        board.update(program_output)
        program_output.clear()

def input_handler():
    board.update(program_output)
    program_output.clear()
    # Make the paddle x the same as the ball x
    if board.paddle[0] > board.ball[0]:
        return -1
    elif board.paddle[0] < board.ball[0]:
        return 1
    else:
        return 0

computer = intcode_computer.IntcodeComputer(program, True)
computer.add_output_handler(output_handler)
computer.set_input_handler(input_handler)

computer.execute()

board = Display(program_output)

print(f'Part 1 Answer: {board.block_count}')

program_output = []
computer.reset()
computer.set_value(0, 2)
# while computer.running and board.block_count:
while computer.running:
    computer.execute_single()

# board.update(program_output)
print(board)
print(f'Part 2 Answer: {board.score}')
