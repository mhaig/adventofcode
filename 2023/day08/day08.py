#!/usr/bin/env python3

import sys


class Node:
    def __init__(self, name: str, left: str, right: str):
        self._name = name
        self._left = left
        self._right = right

    @property
    def name(self) -> str:
        return self._name

    @property
    def left(self) -> str:
        return self._left

    @property
    def right(self) -> str:
        return self._right

    def get(self, direction: chr)->str:
        if direction == 'L':
            return self._left
        elif direction == 'R':
            return self._right
        else:
            raise ValueError

    def __repr__(self) -> str:
        return f"Node({self._name} = ({self._left}, {self._right}))"


game_input = list(sys.stdin.readlines())

node_map = {}
for line in game_input:
    if line == '\n':
        continue

    if '=' in line:
        label = line.split('=')[0].strip()
        left = line.split('=')[1].split(',')[0].strip()[1:]
        right = line.split('=')[1].split(',')[1].strip()[:-1]

        n = Node(label, left, right)
        node_map[label] = n

    else:
        instructions = line.strip()

steps = 0
node = node_map['AAA']
while node.name != 'ZZZ':
    for i in instructions:
        node = node_map[node.get(i)]
        steps += 1
        if node.name == 'ZZZ':
            break

print(steps)
