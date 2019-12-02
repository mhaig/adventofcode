#!/usr/bin/env python
# vim:set fileencoding=utf8: #

class Module(object):
    """Module that requires fuel to be launched into space."""

    def __init__(self, uid: int, mass: int):
        """
        Initialize object.

        uid - Unique ID for module.
        mass - Mass of module.
        """
        self._uid = uid
        self._mass = mass

        self._calculate_fuel_simple()
        self._calculate_fuel()

    @property
    def mass(self):
        return self._mass

    @mass.setter
    def mass(self, value: int):
        self._mass = value
        self._calculate_fuel()
        self._calculate_fuel_simple()

    @property
    def fuel(self):
        return (self._fuel_simple, self._fuel)

    def _calculate_fuel(self):
        """Calculate required fuel to launch module based on mass for part 2.
        """
        self._fuel = self._calculate_fuel_r(self._mass)

    def _calculate_fuel_r(self, mass):
        """Calculate required fuel to launch module based on mass for part 2.
        """
        fuel = (mass // 3) - 2
        if fuel <= 0:
            return 0

        return (self._calculate_fuel_r(fuel) + fuel)

    def _calculate_fuel_simple(self):
        """Calculate required fuel to launch module based on mass for part 1.
        """
        self._fuel_simple = (self.mass // 3) - 2

    def __repr__(self):
        return ('Module(%d, %d, %d, %d)' %
                (self._uid, self._mass, self._fuel_simple, self._fuel))
