"""
b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10
"""

def do_operation(val, operation, amount):
    if operation == 'inc':
        val = val + amount
    else:
        val = val - amount

    return val

import sys

data = ''
for line in sys.stdin:
    data += line

data = data[:-1]

high_value = None

registers = {}
for line in data.split('\n'):
    instruction = line.split()

    register = instruction[0]
    operation = instruction[1]
    amount = int(instruction[2])
    condition = instruction[3:]

    if not registers.has_key(register):
        registers[register] = 0

    if not registers.has_key(condition[1]):
        registers[condition[1]] = 0

    # Evaluate the conditional.
    if condition[2] == '>':
        if registers[condition[1]] > int(condition[3]):
            registers[register] = do_operation(registers[register], operation, amount)
    elif condition[2] == '<':
        if registers[condition[1]] < int(condition[3]):
            registers[register] = do_operation(registers[register], operation, amount)
    elif condition[2] == '>=':
        if registers[condition[1]] >= int(condition[3]):
            registers[register] = do_operation(registers[register], operation, amount)
    elif condition[2] == '==':
        if registers[condition[1]] == int(condition[3]):
            registers[register] = do_operation(registers[register], operation, amount)
    elif condition[2] == '!=':
        if registers[condition[1]] != int(condition[3]):
            registers[register] = do_operation(registers[register], operation, amount)
    elif condition[2] == '<=':
        if registers[condition[1]] <= int(condition[3]):
            registers[register] = do_operation(registers[register], operation, amount)
    else:
        print('Need to implement %s' % condition[2])
        quit()

    # Find the highest value in the registers and store.
    tmp = registers.values()
    tmp.sort()
    tmp = tmp[-1]
    if high_value is None or tmp > high_value:
        high_value = tmp


# Get a list of all the values from the registers.
values = registers.values()
print(values)
values.sort()
print(values)
print(high_value)
