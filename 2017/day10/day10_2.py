from __future__ import print_function
import sys

# Lengths to add to each input, per the puzzle.
PUZZLE_LENGTHS = [17, 31, 73, 47, 23]

def get_input():
    """Get input from stdin and return as a string."""
    data = ''
    for line in sys.stdin:
        data += line

    data = data[:-1]

    return data

def compute_knot_hash(lengths):
    """Using a list of ASCII codes, compute the Knot Hash."""

    circular_list = range(256)

    current_position = 0
    skip_size = 0

    for j in range(64):
        for length in lengths:

            # Select based on the input.
            temp_list = []
            i = 0
            while i < length:
                temp_list.append(circular_list[(current_position + i) % len(circular_list)])
                i += 1

            # Reverse
            # print(temp_list)
            temp_list.reverse()
            # Update the circular list with the temp list.
            pointer = current_position
            for i in temp_list:
                circular_list[pointer % len(circular_list)] = i
                pointer += 1
            # Update the current position.
            current_position = current_position + length + skip_size
            # Update the skip size
            skip_size += 1

            # print(circular_list)

    dense_hash = []
    for i in range(len(circular_list) / 16):
        sparse_hash = circular_list[i*16:(i*16) + 16]
        # print(sparse_hash)
        dense_hash.append(reduce(lambda x, y: x ^ y, sparse_hash))

    # print(len(dense_hash))
    # print(dense_hash)

    string = ''
    for x in dense_hash:
        string += '%02x' % x

    return string

def str_to_hash_input(string):
    """Take a string and convert it to a list of ASCII codes."""
    hash_input = [ord(x) for x in string]
    hash_input.extend(PUZZLE_LENGTHS)
    return hash_input

def main():
    """Main solution to Day 10."""

    # Get the puzzle input from stdin.
    data = get_input()

    # Convert the incoming lengths into ASCII codes.
    print('Puzzle Input %s' % data)
    # lengths = []
    # for x in data:
    #     if x == ',':
    #         lengths.append(44)
    #     else:
    #         lengths.append(int(x) + 48)
    lengths = str_to_hash_input(data)
    # Append the standard list.
    print('Puzzle Input Converted to List %s' % lengths)
    # lengths.extend(PUZZLE_LENGTHS)
    print('Puzzle Input Prior to Hash %s' % lengths)

    print(compute_knot_hash(lengths))

if __name__ == '__main__':
    main()
