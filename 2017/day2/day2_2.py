import sys

data = ''
for line in sys.stdin:
    data += line

data = data[:-1]

checksum = 0
for line in data.split('\n'):
    line = [int(x) for x in line.split() if (x != ' ' and x != '\t')]
    print(line)

    # Find the two numbers that evenly divide.
    done = False
    for i in line:
        for j in line:
            if i == j:
                continue
            elif (i % j) == 0:
                checksum = checksum + (i / j)
                done = True
                break
            elif (j % i) == 0:
                checksum = checksum + (j / i)
                done = True
                break

        if done:
            break

    # checksum = checksum + (max(line) - min(line))

print(checksum)
