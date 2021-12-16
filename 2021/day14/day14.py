#!/usr/bin/env python
# vim:set fileencoding=utf8: #

import sys
from collections import Counter

polymer_template = ''
pair_insertion = {}

for line in sys.stdin.readlines():
    if '->' in line:
        k,v = line.split('->')
        pair_insertion[k.strip()] = v.strip()
    elif line.strip():
        polymer_template = [c for c in line.strip()]


print(polymer_template)
print(pair_insertion)

    # if len(template[pos:]) == 1:
    #     return

    # template.insert(pos+1, rules[''.join(template[pos:pos+2])])

    # do_insertion(template, rules, pos+2)

def do_insertion(template, rules):
    i = 0
    while i < len(polymer_template)-1:
        template.insert(i+1, rules[''.join(template[i:i+2])])
        i += 2
    return template

# Part 1
for x in range(10):
    polymer_template = do_insertion(polymer_template, pair_insertion)
    print('Done step {} of {}'.format(x, 10))

counts = Counter(polymer_template)
print('Part 1 Solution: {}'.format(max(counts.values()) - min(counts.values())))
