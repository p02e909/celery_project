import unittest
from .. import my_exception


class Test(unittest.TestCase):

    MESSAGE_FMT = (
        'Input '
        'a: {a}, '
        'b: {b} '
        ' - '
        'expected '
        'perimeter: {perimeter_expect}, '
        'area: {area_expect} '
        ' - '
        'Output '
        'perimeter: {perimeter_output}, '
        'area: {area_output} '
    )

    def _test_all(self, func, cases):
        for case in cases:
            a = case['a']
            b = case['b']
            perimeter_expect, area_expect = case['perimeter'], case['area']

            try:
                perimeter_output, area_output = func(a, b)
            except my_exception.WrongInput:
                perimeter_output = None
                area_output = None

            output = perimeter_output, area_output
            expect = perimeter_expect, area_expect
            msg = self.MESSAGE_FMT.format(
                a=a,
                b=b,
                perimeter_expect=perimeter_expect,
                area_expect=area_expect,
                perimeter_output=perimeter_output,
                area_output=area_output,
            )
            self.assertEqual(output, expect, msg)

