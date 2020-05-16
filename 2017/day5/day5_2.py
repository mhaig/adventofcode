import sys

data = ''
for line in sys.stdin:
    data += line

data = data[:-1]

instructions = data.split('\n')
instructions = [int(x) for x in instructions]

print('Total instructions: %d' % len(instructions))

instruction_pointer = 0
instruction_count = 0

while instruction_pointer < len(instructions):
    # Execute the current instruction.
    jump = instructions[instruction_pointer]
    if jump >= 3:
        instructions[instruction_pointer] -= 1
    else:
        instructions[instruction_pointer] += 1
    instruction_pointer += jump
    instruction_count += 1

print(instruction_count)
