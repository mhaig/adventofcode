#!/usr/bin/env python
# vim:set fileencoding=utf8: #

import sys
from collections import Counter
from collections import deque

polymer_template = deque()
pair_insertion = {}

for line in sys.stdin.readlines():
    if '->' in line:
        k,v = line.split('->')
        pair_insertion[k.strip()] = v.strip()
    elif line.strip():
        polymer_template = deque([c for c in line.strip()])


print('Template: {}'.format(''.join(polymer_template)))

def do_insertion(template, rules):
    i = 0
    length = len(polymer_template) - 1
    while i < length:
        template.insert(i+1, rules[template[i]+template[i+1]])
        i += 2
        length += 1
    return template

# Part 1
for x in range(10):
    polymer_template = do_insertion(polymer_template, pair_insertion)
    print('Done step {} of {}'.format(x, 10))

counts = Counter(polymer_template)
print('Part 1 Solution: {}'.format(max(counts.values()) - min(counts.values())))

# Part 2
for x in range(10, 40):
    polymer_template = do_insertion(polymer_template, pair_insertion)
    print('Done step {} of {}'.format(x, 40))
