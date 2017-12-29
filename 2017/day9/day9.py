"""
- {}, score of 1.
- {{{}}}, score of 1 + 2 + 3 = 6.
- {{},{}}, score of 1 + 2 + 2 = 5.
- {{{},{},{{}}}}, score of 1 + 2 + 3 + 3 + 3 + 4 = 16.
- {<a>,<a>,<a>,<a>}, score of 1.
- {{<ab>},{<ab>},{<ab>},{<ab>}}, score of 1 + 2 + 2 + 2 + 2 = 9.
- {{<!!>},{<!!>},{<!!>},{<!!>}}, score of 1 + 2 + 2 + 2 + 2 = 9.
- {{<a!>},{<a!>},{<a!>},{<ab>}}, score of 1 + 2 = 3.
"""

import sys

data = ''
for line in sys.stdin:
    data += line

data = data[:-1]

data_list = list(data)

garbage = False
garbage_count = 0
sum = 0
level = 0
token = data_list.pop(0)
debug_list = []
while token:

    print('Processing %s' % token)

    if token == '{' and not garbage:
        level += 1
    elif token == '}' and not garbage:
        debug_list.append(str(level))
        sum += level
        level -= 1
    elif token == '<' and not garbage:
        garbage = True
    elif token == '>':
        garbage = False
    elif token == '!':
        data_list.pop(0)
        pass
    elif token == ',' and garbage:
        print('Garbage!')
        garbage_count += 1
        pass
    elif garbage:
        print('Garbage!')
        garbage_count += 1

    if len(data_list):
        token = data_list.pop(0)
    else:
        token = None

print('+'.join(debug_list))
print(sum)
print(garbage_count)
