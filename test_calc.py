from unittest import TestCase
from calc import Calc

class TestCalc(TestCase):
    def test_get_gom(self):
        sut = Calc()
        self.assertEqual(sut.get_gom(2, 3), 6)


