#!/usr/bin/env python
# vim:set fileencoding=utf8: #

import argparse

def deal_into_new(cards):
    return cards[::-1]

def cut_n_cards(cards, n):
    return cards[n:] + cards[:n]

def deal_with_increment_n(cards, n):
    new_cards = [0] * len(cards)
    new_index = 0
    for x,c in enumerate(cards):
        new_cards[new_index] = c
        new_index = (new_index + n) % len(cards)

    return new_cards

def get_n(instruction):
    return int(instruction.split()[-1])

def process_instructions(cards, instructions):

    for instruction in instructions.split('\n'):
        if not instruction:
            continue

        if instruction == 'deal into new stack':
            cards = deal_into_new(cards)
        elif 'cut' in instruction:
            cards = cut_n_cards(cards, get_n(instruction))
        elif 'deal with increment' in instruction:
            cards = deal_with_increment_n(cards, get_n(instruction))
        else:
            raise NotImplemented('Bad instruction!')

    return cards


parser = argparse.ArgumentParser()
parser.add_argument('file_name')
parser.add_argument('cards', type=int)
parser.add_argument('card', type=int)
args = parser.parse_args()

with open(args.file_name, 'r') as f:
    card_instructions = f.read()

cards = list(range(10))

print('Running Test #1... ', end='')
instructions = """deal with increment 7
deal into new stack
deal into new stack"""
if [0, 3, 6, 9, 2, 5, 8, 1, 4, 7] == process_instructions(cards, instructions):
    print('passed!')
else:
    print('failed!')


print('Running Test #2... ', end='')
instructions= """cut 6
deal with increment 7
deal into new stack"""
if [3, 0, 7, 4, 1, 8, 5, 2, 9, 6] == process_instructions(cards, instructions):
    print('passed!')
else:
    print('failed!')

print('Running Test #3... ', end='')
instructions = """deal with increment 7
deal with increment 9
cut -2"""
if [6, 3, 0, 7, 4, 1, 8, 5, 2, 9] == process_instructions(cards, instructions):
    print('passed!')
else:
    print('failed!')

print('Running Test #4... ', end='')
instructions = """deal into new stack
cut -2
deal with increment 7
cut 8
cut -4
deal with increment 7
cut 3
deal with increment 9
deal with increment 3
cut -1"""
if [9, 2, 5, 8, 1, 4, 7, 0, 3, 6] == process_instructions(cards, instructions):
    print('passed!')
else:
    print('failed!')

cards = list(range(args.cards))
print(f'Running algorithm on {args.cards} cards to find card {args.card}')
print(len(cards))
answer = process_instructions(cards, card_instructions)
print(f'Part 1 Answer: {answer.index(args.card)}')
