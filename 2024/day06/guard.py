class Guard(object):

    def __init__(self):
        self._x = 0
        self._y = 0
        self._char = "^"

    @property
    def pos(self):
        return [self._x, self._y]

    @pos.setter
    def pos(self, value):
        assert isinstance(value, (list, tuple))
        if len(value) == 2:
            assert isinstance(value[0], int)
            assert isinstance(value[1], int)
            self._x = value[0]
            self._y = value[1]
        else:
            raise ValueError()

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def move_n(self):
        self._y -= 1

    def move_s(self):
        self._y += 1

    def move_e(self):
        self._x += 1

    def move_w(self):
        self._x -= 1

    def turn(self):
        if self._char == "^":
            self._char = ">"
        elif self._char == ">":
            self._char = "v"
        elif self._char == "v":
            self._char = "<"
        elif self._char == "<":
            self._char = "^"
        else:
            raise Exception()

    def move(self):
        if self._char == "^":
            self.move_n()
        elif self._char == ">":
            self.move_e()
        elif self._char == "v":
            self.move_s()
        elif self._char == "<":
            self.move_w()
        else:
            raise Exception()
