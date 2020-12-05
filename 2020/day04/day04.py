#!/usr/bin/env python
# vim:set fileencoding=utf8: #

import sys

class Passport(object):
    """Docstring for Passport."""

    def __init__(self, byr=None, iyr=None, eyr=None, hgt=None, hcl=None,
                 ecl=None, pid=None, cid=None):
        """
        @todo Document Passport.__init__ (along with arguments).

        byr - @todo Document argument byr.
        iyr - @todo Document argument iyr.
        eyr - @todo Document argument eyr.
        hgt - @todo Document argument hgt.
        hcl - @todo Document argument hcl.
        ecl - @todo Document argument ecl.
        pid - @todo Document argument pid.
        cid - @todo Document argument cid.
        """
        self._byr = byr
        self._iyr = iyr
        self._eyr = eyr
        self._hgt = hgt
        self._hcl = hcl
        self._ecl = ecl
        self._pid = pid
        self._cid = cid


    @staticmethod
    def from_string(string):
        key_vals = {}
        for x in string.split():
            try:
                key_vals[x.split(':')[0]] = x.split(':')[1]
            except:
                print('error...')
                print(string)

        return Passport(**key_vals)

    def valid(self):
        field_count = len([x for x in self.__dict__ if self.__dict__[x]])
        return field_count == 8 or (field_count == 7 and not self._cid)

    def valid_byr(self):
        """byr (Birth Year) - four digits; at least 1920 and at most 2002."""
        if int(self._byr) >= 1920 and int(self._byr) <= 2002:
            return True

        return False

    def valid_iyr(self):
        """iyr (Issue Year) - four digits; at least 2010 and at most 2020."""
        if int(self._iyr) >= 2010 and int(self._iyr) <= 2020:
            return True

        return False

    def valid_eyr(self):
        """eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        """
        if int(self._eyr) >= 2020 and int(self._eyr) <= 2030:
            return True

        return False

    def valid_hgt(self):
        """hgt (Height) - a number followed by either cm or in:
            If cm, the number must be at least 150 and at most 193.
            If in, the number must be at least 59 and at most 76.
        """
        if self._hgt[-2:] == 'cm':
            if int(self._hgt[0:-2]) >= 150 and int(self._hgt[0:-2]) <= 193:
                return True
        elif self._hgt[-2:] == 'in':
            if int(self._hgt[0:-2]) >= 59 and int(self._hgt[0:-2]) <= 76:
                return True
        else:
            return False

        return False

    def valid_hcl(self):
        """hcl (Hair Color) - a # followed by exactly six characters 0-9 or
        a-f."""
        if self._hcl[0] == '#' and len(self._hcl[1:]) == 6:
            if len([x for x in self._hcl[1:] if x.isdecimal() or (x.isalpha() and x.islower())]) == 6:
                return True


        return False

    def valid_ecl(self):
        """ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth."""
        return self._ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    def valid_pid(self):
        """pid (Passport ID) - a nine-digit number, including leading zeroes.
        """
        return len(self._pid) == 9

    def secure(self):
        return (self.valid() and
                self.valid_byr() and
                self.valid_iyr() and
                self.valid_eyr() and
                self.valid_hgt() and
                self.valid_hcl() and
                self.valid_ecl() and
                self.valid_pid())

passports = [Passport.from_string(x) for x in sys.stdin.read().split('\n\n')]
print('Part 1 Answer: {}'.format([p.valid() for p in passports].count(True)))
print('Part 2 Answer: {}'.format([p.secure() for p in passports].count(True)))
