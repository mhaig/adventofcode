#!/usr/bin/env python
# vim:set fileencoding=utf8: #

import sys

diagnostic_report = sys.stdin.readlines()
diagnostic_report = [x.strip() for x in diagnostic_report]

columns = [[] for i in diagnostic_report[0]]
print(len(columns))
for r in diagnostic_report:
    for i,b in enumerate(r):
        columns[i].append(b)

negate = 1
gamma_rate = 0
for c in columns:
    if c.count('1') > c.count('0'):
        gamma_rate += 1
    gamma_rate <<= 1
    negate <<= 1
    negate += 1
gamma_rate >>= 1
negate >>= 1

print('gamma rate: {} {}'.format(bin(gamma_rate), gamma_rate))
print('negate: {} {}'.format(bin(negate), negate))
epsilon_rate = negate - gamma_rate
print('epsilon rate: {} {}'.format(bin(epsilon_rate), epsilon_rate))
print('Part 1 Solution: {}'.format(gamma_rate * epsilon_rate))

# Turn into columns, get most of "current" column, pull out numbers that match,
# call again with index and remaining list.
def solve(pos, remaining_list, most_or_least):
    if pos > len(remaining_list[0]) or len(remaining_list) == 1:
        return remaining_list

    column = []
    for r in remaining_list:
        column.append(r[pos])

    match = '0'
    if most_or_least == 'least':
        match = '1'
    if column.count('1') == column.count('0'):
        if most_or_least == 'most':
            match = '1'
        else:
            match = '0'
    elif column.count('1') > column.count('0'):
        if most_or_least == 'most':
            match = '1'
        else:
            match = '0'

    remaining_list = [x for x in remaining_list if x[pos] == match]
    return solve(pos+1, remaining_list, most_or_least)

oxygen_generator_rating = solve(0, diagnostic_report, 'most')[0]
print('Oxygen Generator Rating {} {}'.format(
    int(oxygen_generator_rating, 2), oxygen_generator_rating))
co2_scrubber_rating = solve(0, diagnostic_report, 'least')[0]
print('CO2 Scrubber Rating {} {}'.format(
    int(co2_scrubber_rating, 2), co2_scrubber_rating))
print('Part 2 Solution {}'.format(
    int(oxygen_generator_rating, 2) * int(co2_scrubber_rating,2)))
