import math

"""
17  16  15  14  13
18   5   4   3  12
19   6   1   2  11
20   7   8   9  10
21  22  23  24  25

-2,0 => 19
-1,0 => 6
 0,0 => 1
 1,0 => 2
 2,0 => 11

-2,2  => 17    4 * 4 + 1
-1,1  => 5     2 * 2 + 1
 0,0  => 1
 1,-1 => 9     3 * 3
 2,-2 => 25    5 * 5


NxN odd      == lower right corner
NxN even + 1 == upper left corner

"""

def manhattan_distance(x, y):
    return math.fabs(x) + math.fabs(y)

def solve(input):
    # Figure out grid size that has input number.
    print('finding N x N for %d' % input)
    N = math.sqrt(input)
    print(' N = %f' % N)
    N = int(math.ceil(N))
    print(' N = %f' % N)
    if N % 2 == 0:
        N += 1
    print(' N = %d' % N)
    print('Need a %dx%d grid' % (N, N))

    # Find the corners:
    upper_left = ((N-1) * (N-1)) + 1
    upper_right = (upper_left - N) + 1
    print([upper_left, upper_right])
    lower_left = upper_left + (N-1)
    lower_right = N * N
    print([lower_left, lower_right])

    # Figure out grid position of input.
    x, y = 0, 0
    if input >= upper_right and input <= upper_left:
        # Number is on the top of the spiral.
        print('Number is on the top of the spiral.')
        middle = (N / 2) + upper_right
        x = middle - input
        y = N / 2
        pass
    elif input >= upper_left and input <= lower_left:
        # Number is on the left edge of spiral.
        print('Number is on the left edge of spiral.')
        middle = (N / 2) + upper_left
        x = -1 * (N / 2)
        y = middle - input
        pass
    elif input >= lower_left and input <= lower_right:
        # Number is on the bottom of the spiral.
        print('Number is on the bottom of the spiral.')
        middle = (N / 2) + lower_left
        x = input - middle
        y = -1 * (N / 2)
        pass
    else:
        # Number is on the right edge of the spiral.
        print('Number is on the right edge of the spiral.')
        middle = upper_right - (N / 2)
        x = N / 2
        y = input - middle
        if (input == lower_right):
            y = -1 * (N / 2)
        pass

    print([x, y])
    print(manhattan_distance(x, y))



x = [1, 12, 23, 1024, 312051]
for i in x:
    solve(i)
