#!/usr/bin/env python
# vim:set fileencoding=utf8: #

import argparse

import intcode_computer

parser = argparse.ArgumentParser()
parser.add_argument('file_name')
args = parser.parse_args()

with open(args.file_name, 'r') as f:
    program = f.read()

program_output = []
def output_handler(output):
    program_output.append(chr(output))

computer = intcode_computer.IntcodeComputer(program, True)
computer.add_output_handler(output_handler)

computer.execute()

pretty = ''
scaffold = {}
x = 0
y = 0
for char in program_output:
    if char == '\n':
        x = 0
        y += 1
    else:
        scaffold[x, y] = char
        x += 1

height = max([y[1] for y in scaffold.keys()]) + 1
width = max([x[0] for x in scaffold.keys()]) + 1

for x in range(width):
    for y in range(height):
        pretty += scaffold[x, y]

    pretty += '\n'

print(pretty)

# Find intersections.
intersection = 0
for x in range(width):
    for y in range(height):
        if x == 0 or x == width - 1:
            continue
        elif y == 0 or y == height - 1:
            continue
        elif scaffold[x, y] == '#':
            # See if all four sides are # as well
            if (scaffold[x - 1, y] == '#' and
                scaffold[x + 1, y] == '#' and
                scaffold[x, y - 1] == '#' and
                scaffold[x, y + 1] == '#'):
                intersection += (x * y)

print(f'Part 1 Answer: {intersection}')
