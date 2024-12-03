#!/usr/bin/env python3

import sys


class Report(object):

    def __init__(self, report):

        self._report = [int(x) for x in report.split()]

        self._safe = self._is_safe(self._report)

    def _is_safe(self, report):

        running_diff = 0
        for i, level in enumerate(report):

            if i + 1 >= len(report):
                break

            # Assume increasing.
            diff = report[i + 1] - level
            if diff == 0 or abs(diff) > 3:
                return False

            if (diff > 0 and running_diff >= 0) or (
                diff < 0 and running_diff <= 0
            ):
                # List is still safe, keep going.
                running_diff += diff
            else:
                return False

        return True

    def is_safe(self):
        return self._safe

    def could_be_safe(self):
        if self._safe:
            return True

        # Re-run bad reports by removing a level to see if it's good.
        for i in range(len(self._report)):
            if self._is_safe(self._report[:i] + self._report[i + 1 :]):
                return True

        return False


reports = [Report(x) for x in list(sys.stdin.readlines())]

print("Day 2 Part 1 Solution: %d" % sum([x.is_safe() for x in reports]))

print("Day 2 Part 2 Solution: %d" % sum([x.could_be_safe() for x in reports]))
