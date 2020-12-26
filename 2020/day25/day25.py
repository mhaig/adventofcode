#!/usr/bin/env python
# vim:set fileencoding=utf8: #

import sys

def transform(subject_number, loop_size):
    value = 1
    for x in range(loop_size):
        value *= subject_number
        value = value % 20201227
    return value

def determine_loop_size(public_key):
    subject_number = 7
    value = 1
    loop_size = 0
    while value != public_key:
        loop_size += 1
        value *= subject_number
        value = value % 20201227

    return loop_size

def get_encryption_key(public_key, loop_size):
    return transform(public_key, loop_size)

puzzle_input = sys.stdin.read().strip('\n')

door_public_key = int(puzzle_input.split('\n')[0])
card_public_key = int(puzzle_input.split('\n')[1])

print(f'Door public key: {door_public_key}')
print(f'Card public key: {card_public_key}')

print('Determining loop size of the door...', end='')
door_loop_size = determine_loop_size(door_public_key)
print(f' done: {door_loop_size}')
print('Determining loop size of the card...', end='')
card_loop_size = determine_loop_size(card_public_key)
print(f' done: {card_loop_size}')

encryption_key = get_encryption_key(card_public_key, door_loop_size)

print('Part 1 Answer: {}'.format(encryption_key))
