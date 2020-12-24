#!/usr/bin/env python
# vim:set fileencoding=utf8: #

import sys

def find_holders(bag_name, bag_dict):
    holders = []
    for k,v in bag_dict.items():
        if bag_name in v:
            if k not in holders:
                holders.append(k)
                holders.extend(find_holders(k, bag_dict))

    return holders

def count_bags(bag_name, bag_dict):
    # Get the bags inside the named bag.
    inside_bags = bag_dict[bag_name]
    num = 0
    for b in inside_bags.split(', '):
        bag_name = ' '.join(b.split()[1:-1])
        if 'other' in bag_name:
            continue
        else:
            n = int(b.split()[0])
            c = count_bags(bag_name, bag_dict)
            num += n + n*c
    return num

puzzle_input = sys.stdin.read().strip()

bags = {}

for line in puzzle_input.split('\n'):
    bags[line.split('contain')[0].replace('bags','').strip()] = line.split('contain')[1].strip()

holders = []
holders.extend(find_holders('shiny gold', bags))

print('Part 1 Answer: {}'.format(len(set(holders))))

print('Part 2 Answer: {}'.format(count_bags('shiny gold', bags)))
