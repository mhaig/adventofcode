#!/usr/bin/env python
# vim:set fileencoding=utf8: #

import argparse

import grid
import intcode_computer

parser = argparse.ArgumentParser()
parser.add_argument('file_name')
args = parser.parse_args()

with open(args.file_name, 'r') as f:
    program = f.read()

computer = intcode_computer.IntcodeComputer(program, True)

def print_tractor_beam(tractor_beam):

    # height = max([k[1] for k in tractor_beam.keys()]) + 1
    # width = max([k[0] for k in tractor_beam.keys()]) + 1

    print_str = ''
    for y in range(tractor_beam.height):
        print_str += '%02d' % y
        for x in range(tractor_beam.width):
            if tractor_beam[x, y] == 0:
                print_str += '.'
            else:
                print_str += '#'
        print_str += '\n'

    print(print_str)

cache = {}
def get_tractor_beam_point(x, y):
    if (x,y) not in cache:
        # print('not in cache!')
        computer.reset()
        computer.set_input([x, y])
        computer.execute()
        cache[x,y] = computer.output
    return cache[x,y]

def get_tractor_beam(start_x, start_y, height, width):

    tractor_beam = grid.Grid()
    for x in range(width):
        for y in range(height):

            x += start_x
            y += start_y
            tractor_beam[x, y] = get_tractor_beam_point(x, y)

    return tractor_beam

tractor_beam = get_tractor_beam(0, 0, 50, 50)
print(f'Part 1 Answer: {sum(tractor_beam.values())}')
print_tractor_beam(tractor_beam)

# Part 2.

y = 4
prev_x = 0
done = False
while not done:
    first_x = False
    x = prev_x
    # For this row, find the first X
    while True:
        # print(x,y)
        if get_tractor_beam_point(x, y) == 1:
            if not first_x:
                prev_x = x
                first_x = True
            # See if it's at least 100 points wide.
            if get_tractor_beam_point(x+99, y) == 1:
                # See if it's 100 points deep.
                # print('100 points wide!')
                if get_tractor_beam_point(x, y+99) == 1:
                    # Check the last corner.
                    print('100 points deep!')
                    if get_tractor_beam_point(x+99, y+99) == 1:
                        # Got it!
                        print(f'Part 2 Answer: {x},{y} {(10000*x) + y}')
                        done = True
                        break
                    else:
                        x += 1
                else:
                    x += 1
            else:
                break
        else:
            x += 1

    y += 1
