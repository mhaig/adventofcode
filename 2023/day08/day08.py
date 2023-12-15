#!/usr/bin/env python3

import sys
from functools import reduce


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


def lcmn(*args):
    return reduce(lcm, args)


class Node:
    def __init__(self, name: str, left: str, right: str):
        self._name = name
        self._left = left
        self._right = right
        self._steps = 0

    @property
    def name(self) -> str:
        return self._name

    @property
    def left(self) -> str:
        return self._left

    @property
    def right(self) -> str:
        return self._right

    @property
    def steps(self) -> int:
        return self._steps

    @steps.setter
    def steps(self, value: int) -> None:
        if self._steps == 0:
            self._steps = value

    def get(self, direction: str) -> str:
        if direction == "L":
            return self._left
        elif direction == "R":
            return self._right
        else:
            raise ValueError

    def __repr__(self) -> str:
        return f"Node({self._name} = ({self._left}, {self._right}))"


game_input = list(sys.stdin.readlines())

node_map = {}
for line in game_input:
    if line == "\n":
        continue

    if "=" in line:
        label = line.split("=")[0].strip()
        left = line.split("=")[1].split(",")[0].strip()[1:]
        right = line.split("=")[1].split(",")[1].strip()[:-1]

        n = Node(label, left, right)
        node_map[label] = n

    else:
        instructions = line.strip()

steps = 0
node = node_map["AAA"]
while node.name != "ZZZ":
    for i in instructions:
        node = node_map[node.get(i)]
        steps += 1
        if node.name == "ZZZ":
            break

print("Part 1 Solution: {}".format(steps))


# Get all the nodes that end with 'A'.
nodes = []
for k, v in node_map.items():
    if k[-1] == "A":
        nodes.append(v)


steps = 0
steps_to_z = [0] * len(nodes)
while True:
    for i in instructions:
        steps += 1
        for j in range(len(nodes)):
            nodes[j] = node_map[nodes[j].get(i)]
            if nodes[j].name[-1] == "Z":
                if steps_to_z[j] == 0:
                    steps_to_z[j] = steps

    if all(steps_to_z):
        break

print("Part 2 Solution: {}".format(lcmn(*steps_to_z)))
