#!/usr/bin/env python
# vim:set fileencoding=utf8: #

class Chemical(object):

    def __init__(self, name, amount):
        self._name = name
        self._amount = amount

    @property
    def name(self):
        return self._name

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value

    def __str__(self):
        return f'{self._amount} {self._name}'

class Reaction(object):
    """Docstring for Reaction."""

    def __init__(self, string):
        """
        @todo Document Reaction.__init__ (along with arguments).

        arg - @todo Document argument arg.
        """
        self._string = string

        self._inputs = []
        inputs, outputs = string.split('=>')
        for i in inputs.split(','):
            self._inputs.append(Chemical(i.split()[1], int(i.split()[0])))

        self._output = Chemical(outputs.split()[1], int(outputs.split()[0]))

        self._is_fuel = self._output.name == 'FUEL'
        self._is_ore = self._inputs[0].name == 'ORE'

    def is_fuel(self):
        return self._is_fuel

    def is_ore(self):
        return self._is_ore


    def __str__(self):
        string = ''
        for i in self._inputs:
            if string:
                string += ', '
            string += str(i)

        string += ' => '
        string += str(self._output)

        return string

    @property
    def inputs(self):
        return self._inputs

    @property
    def output(self):
        return self._output

def get_reaction(chemical, reactions):
    for r in reactions:
        if r.output.name == chemical:
            return r

final_list = {}
overages = {}
def get_required_ore(amount, reaction, reactions):

    # print(f'Get required ore for {reaction}')

    if reaction.is_ore():
        # print(f'Base element, adding {amount} to final list.')
        final_list[reaction.output.name] += amount
        return
    else:
        # print(f'I need {amount} of {reaction.output.name}')
        if overages.get(reaction.output.name, 0):
            # Reduce amount by overage.
            # print(f'Applying existing overage of {overages[reaction.output.name]}')
            amount -= overages[reaction.output.name]
            overages[reaction.output.name] = 0
        # print(f'I need {amount} of {reaction.output.name}')
        reaction_scale = math.ceil(amount / reaction.output.amount)
        scaled_result = reaction_scale * reaction.output.amount
        # print(f'This reaction will produce {scaled_result} of ' +
              # f'{reaction.output.name}')
        if scaled_result - amount:
            # print(f'overage of {scaled_result - amount}')
            overages[reaction.output.name] = (
                overages.get(reaction.output.name, 0) +
                (scaled_result - amount))
        for i in reaction.inputs:
            a_reaction = get_reaction(i.name, reactions)
            get_required_ore(reaction_scale * i.amount, a_reaction, reactions)

        return

import argparse
import math
import copy

parser = argparse.ArgumentParser()
parser.add_argument('file_name')
args = parser.parse_args()

with open(args.file_name, 'r') as f:
    recipe = f.read()

ores = {}
reactions = []
for line in recipe.split('\n'):
    if line:
        reactions.append(Reaction(line))

        if reactions[-1].is_ore():
            final_list[reactions[-1].output.name] = 0
            ores[reactions[-1].output.name] = (reactions[-1].inputs[0].amount,
                                               reactions[-1].output.amount)

print('\n'.join([str(x) for x in reactions]))

# Find the reaction that results in FUEL
fuel = None
for r in reactions:
    if r.is_fuel():
        fuel = r
        break

print(f'Fuel line: {fuel}')

def calculate_fuel():

    for k in final_list.keys():
        final_list[k] = 0
    for k in overages.keys():
        overages[k] = 0

    # get_required_ore(fuel, reactions)
    for i in fuel.inputs:
        a_reaction1 = get_reaction(i.name, reactions)
        # print(f'I need {i.amount} of {i.name}')
        get_required_ore(i.amount, a_reaction1, reactions) 

    # Use final_list to calculate required ore.
    total = 0
    for k,v in final_list.items():

        # Get ratio for ore
        ratio = ores[k]
        # print(f'Need {v} of {k} at {ratio[1]} {k} to {ratio[0]} ORE')
        total += math.ceil(v / ratio[1]) * ratio[0]

    return total

num = calculate_fuel()
print(f'Part 1 Answer: {num}')

# Double the fuel line.
original_fuel = copy.deepcopy(fuel)
start = 1
stop = 1000000000000
while True:

    if stop - start == 1:
        print(f'Part 2 Answer: {multiplier}')
        break

    # First pick a number half way between start and stop
    multiplier = start + ((stop - start) // 2)
    # print(f'start: {start}')
    # print(f'stop: {stop}')
    # print(f'multiplier: {multiplier}')

    # Get a fresh copy of the fuel line and apply the multiplier.
    fuel = copy.deepcopy(original_fuel)
    for c in fuel.inputs:
        c.amount *= multiplier
    fuel.output.amount *= multiplier
    num = calculate_fuel()
    # print(f'ore needed: {num}')
    if num > 1000000000000:
        # Too much ore needed, new stop point.
        stop = multiplier
    else:
        # Not enough ore needed, new start point.
        start = multiplier
