class SevenSegment(object):

    def __init__(self):

        self._display = (' {0}{0}{0}{0} \n'
                         '{1}    {2}\n'
                         '{1}    {2}\n'
                         ' {3}{3}{3}{3} \n'
                         '{4}    {5}\n'
                         '{4}    {5}\n'
                         ' {6}{6}{6}{6} \n')
        self._a = '.'
        self._b = '.'
        self._c = '.'
        self._d = '.'
        self._e = '.'
        self._f = '.'
        self._g = '.'

        self._zero = [self._a, self._b, self._c, self._e, self._f, self._g]
        self._one = [self._c, self._f]
        self._two = [self._a, self._c, self._d, self._e, self._g]
        self._three = [self._a, self._c, self._d, self._f, self._g]
        self._four = [self._b, self._c, self._d, self._f]
        self._five = [self._a, self._b, self._d, self._f, self._g]
        self._six = [self._a, self._b, self._d, self._e, self._f, self._g]
        self._seven = [self._a, self._c, self._f]
        self._eight = [self._a, self._b, self._c, self._d, self._e, self._f, self._g]
        self._nine = [self._a, self._b, self._c, self._d, self._f, self._g]

        self._temp_zero = []
        self._temp_one = []
        self._temp_two = []
        self._temp_three = []
        self._temp_four = []
        self._temp_five = []
        self._temp_six = []
        self._temp_seven = []
        self._temp_eight = []
        self._temp_nine = []

    def __str__(self):
        return self._display.format(self._a,
                                    self._b,
                                    self._c,
                                    self._d,
                                    self._e,
                                    self._f,
                                    self._g)


    def set_unknown(self, segments):
        segments = [x for x in segments]
        # This is 1.
        if len(segments) == 2 and not self._temp_one:
            self._temp_one = segments

        # This is 7.
        if len(segments) == 3 and not self._temp_seven:
            self._temp_seven = segments

        # This is 4
        if len(segments) == 4 and not self._temp_four:
            self._temp_four = segments

        # This is 8
        if len(segments) == 7 and not self._temp_eight:
            self._temp_eight = segments

        # Could be 2, 3, 5
        if len(segments) == 5:

            # If one is set and one is in segments, the segments are three.
            if self._temp_one:
                if all(s in segments for s in self._temp_one):
                    self._temp_three = segments

        # Could be 0, 6, 9
        if len(segments) == 6:

            # If one is set and one is in segments, the segments are not six.
            if self._temp_one:
                if all(s in segments for s in self._temp_one):
                    # Segments are either 0 or 9
                    if self._temp_four:
                        if all(s in segments for s in self._temp_four):
                            # If four is set and all of four is in segments, it
                            # is 9.
                            self._temp_nine = segments
                        else:
                            # Four is set but not all of four is in segments, must
                            # be 0.
                            self._temp_zero = segments
                else:
                    self._temp_six = segments

        self._rectify()


    def _rectify(self):
        if self._temp_one and self._temp_seven:
            self._a = list((set(self._temp_seven) - set(self._temp_one)))[0]
        if self._temp_eight and self._temp_zero:
            self._d = list((set(self._temp_eight) - set(self._temp_zero)))[0]
        if self._temp_six and self._temp_eight:
            self._c = list(set(self._temp_eight) - set(self._temp_six))[0]
            self._f = list(set(self._temp_one) - set(self._c))[0]
        if self._temp_nine and self._temp_eight:
            self._e = list(set(self._temp_eight) - set(self._temp_nine))[0]
        if self._temp_three and self._temp_four and self._a != '.':
            self._g = list(set(self._temp_three) -
                           set(self._temp_four) -
                           set(self._a))[0]
        if self._temp_four and self._temp_one and self._d:
            self._b = list(set(self._temp_four) -
                           set(self._temp_one) -
                           set(self._d))[0]

        self._zero = [self._a, self._b, self._c, self._e, self._f, self._g]
        self._one = [self._c, self._f]
        self._two = [self._a, self._c, self._d, self._e, self._g]
        self._three = [self._a, self._c, self._d, self._f, self._g]
        self._four = [self._b, self._c, self._d, self._f]
        self._five = [self._a, self._b, self._d, self._f, self._g]
        self._six = [self._a, self._b, self._d, self._e, self._f, self._g]
        self._seven = [self._a, self._c, self._f]
        self._eight = [self._a, self._b, self._c, self._d, self._e, self._f, self._g]
        self._nine = [self._a, self._b, self._c, self._d, self._f, self._g]

    def solved(self):
        if '.' in str(self):
            return False

        return True

    def get_digit(self, digit):
        self._digits = {''.join(sorted(self._zero)):  0,
                        ''.join(sorted(self._one)):   1,
                        ''.join(sorted(self._two)):   2,
                        ''.join(sorted(self._three)): 3,
                        ''.join(sorted(self._four)):  4,
                        ''.join(sorted(self._five)):  5,
                        ''.join(sorted(self._six)):   6,
                        ''.join(sorted(self._seven)): 7,
                        ''.join(sorted(self._eight)): 8,
                        ''.join(sorted(self._nine)):  9}
        return self._digits[''.join(sorted(digit))]

    def debug(self):
        print(self._temp_zero)
        print(self._temp_one)
        print(self._temp_two)
        print(self._temp_three)
        print(self._temp_four)
        print(self._temp_five)
        print(self._temp_six)
        print(self._temp_seven)
        print(self._temp_eight)
        print(self._temp_nine)
