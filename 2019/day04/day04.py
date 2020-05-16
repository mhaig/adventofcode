#!/usr/bin/env python
# vim:set fileencoding=utf8: #

import sys

start, stop = sys.stdin.read().split('-')

print(start, stop)

passwords = []
for x in range(int(start), int(stop)+1):
    password = str(x)

    # Check for one matching adjacent digit.
    matching = False
    for i in range(len(password)-1):
        if password[i] > password[i+1]:
            matching = False
            break

        if password[i] == password[i+1]:
            matching = True

    if matching:
        passwords.append(password)

print(f"Part 1 Passwords: {len(passwords)}")

def check_for_double(pw):

    if pw[0] == pw[1] and pw[0] != pw[2]:
        return True
    elif pw[1] == pw[2] and pw[1] != pw[3] and pw[1] != pw[0]:
        return True
    elif pw[2] == pw[3] and pw[2] != pw[4] and pw[2] != pw[1]:
        return True
    elif pw[3] == pw[4] and pw[3] != pw[5] and pw[3] != pw[2]:
        return True
    elif pw[4] == pw[5] and pw[4] != pw[3]:
        return True

    return False

passwords = []
for x in range(int(start), int(stop)+1):
    password = str(x)

    incrementing = True
    for i in range(len(password)-1):
        # Check that the digits are either the same or incrementing.
        if password[i] > password[i+1]:
            incrementing = False
            break

    if incrementing:
        if check_for_double(password):
            passwords.append(password)

print(f"Part 2 Passwords: {len(passwords)}")
