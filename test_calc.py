from unittest import TestCase
from calc import Calc


class TestCalc(TestCase):

    def test_get_minus(self):
        calc = Calc()
        self.assertEqual(0, calc.get_minus(5, 5))
        self.assertEqual(2, calc.get_minus(5, 3))
        self.assertEqual(-1, calc.get_minus(5, 6))

    def test_get_divided_value(self):
        sut = Calc()
        expected = sut.get_divided_value(5, 5)

        self.assertEqual(expected, 1)
