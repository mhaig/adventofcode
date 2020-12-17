#!/usr/bin/env python
# vim:set fileencoding=utf8: #

import sys
from rule import Rule
from ticket import Ticket

puzzle_input = sys.stdin.read().strip()

rules = []
your_ticket = None
nearby_tickets = []

is_your_ticket = False
is_nearby_tickets = False
for line in puzzle_input.split('\n'):
    if '-' in line:
        # Parse a rule.
        rules.append(Rule.from_string(line))
    elif 'your ticket' in line:
        is_your_ticket = True
    elif line and is_your_ticket:
        your_ticket = Ticket.from_string(line)
        is_your_ticket = False
    elif 'nearby tickets' in line:
        is_nearby_tickets = True
    elif line and is_nearby_tickets:
        nearby_tickets.append(Ticket.from_string(line))

invalid_fields = []
results = {}

field_rule = [[x,y] for x in range(len(rules)) for y in range(len(rules))]

for i,ticket in enumerate(nearby_tickets):
    is_valid_ticket = True
    for j,num in enumerate(ticket.nums):
        each_rule = [r.valid(num) for r in rules]
        if not any(each_rule):
            invalid_fields.append(num)
            is_valid_ticket = False
        else:
            # Valid ticket, all all rules that passed to dictionary
            for k,result in enumerate(each_rule):
                if not result:
                    field_rule.remove([j,k])

print('Part 1 Answer: {}'.format(sum(invalid_fields)))

# Find the field with the minimum valid rules
rule_count = [0] * len(rules)
for f in range(len(rules)):
    for fr in field_rule:
        if fr[0] == f:
            rule_count[f] += 1

# This is a list.  The index is the field and the value is how many valid rules
# it has.

field_rule_map = {}
for x in range(len(rules)):
    # Get the field of the rule with count x
    index = rule_count.index(x+1)

    # Use the index to find the rule in the field_rule list.
    for j,k in field_rule:
        if j == index:
            rule = k
            break

    field_rule_map[index] = rule

    # Assigned so remove all instances of rule from field_rule list
    field_rule = list(filter(lambda j: j[1] != rule, field_rule))


# What rules start with departure?
part2 = 1
for i, rule in enumerate(rules):
    if 'departure' in rule.name:
        # i is the rule number
        # Get the corresponding field
        for k,v in field_rule_map.items():
            if v == i:
                field = k
        part2 *= your_ticket.nums[field]

print('Part 2 Answer: {}'.format(part2))
