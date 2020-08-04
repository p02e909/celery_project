import unittest

from .base import Test
from ..tasks import calcular_rectangle


class TestCalcularRectangle(Test):

    def test_calcular_rectangle(self):
        rectangle_one = {
            'a': 1,
            'b': 1,
            'area' : 1,
            'perimeter': 4,
        }

        rectangle_zero_1_side = {
            'a': 0,
            'b': 1,
            'area' : None,
            'perimeter': None,
        }

        rectangle_negative_1_side = {
            'a': -1,
            'b': 1,
            'area' : None,
            'perimeter': None,
        }

        rectangle_negative_2_side = {
            'a': -1,
            'b': -1,
            'area' : None,
            'perimeter': None,
        }

        rectangle_big_side = {
            'a': 100000,
            'b': 1000000,
            'area' : 100000000000,
            'perimeter': 2200000,
        }

        cases = [
            rectangle_one,
            rectangle_zero_1_side,
            rectangle_big_side,
            rectangle_negative_1_side,
            rectangle_negative_2_side,
        ]
        self._test_all(calcular_rectangle, cases)


if __name__ == "__main__":
    unittest.main()

