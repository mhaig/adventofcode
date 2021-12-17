#!/usr/bin/env python
# vim:set fileencoding=utf8: #

import math
import sys
from collections import Counter
from collections import deque

polymer_template = []
pair_insertion = {}

for line in sys.stdin.readlines():
    if '->' in line:
        k,v = line.split('->')
        pair_insertion[k.strip()] = v.strip()
    elif line.strip():
        polymer_template = [c for c in line.strip()]


# Convert the template to a dictionary of pairs.
polymer_template_dict = {}
for i in range(len(polymer_template)-1):
    pair = ''.join(polymer_template[i:i+2])
    if pair in polymer_template_dict:
        polymer_template_dict[pair] += 1
    else:
        polymer_template_dict[pair] = 1
polymer_template = polymer_template_dict
print('Template: {}'.format(polymer_template))

def do_insertion(template, rules):
    keys_values = list(template.items())
    new_template = {}
    for k,v in keys_values:
        # Based on the rules, get the new pairs that need to inserted or added.
        new_pair1 = k[0] + rules[k]
        new_pair2 = rules[k] + k[1]

        if new_pair1 in new_template:
            new_template[new_pair1] += (1*v)
        else:
            new_template[new_pair1] = 1*v

        if new_pair2 in new_template:
            new_template[new_pair2] += (1*v)
        else:
            new_template[new_pair2] = (1*v)

    return new_template

def count_elements(template):
    counts = {}
    for k,v in template.items():
        for c in k:
            if c in counts:
                counts[c] += v
            else:
                counts[c] = v

    return counts

# Part 1
for x in range(10):
    polymer_template = do_insertion(polymer_template, pair_insertion)

counts = count_elements(polymer_template)
print('Part 1 Solution: {}'.format(math.ceil(max(counts.values())/2) -
                                   math.ceil(min(counts.values())/2)))

# Part 2
for x in range(10, 40):
    polymer_template = do_insertion(polymer_template, pair_insertion)

counts = count_elements(polymer_template)
print('Part 2 Solution: {}'.format(math.ceil(max(counts.values())/2) -
                                   math.ceil(min(counts.values())/2)))
