class Rule(object):
    """Docstring for Rule."""

    def __init__(self, name, min1, max1, min2, max2):
        """
        @todo Document Rule.__init__ (along with arguments).

        name - @todo Document argument name.
        min1 - @todo Document argument min1.
        max1 - @todo Document argument max1.
        min2 - @todo Document argument min2.
        max2 - @todo Document argument max2.
        """
        self._name = name
        self._min1 = int(min1)
        self._max1 = int(max1)
        self._min2 = int(min2)
        self._max2 = int(max2)


    @property
    def name(self):
        """Description of function name."""
        return self._name

    @property
    def min1(self):
        """Description of function min1."""
        return self._min1

    @property
    def max1(self):
        """Description of function max1."""
        return self._max1

    @property
    def min2(self):
        """Description of function min2."""
        return self._min2

    @property
    def max2(self):
        return self._max2

    def valid(self, value):
        """Test if a value is valid per the rule."""
        return ((value >= self.min1 and
                 value <= self.max1) or
                (value >= self.min2 and
                 value <= self.max2))

    @staticmethod
    def from_string(string):
        name = string.split(':')[0]
        min1 = string.split(':')[1].split('or')[0].split('-')[0]
        max1 = string.split(':')[1].split('or')[0].split('-')[1]
        min2 = string.split(':')[1].split('or')[1].split('-')[0]
        max2 = string.split(':')[1].split('or')[1].split('-')[1]

        return Rule(name, min1, max1, min2, max2)

    def __str__(self):
        return '{}: {}-{} or {}-{}'.format(self.name, self.min1, self.max1,
                                                      self.min2, self.max2)
    def __repr__(self):
        return str(self)
