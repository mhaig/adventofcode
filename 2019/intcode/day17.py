#!/usr/bin/env python
# vim:set fileencoding=utf8: #

import argparse

import intcode_computer
import cell

class Cell(cell.Cell):

    def __init__(self, content):
        super(Cell, self).__init__()

        self._content = content

    def __eq__(self, other):
        if isinstance(other, str):
            return self._content == other
        else:
            return False

parser = argparse.ArgumentParser()
parser.add_argument('file_name')
parser.add_argument('--print', action="store_true")
args = parser.parse_args()

with open(args.file_name, 'r') as f:
    program = f.read()

verbose = []
program_output = []
def output_handler(output):
    program_output.append(chr(output))
    verbose.append(chr(output))

computer = intcode_computer.IntcodeComputer(program, True)
computer.add_output_handler(output_handler)

computer.execute()

scaffold = {}
x = 0
y = 0
for char in program_output:
    if char == '\n':
        x = 0
        y += 1
    else:
        scaffold[x, y] = Cell(char)
        x += 1

height = max([y[1] for y in scaffold.keys()]) + 1
width = max([x[0] for x in scaffold.keys()]) + 1

def print_scaffold():
    pretty = ''
    for y in range(height):
        for x in range(width):
            if scaffold[x, y].visited:
                pretty += 'X'
            else:
                pretty += str(scaffold[x, y])

        pretty += '\n'

    print(pretty)

if args.print:
    print_scaffold()
    print(''.join(verbose))

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

for k,v in scaffold.items():
    if v == '^':
        start = k

print(f'Start position: {start}')
print(f'{width}, {height}')

robot_path = []
def search(x, y):
    if all([x.visited for x in scaffold.values()]):
        # All scaffold has been visited.
        return True
    elif scaffold[x, y] == '.':
        # Non-scaffold
        return False
    elif scaffold[x, y].visited:
        # Visited
        return False

    robot_path.append((x,y))
    scaffold[x,y].visited = True

    if ((x < width-1 and search(x+1, y))
            or (y > 0 and search(x, y-1))
            or (x > 0 and search(x-1, y))
            or (y < height-1 and search(x, y+1))):
        return True

    return False

search(start[0], start[1])
print_scaffold()
print(len(robot_path))
print(len(set(robot_path)))

# Validate, there shouldn't be any jumps more than 1 in either direction.
for i, path in enumerate(robot_path[1:]):
    if (abs(path[0] - robot_path[i][0]) > 1 or
            abs(path[1] - robot_path[i][1]) > 1 or
            (path[0] - robot_path[i][0] == 0 and
            path[1] - robot_path[i][1] == 0)):
        print(f'Error at {path} {robot_path[i]}')

# Turn the x,y robot path into directions, starting with a L
directions = ['L', 0]
for i, path in enumerate(robot_path):
    if path[0] == robot_path[i-1][0]:
        # X is the same, no turn, just increment.
        directions[-1] += 1
    elif path[0] > robot_path[i-1][0]:
        # X has increased, 
        pass
