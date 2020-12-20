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
print(rule0)

matches = 0
for m in messages:
    result = re.match(rule0, m)
    if result:
        if result.span()[0] == 0 and result.span()[1] == len(m):
            matches += 1

print(f'Part 1 Answer: {matches}')
