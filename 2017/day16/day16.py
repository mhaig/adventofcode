from __future__ import print_function
import sys
from collections import Counter

def get_input():
    """Get input from stdin and return as a string."""
    # TODO move into something common so I can pull this out of all these
    # scripts.
    data = ''
    for line in sys.stdin:
        data += line

    data = data[:-1]

    return data

def move_dancers(move, dancers):
    if move[0] == 's':
        # Spin
        count = -1 * int(move[1:])
        # Split string at -count and move that slice to the front.
        temp = dancers[count:]
        temp.extend(dancers[:16+count])
        dancers = temp
    elif move[0] == 'x':
        # Exchange
        a = int(move[1:].split('/')[0])
        b = int(move[1:].split('/')[1])
        temp = dancers[a]
        dancers[a] = dancers[b]
        dancers[b] = temp
    elif move[0] == 'p':
        # Partner
        a = move[1:].split('/')[0]
        b = move[1:].split('/')[1]
        index_a = dancers.index(a)
        index_b = dancers.index(b)
        dancers[index_a] = b
        dancers[index_b] = a
    else:
        print('Could not handle %s' % move)
        quit()

    return dancers

def main():

    moves = get_input()
    moves = moves.split(',')

    dancers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', \
               'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']

    for move in moves:
        dancers = move_dancers(move, dancers)

    print(''.join(dancers))

    # Pattern repeats every 60 rounds.  Generate a list of 60 and then use
    # modulo of 1,000,000,000 to determine what the final positions would be.
    dancers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', \
               'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
    old_dancers = []
    for i in xrange(60):
        for move in moves:
            dancers = move_dancers(move, dancers)
        old_dancers.append(''.join(dancers))

    print(len(old_dancers))
    # print(old_dancers[0])
    # print(old_dancers[60])
    index = 1000000000 % 60
    print(index)
    # Answer is index-1 for some reason.  Should probably figure this out so I
    # Can understand it.
    print(old_dancers[index-1])

if __name__ == '__main__':
    main()