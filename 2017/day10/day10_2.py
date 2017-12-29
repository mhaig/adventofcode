from __future__ import print_function
import sys

# Lengths to add to each input, per the puzzle.
PUZZLE_LENGTHS = [17, 31, 73, 47, 23]

data = ''
for line in sys.stdin:
    data += line

data = data[:-1]

# Convert the incoming lengths into ASCII codes.
lengths = []
for x in data:
    if x == ',':
        lengths.append(44)
    else:
        lengths.append(int(x) + 48)
# Append the standard list.
lengths.extend(PUZZLE_LENGTHS)
print(lengths)


circular_list = range(256)
# circular_list = range(5)

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
        print(temp_list)
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

        print(circular_list)

dense_hash = []
for i in range(len(circular_list) / 16):
    sparse_hash = circular_list[i*16:(i*16) + 16]
    print(sparse_hash)
    dense_hash.append(reduce(lambda x, y: x ^ y, sparse_hash))

# print(circular_list[0] * circular_list[1])
print(len(dense_hash))
print(dense_hash)

string = ''
for x in dense_hash:
    string += '%02x' % x
print(string)
