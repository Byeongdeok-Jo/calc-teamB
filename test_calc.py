from unittest import TestCase
from calc import Calc

class TestCalc(TestCase):
    def setUp(self):
        super().setUp()
        self.calc = Calc()

    def test_getSumSum(self):
        self.assertEqual(15, self.calc.getSumSum(3, 5, 7))
        self.assertEqual(-8, self.calc.getSumSum(-3, -5, 0))