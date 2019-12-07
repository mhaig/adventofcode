#!/usr/bin/env python
# vim:set fileencoding=utf8: #

import sys

class OrbitObject(object):
    """Object that can have one parent and many children."""

    def __init__(self, name):
        """
        name - name of orbit object.
        """
        self._name = name
        self._parent = None
        self._children = []

    def add_child(self, value):
        value.parent = self
        self._children.append(value)

    @property
    def name(self):
        return self._name

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, value):
        self._parent = value

    @property
    def children(self):
        return self._children

    def __str__(self):
        return self._name

objects = {}

orbit_map = [
    [x.split(')')[0], x.split(')')[1]]
    for x in sys.stdin.read().split('\n') if x]

start = OrbitObject(orbit_map[0][0])
objects[start.name] = start
for pair in orbit_map:

    parent = objects.get(pair[0], OrbitObject(pair[0]))
    child = objects.get(pair[1], OrbitObject(pair[1]))

    # Tie them together
    parent.add_child(child)

    # Add them to dictionary if not already there.
    if parent not in objects:
        objects[parent.name] = parent
    if child not in objects:
        objects[child.name] = child

total = 0
def count_children(p, total):

    if not p.children:
        return total

    for c in p.children:
        total = count_children(c, total+1)

    return total

def count_parents(c, total):

    if not c.parent:
        return total

    return count_parents(c.parent, total+1)

# print(f"COM: {count_parents(objects['COM'], 0)}")
# print(f"B:   {count_parents(objects['B'], 0)}")
# print(f"C:   {count_parents(objects['C'], 0)}")
# print(f"D:   {count_parents(objects['D'], 0)}")
# print(f"I:   {count_parents(objects['I'], 0)}")
# print(f"L:   {count_parents(objects['L'], 0)}")

print(f"number of orbits: {sum([count_parents(x, 0) for x in objects.values()])}")

def get_parents(c, parents):
    if not c.parent:
        return parents

    parents.append(c.parent)
    return get_parents(c.parent, parents)

# Get all the parents of YOU
you = []
get_parents(objects['YOU'], you)
you = [str(x) for x in you]

# Get all the parents of SAN
san = []
get_parents(objects['SAN'], san)
san = [str(x) for x in san]

# Distance is amount of unique elements between the two lists.  Basically how
# many elements between the common parent.
print(f"number of transfers: {len(set(you) ^ set(san))}")
