from __future__ import print_function
import sys

data = ''
for line in sys.stdin:
    data += line

data = data[:-1]


circular_list = range(256)

current_position = 0
skip_size = 0
lengths = [int(x) for x in data.split(',')]

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

print(circular_list[0] * circular_list[1])
