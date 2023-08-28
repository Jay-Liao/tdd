import unittest

from calculator import Calculator


class CalculatorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_positive_integer_sum(self):
        self.sum_should_be(3, 1, 2)

    def sum_should_be(self, expected, first, second):
        got = self.calculator.sum(1, 2)
        self.assertEqual(expected, got)
