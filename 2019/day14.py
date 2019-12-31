#!/usr/bin/env python
# vim:set fileencoding=utf8: #

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
            self._inputs.append([int(i.split()[0]), i.split()[1]])

        self._output = outputs.split()
        self._output[0] = int(self._output[0])

        self._is_fuel = self._output[1] == 'FUEL'
        self._is_ore = self._inputs[0][1] == 'ORE'

    def is_fuel(self):
        return self._is_fuel

    def is_ore(self):
        return self._is_ore


    def __str__(self):
        string = ''
        for i in self._inputs:
            if string:
                string += ', '
            string += f'{i[0]} {i[1]}'

        string += ' => '
        string += f'{self._output[0]} {self._output[1]}'

        return string

    @property
    def inputs(self):
        return self._inputs

    @property
    def output(self):
        return self._output

def get_reaction(chemical, reactions):
    for r in reactions:
        if r.output[1] == chemical:
            return r

def get_required_ore(reaction, reactions):

    # print(f'Get required ore for{reaction}')

    if reaction.is_ore():
        print(reaction.inputs[0][0])
        return reaction.inputs[0][0]
    else:
        required = 0
        for i in reaction.inputs:
            # ratio = (reaction.
            a_reaction = get_reaction(i[1], reactions)
            required += get_required_ore(a_reaction, reactions)

        return required

def exp(x, y):

    if y == 0:
        return 1

    return x * exp(x, y-1)

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file_name')
args = parser.parse_args()

with open(args.file_name, 'r') as f:
    recipe = f.read()

reactions = []
for line in recipe.split('\n'):
    if line:
        reactions.append(Reaction(line))

print(reactions)
print('\n'.join([str(x) for x in reactions]))

# Find the reaction that results in FUEL
fuel = None
for r in reactions:
    if r.is_fuel():
        fuel = r
        break

print(fuel)

get_required_ore(fuel, reactions)
