#!/usr/bin/env python
# vim:set fileencoding=utf8: #

class Moon(object):
    """Docstring for Moon."""

    def __init__(self, x, y, z):
        """
        @todo Document Moon.__init__ (along with arguments).

        x - @todo Document argument x.
        y - @todo Document argument y.
        z - @todo Document argument z.
        """
        self._x = int(x)
        self._y = int(y)
        self._z = int(z)

        self._v_x = 0
        self._v_y = 0
        self._v_z = 0

        self._repeat_x = 0
        self._repeat_y = 0
        self._repeat_z = 0

        self._repeat = 0

    @property
    def x(self):
        return self._x

    @property
    def xvx(self):
        return (self._x, self._v_x)

    @property
    def yvy(self):
        return (self._y, self._v_y)

    @property
    def zvz(self):
        return (self._z, self._v_z)

    @property
    def y(self):
        return self._y

    @property
    def z(self):
        return self._z

    @property
    def repeat_x(self):
        return self._repeat_x
    @repeat_x.setter
    def repeat_x(self, value):
        self._repeat_x = value

    @property
    def repeat_y(self):
        return self._repeat_y
    @repeat_y.setter
    def repeat_y(self, value):
        self._repeat_y = value

    @property
    def repeat_z(self):
        return self._repeat_z
    @repeat_z.setter
    def repeat_z(self, value):
        self._repeat_z = value

    @property
    def repeat(self):
        return self._repeat
    @repeat.setter
    def repeat(self, value):
        self._repeat = value

    @property
    def potential_energy(self):
        return (abs(self._x) +
                abs(self._y) +
                abs(self._z))

    @property
    def kinetic_energy(self):
        return (abs(self._v_x) +
                abs(self._v_y) +
                abs(self._v_z))

    @property
    def total_energy(self):
        return self.potential_energy * self.kinetic_energy

    @property
    def position_velocity(self):
        return ((self._x, self._y, self._z), (self._v_x, self._v_y, self._v_z))

    def __str__(self):
        return 'pos=<x={:>4}, y={:>4}, z={:>4}>, vel=<x={:>4}, y={:>4}, z={:>4}>'.format(
            self._x, self._y, self._z, self._v_x, self._v_y, self._v_z)

    def __eq__(self, other):
        if isinstance(other, Moon):
            return (self._x == other._x and
                    self._y == other._y and
                    self._z == other._z and
                    self._v_x == other._v_x and
                    self._v_y == other._v_y and
                    self._v_z == other._v_z)
        else:
            return False

    def update_velocity_x(self, other):
        if self._x < other.x:
            self._v_x += 1
        elif self._x > other.x:
            self._v_x -= 1

    def update_velocity_y(self, other):
        if self._y < other.y:
            self._v_y += 1
        elif self._y > other.y:
            self._v_y -= 1

    def update_velocity_z(self, other):
        if self._z < other.z:
            self._v_z += 1
        elif self._z > other.z:
            self._v_z -= 1

    def update_velocity(self, other):
        self.update_velocity_x(other)
        self.update_velocity_y(other)
        self.update_velocity_z(other)

    def apply_velocity_x(self):
        self._x += self._v_x

    def apply_velocity_y(self):
        self._y += self._v_y

    def apply_velocity_z(self):
        self._z += self._v_z

    def apply_velocity(self):
        self.apply_velocity_x()
        self.apply_velocity_y()
        self.apply_velocity_z()
