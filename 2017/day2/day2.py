import sys

data = ''
for line in sys.stdin:
    data += line

data = data[:-1]

checksum = 0
for line in data.split('\n'):
    line = [int(x) for x in line.split('\t') if (x != ' ' and x != '\t')]
    print(line)
    checksum = checksum + (max(line) - min(line))

print(checksum)
