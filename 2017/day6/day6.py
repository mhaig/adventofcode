import sys

data = ''
for line in sys.stdin:
    data += line

data = data[:-1]

memory_banks = [int(x) for x in data.split()]
# Verify that there are exactly 16 memory banks.
if (len(memory_banks) != 16):
    print('Failed to parse input')
    quit()

memory_history = []
memory_history.append(list(memory_banks))

cycle_count = 0

first_infinite_loop = []

while True:
    # Find the bank with the most memory.
    max_blocks = max(memory_banks)
    index = memory_banks.index(max_blocks)

    memory_banks[index] = 0
    index += 1
    while max_blocks > 0:
        memory_banks[index % 16] += 1
        max_blocks -= 1
        index += 1

    cycle_count += 1
    if memory_banks in memory_history:
        print('infinite loop')
        print(cycle_count)
        first_infinite_loop = list(memory_banks)
        break
    else:
        memory_history.append(list(memory_banks))

# Loop again but only look for the one.
cycle_count = 0
while True:
    max_blocks = max(memory_banks)
    index = memory_banks.index(max_blocks)

    memory_banks[index] = 0
    index += 1
    while max_blocks > 0:
        memory_banks[index % 16] += 1
        max_blocks -= 1
        index += 1

    cycle_count += 1
    if memory_banks == first_infinite_loop:
        print('Found it again')
        print(cycle_count)
        quit()
