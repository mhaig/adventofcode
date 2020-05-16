import math
import numpy

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

def cartesian_coordinates(num):
    # Figure out grid size that has input number.
    # print('finding N x N for %d' % num)
    n = math.sqrt(num)
    # print(' N = %f' % n)
    n = int(math.ceil(n))
    # print(' N = %f' % n)
    if n % 2 == 0:
        n += 1
    # print(' N = %d' % n)
    # print('Need a %dx%d grid' % (n, n))
    # Find the corners:
    upper_left = ((n-1) * (n-1)) + 1
    upper_right = (upper_left - n) + 1
    # print([upper_left, upper_right])
    lower_left = upper_left + (n-1)
    lower_right = n * n
    # print([lower_left, lower_right])

    # Figure out grid position of input.
    x, y = 0, 0
    if num >= upper_right and num <= upper_left:
        # Number is on the top of the spiral.
        # print('Number is on the top of the spiral.')
        middle = (n / 2) + upper_right
        x = middle - num
        y = n / 2
        pass
    elif num >= upper_left and num <= lower_left:
        # Number is on the left edge of spiral.
        # print('Number is on the left edge of spiral.')
        middle = (n / 2) + upper_left
        x = -1 * (n / 2)
        y = middle - num
        pass
    elif num >= lower_left and num <= lower_right:
        # Number is on the bottom of the spiral.
        # print('Number is on the bottom of the spiral.')
        middle = (n / 2) + lower_left
        x = num - middle
        y = -1 * (n / 2)
        pass
    else:
        # Number is on the right edge of the spiral.
        # print('Number is on the right edge of the spiral.')
        middle = upper_right - (n / 2)
        x = n / 2
        y = num - middle
        if (num == lower_right):
            y = -1 * (n / 2)
        pass

    return x, y

def cartesian_to_matrix(x, y, N):
    return (N / 2) - y, (N / 2) + x

def solve(input):
    # Figure out grid size that has input number.
    # print('finding N x N for %d' % input)
    N = math.sqrt(input)
    # print(' N = %f' % N)
    N = int(math.ceil(N))
    # print(' N = %f' % N)
    if N % 2 == 0:
        N += 1
    # print(' N = %d' % N)
    # print('Need a %dx%d grid' % (N, N))

    # Make the 2d array
    matrix = numpy.zeros((N,N))

    for p in range(1, input+1):
        # print(p)
        x, y = cartesian_coordinates(p)
        # print([x, y])
        i, j = cartesian_to_matrix(x, y, N)
        # print([i, j])

        # So this algorithm works as is to give us the spiral.  Now the catch
        # is that before writing a value, we need to look at the neighbors for
        # any non-zero, sum the non-zero's and that is the value that is
        # stored.
        # matrix[i, j] = p
        if [x, y] == [0, 0]:
            matrix[i, j] = 1
        else:
            sum = 0
            for a in [-1, 0, 1]:
                for b in [-1, 0, 1]:
                    if i + a < 0 or j + b < 0:
                        val = 0
                    else:
                        try:
                            val = matrix[i + a, j + b]
                            print(val)
                        except:
                            val = 0
                    sum += val
            matrix[i, j] = sum
            if (sum > input):
                print(sum)
                exit()
        print(matrix)

    print(matrix)

    return matrix


# x = [1, 12, 23, 1024, 312051]
x = [312051]
for i in x:
    solve(i)
