#!/usr/bin/env python
# vim:set fileencoding=utf8: #

import sys
import re

puzzle_input = sys.stdin.read().strip()

memory = {}
and_mask = ''
or_mask = ''

for line in puzzle_input.split('\n'):
    if 'mask' in line:
        mask = line.split(' = ')[1]
        mask = '0b' + mask
        and_mask = int(mask.replace('X', '1'),2)
        or_mask = int(mask.replace('X', '0'),2)
    else:
        # Memory line
        parsed = re.split(r'mem\[(\d+)\] = (\d+)', line)
        memory[int(parsed[1])] = (int(parsed[2]) & and_mask) | or_mask

print('Part 1 Answer: {}'.format(sum(memory.values())))

def convert_to_address(mask, addresses):

    if 'X' in mask:
        # Find the first X, replace with a 0, and then call again...
        convert_to_address(mask.replace('X', '0', 1), addresses)
        convert_to_address(mask.replace('X', '1', 1), addresses)
    else:
        addresses.append(int(mask,2))

memory = {}
for line in puzzle_input.split('\n'):
    if 'mask' in line:
        mask = line.split(' = ')[1]
        mask = '0b' + mask
    else:
        # Memory line
        parsed = re.split(r'mem\[(\d+)\] = (\d+)', line)

        address = '{:036b}'.format(int(parsed[1]))
        address_mask = list('0b' + address)
        # Apply mask
        for i, b in enumerate(mask):
            if b == '1':
                address_mask[i] = '1'
            elif b == 'X':
                address_mask[i] = 'X'

        address_mask = ''.join(address_mask)
        addresses = []
        convert_to_address(address_mask, addresses)
        for a in addresses:
            memory[a] = int(parsed[2])

print('Part 2 Answer: {}'.format(sum(memory.values())))
