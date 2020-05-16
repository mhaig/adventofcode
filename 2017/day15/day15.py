from __future__ import print_function
import sys

GENERATOR_A_FACTOR = 16807
GENERATOR_B_FACTOR = 48271
DIVISOR = 2147483647

def get_input():
    """Get input from stdin and return as a string."""
    # TODO move into something common so I can pull this out of all these
    # scripts.
    data = ''
    for line in sys.stdin:
        data += line

    data = data[:-1]

    return data

def main():
    
    generator_input = get_input()
    print(generator_input)
    generator_a_start = int(generator_input.split('\n')[0].split()[-1])
    generator_b_start = int(generator_input.split('\n')[1].split()[-1])

    print(generator_a_start)
    print(generator_b_start)

    generator_a = generator_a_start
    generator_b = generator_b_start
    judge = 0
    generator_a_list = []
    generator_b_list = []
    for i in range(40000000):
        # Calculate
        generator_a = ((generator_a * GENERATOR_A_FACTOR) % DIVISOR)
        generator_b = ((generator_b * GENERATOR_B_FACTOR) % DIVISOR)
        # print('%i   %i' % (generator_a, generator_b))
        generator_a_list.append(generator_a)
        generator_b_list.append(generator_b)
        if (generator_a_list[i] & 0xFFFF) == (generator_b_list[i] & 0xFFFF):
            judge += 1


            
        # if generator_a % 4 == 0:
        # if generator_b % 8 == 0:

    print('Part 1 Judge: %d' % judge)

    generator_a_list = [x for x in generator_a_list if x % 4 == 0]
    generator_b_list = [x for x in generator_b_list if x % 8 == 0]
    
    judge = 0
    for i in range(min(len(generator_a_list), len(generator_b_list))):
        if (generator_a_list[i] & 0xFFFF) == (generator_b_list[i] & 0xFFFF):
            judge += 1

    print('Part 2 Judge: %d' % judge)

if __name__ == '__main__':
    main()