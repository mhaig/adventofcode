#!/usr/bin/env python
# vim:set fileencoding=utf8: #

import sys

def solve_part_2(input_data):

    floor = 0
    for pos, c in enumerate(input_data):
        if c == '(':
            floor += 1
        else:
            floor -= 1

        if floor < 0:
            return pos + 1


def solve_part_1(input_data):

    return input_data.count('(') - input_data.count(')')

if __name__ == '__main__':
    # Read input from stdin
    data = sys.stdin.read()
    print(solve_part_1(data))
    print(solve_part_2(data))
