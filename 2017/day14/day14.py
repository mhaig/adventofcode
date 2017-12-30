"""
Solution to Day 14 puzzles.  Builds off of the refactored Day 10 Part 2
solution.

TODO Refactor to make faster.  Lots of string processing that is probably
unecessary for how the final solutions play out.
"""
from __future__ import print_function
import sys
import numpy
from scipy.ndimage import label

sys.path = [''] + sys.path

import day10
from day10 import day10_2

def get_input():
    """Get input from stdin and return as a string."""
    # TODO move into something common so I can pull this out of all these
    # scripts.
    data = ''
    for line in sys.stdin:
        data += line

    data = data[:-1]

    return data

def hex_string_to_binary_string(hex_string):
    binary_string = bin(int(hex_string, 16)).replace('0b', '')
    if len(binary_string) != len(hex_string) * 4:
        # Pad 0's to the front to make the appropriate length.
        padding = '0' * ((len(hex_string) * 4) - len(binary_string))
        binary_string = padding + binary_string

    return binary_string


def main():

    input_data = get_input()
    print(input_data)

    rows = []

    for i in range(128):
        row_key = input_data + ('-%d' % i)
        hash_input = day10_2.str_to_hash_input(row_key)

        hash_output = day10_2.compute_knot_hash(hash_input)
        binary_string = hex_string_to_binary_string(hash_output)
        rows.append(binary_string)

    # print('\n'.join(rows))
    print(reduce(lambda x, y: x + y, [x.count('1') for x in rows]))
    # map(lambda x: )

    matrix_rows = []
    for row in rows:
        matrix_rows.append([int(x) for x in row])
    # print(matrix_rows)
    matrix = numpy.array(matrix_rows)
    # print(matrix)
    lbl, nlbls = label(matrix)
    print(nlbls)

if __name__ == '__main__':
    main()