#!/usr/bin/env python
# vim:set fileencoding=utf8: #

import sys

class Rule(object):
    """Password rule."""

    def __init__(self, min, max, letter):
        """
        @todo Document Rule.__init__ (along with arguments).

        min - @todo Document argument min.
        max - @todo Document argument max.
        letter - @todo Document argument letter.
        """
        self._min = min
        self._max = max
        self._letter = letter

    @staticmethod
    def from_string(string):
        min = int(string.split('-')[0])
        max = int(string.split('-')[1].split()[0])
        letter = string.split()[1][0]

        return Rule(min, max, letter)

    def validate(self, password):
        count = list(password).count(self._letter)
        return count >= self._min and count <= self._max

    def validate2(self, password):
        return (bool(password[self._min-1] == self._letter) ^
                bool(password[self._max-1] == self._letter))


class Password(object):

    def __init__(self, rule, password):
        self._rule = rule
        self._password = password

    def validate(self):
        return self._rule.validate(self._password)

    def validate2(self):
        return self._rule.validate2(self._password)

def line_to_password(line):
    r = Rule.from_string(line.split(':')[0])
    p = Password(r, line.split(': ')[1])

    return p

rules_passwords = list(sys.stdin.readlines())
print('Part 1 Answer: {}'.format(
    [line_to_password(x).validate() for x in rules_passwords].count(True)))
print('Part 2 Answer: {}'.format(
    [line_to_password(x).validate2() for x in rules_passwords].count(True)))
