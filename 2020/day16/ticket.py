class Ticket(object):
    """Docstring for Ticket."""

    def __init__(self, nums):
        """
        @todo Document Ticket.__init__ (along with arguments).

        nums - @todo Document argument nums.
        """
        self._nums = nums

    @staticmethod
    def from_string(string):
        return Ticket([int(x) for x in string.split(',')])

    @property
    def nums(self):
        return self._nums

    def __repr__(self):
        return ','.join([str(x) for x in self._nums])
