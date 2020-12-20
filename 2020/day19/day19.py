#!/usr/bin/env python
# vim:set fileencoding=utf8: #

import re
import sys

puzzle_input = sys.stdin.read().strip()

rules = {}
messages = []
# Turn the rules into a dictionary.
for line in puzzle_input.split('\n'):
    if ':' in line:
        num, rule = line.split(':')
        rules[num] = rule.strip()
    elif line:
        messages.append(line)

print(rules)
print(messages)

expanded = []
def build_rule(rule):

    string = ''
    if '|' in rules[rule]:
        string += '('
    for r in rules[rule].split():
        if '"' in r:
            string += r.strip('"')
        elif r == '|':
            # pass
            # break
            string += '|'
        else:
            string += build_rule(r)

    if '|' in rules[rule]:
        string += ')'
    return string

rule0 = build_rule('0')

matches = 0
for m in messages:
    result = re.match(rule0, m)
    if result:
        if result.span()[0] == 0 and result.span()[1] == len(m):
            matches += 1

print(f'Part 1 Answer: {matches}')

# Part 2.

# print('Rule 8: {}'.format(build_rule('8')))
# print('Rule 11: {}'.format(build_rule('11')))
# print('Rule 31: {}'.format(build_rule('31')))
# print('Rule 42: {}'.format(build_rule('42')))

rule8 = build_rule('8')
rule42 = build_rule('42')
print('rule8: {}'.format(rule8))
print('rule42: {}'.format(rule42))

print('Does rule8 == rule42?: {}'.format(rule8 == rule42))

# First replace the rules per the puzzle:
#   8: 42 | 42 8
#  11: 42 31 | 42 11 31

# print(rules['8'])
# rules['8'] = '42 | 42 8'
# print(rules['8'])
# print(rules['11'])
# rules['11'] = '42 31 | 42 11 31'
# print(rules['11'])

rule0 = build_rule('0')

# So for rule 8, find rule 42, add an |, 42 again, and a
#   8: 42 | 42 8  => (42 | 42 ( 42 | 42 ( 42 | 42 )))

# print(rule0.find(rule42))
# print(rule0.find(rule8))
print(rule0)

matches = 0
for m in messages:
    result = re.match(rule0, m)
    if result:
        if result.span()[0] == 0 and result.span()[1] == len(m):
            matches += 1

print(f'Part 2 Answer: {matches}')
