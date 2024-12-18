import itertools


class Equation(object):

    def __init__(self, equation):
        self._equation = equation

        parts = equation.split(":")
        self._test_value = int(parts[0])
        self._numbers = [int(x) for x in parts[1].split()]
        self._operators = None

    def __str__(self) -> str:
        if self._operators:
            return self._combine(self._operators)
        else:
            return (
                str(self._test_value)
                + " == "
                + " ".join([str(x) for x in self._numbers])
            )

    def _combine(self, operators) -> str:
        operators = list(operators)
        if len(operators) != len(self._numbers):
            operators.append(None)
        string = str(self._test_value) + " == "
        for i, o in zip(self._numbers, operators):
            string += str(i)
            string += " "
            if o:
                string += o
                string += " "

        return string

    def _solve(self, numbers, operators):
        for operands in itertools.product(
            operators, repeat=(len(self._numbers) - 1)
        ):
            nums = list(self._numbers)
            val = nums.pop(0)
            for o in operands:
                if o == "+":
                    val += nums.pop(0)
                elif o == "*":
                    val *= nums.pop(0)
                else:
                    val = int(str(val) + str(nums.pop(0)))

            if val == self._test_value:
                self._operators = operands
                return True

        return False

    def solve_add_mul(self):
        return self._solve(self._numbers, "*+")

    def solve_concat(self):
        return self._solve(self._numbers, "*+|")
