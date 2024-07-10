from unittest import TestCase
from calc import Calc


class TestCalc(TestCase):
  
    def test_get_gom(self):
        sut = Calc()
        self.assertEqual(sut.get_gom(2, 3), 6)

    def test_get_minus(self):
        calc = Calc()
        self.assertEqual(0, calc.get_minus(5, 5))
        self.assertEqual(2, calc.get_minus(5, 3))
        self.assertEqual(-1, calc.get_minus(5, 6))

    def test_get_divided_value(self):
        sut = Calc()
        expected = sut.get_divided_value(5, 5)

        self.assertEqual(expected, 1)
        
    def test_get_zegop_plus(self):
        cal = Calc()
        self.assertEqual(0, cal.get_zegop(0))
        self.assertEqual(1, cal.get_zegop(1))
        self.assertEqual(4, cal.get_zegop(2))
        self.assertEqual(9, cal.get_zegop(3))
        self.assertEqual(16, cal.get_zegop(4))
        self.assertEqual(25, cal.get_zegop(5))
        self.assertEqual(100, cal.get_zegop(10))

    def test_get_zegop_minus(self):
        cal = Calc()
        self.assertEqual(1, cal.get_zegop(-1))
        self.assertEqual(4, cal.get_zegop(-2))
        self.assertEqual(9, cal.get_zegop(-3))
        self.assertEqual(16, cal.get_zegop(-4))
        self.assertEqual(25, cal.get_zegop(-5))
        self.assertEqual(100, cal.get_zegop(-10))
        
    def test_getSumSum(self):
        calc = Calc()
        self.assertEqual(15, calc.getSumSum(3, 5, 7))
        self.assertEqual(-8, calc.getSumSum(-3, -5, 0))
