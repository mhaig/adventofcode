#!/usr/bin/env python
# vim:set fileencoding=utf8: #

import sys

class Group(object):
    """Docstring for Group."""

    def __init__(self, answers, num_people):
        """
        @todo Document Group.__init__ (along with arguments).

        answers - @todo Document argument answers.
        num_people - @todo Document argument num_people.
        """
        self._answers = answers
        self._num_people = num_people

    def count_all_yes(self):
        all_yes = 0
        for x in self._answers.items():
            if x[1] == self._num_people:
                all_yes += 1

        return all_yes


input_string = sys.stdin.read().strip()

# Break into groups.
groups = input_string.split('\n\n')

group_answers = []
# Process each group.
for g in groups:

    # Break into people
    people = g.split('\n')

    answers = {}
    for p in people:
        for c in p:
            if c in answers:
                answers[c] += 1
            else:
                answers[c] = 1
    group_answers.append(Group(answers, len(people)))

total_keys = sum([len(x._answers.keys()) for x in group_answers])
print('Part 1 Answer: {}'.format(total_keys))
print('Part 2 Answer: {}'.format(sum([x.count_all_yes() for x in group_answers])))
