"""
Test for source.shape_checker
"""
from unittest import TestCase
from test.plugins.ReqTracer import requirements
from shape_checker import get_triangle_type, get_quad_type


class TestGetTriangleType(TestCase):

# 1. Tests that check each type of triangle
    @requirements(['#0001', '#0002'])
    def test_get_triangle_equilateral_all_int(self):
        result = get_triangle_type(1, 1, 1)
        self.assertEqual(result, 'equilateral')

    @requirements(['#0001', '#0002'])
    def test_get_triangle_invalid_all_int(self):
        result = get_triangle_type(1, 2, 3)
        self.assertEqual(result, 'invalid')

    @requirements(['#0001', '#0002'])
    def test_get_triangle_isosceles_all_int(self):
        result = get_triangle_type(1, 2, 2)
        self.assertEqual(result, 'isosceles')

    @requirements(['#0001', '#0002'])
    def test_get_triangle_scalene_all_int(self):
        result = get_triangle_type(4, 5, 7)
        self.assertEqual(result, 'scalene')

# 4. Do you have at least three test cases that represent valid isosceles
# triangles such that you have tried all three permutations of two equal
# sides (such as, 3, 3, 4; 3, 4, 3; and 4, 3, 3)?
    @requirements(['#0001', '#0002'])
    def test_get_triangle_isosceles_all_int2(self):
        result = get_triangle_type(2, 2, 1)
        self.assertEqual(result, 'isosceles')

    @requirements(['#0001', '#0002'])
    def test_get_triangle_isosceles_all_int3(self):
        result = get_triangle_type(2, 1, 2)
        self.assertEqual(result, 'isosceles')

# 5. Do you have a test case in which one side has a zero value?
    @requirements(['#0001', '#0002'])
    def test_get_triangle_invalid_all_int2(self):
        result = get_triangle_type(2, 0, 2)
        self.assertEqual(result, 'invalid')

    @requirements(['#0001', '#0002'])
    def test_get_triangle_invalid_all_int3(self):
        result = get_triangle_type(2, 2, 0)
        self.assertEqual(result, 'invalid')

# 6. Do you have a test case in which one side has a negative value?
    @requirements(['#0001', '#0002'])
    def test_get_triangle_invalid_all_int4(self):
        result = get_triangle_type(2, -2, 3)
        self.assertEqual(result, 'invalid')

# 7. Do you have a test case with three integers greater than zero such that
# the sum of two of the numbers is equal to the third? (That is, if the
# program said that 1, 2, 3 represents a scalene triangle, it would contain
# a bug.)
    @requirements(['#0001', '#0002'])
    def test_get_triangle_invalid_all_int5(self):
        result = get_triangle_type(2, 2, 4)
        self.assertEqual(result, 'invalid')

# 8. Do you have at least three test cases in category 7 such that you have
# tried all three permutations where the length of one side is equal to
# the sum of the lengths of the other two sides (e.g., 1, 2, 3; 1, 3, 2; and
# 3, 1, 2)?
    @requirements(['#0001', '#0002'])
    def test_get_triangle_invalid_all_int6(self):
        result = get_triangle_type(2, 4, 2)
        self.assertEqual(result, 'invalid')

    @requirements(['#0001', '#0002'])
    def test_get_triangle_invalid_all_int7(self):
        result = get_triangle_type(4, 2, 2)
        self.assertEqual(result, 'invalid')

# 9. Do you have a test case with three integers greater than zero such that
# the sum of two of the numbers is less than the third (such as 1, 2, 4 or
# 12, 15, 30)?
    @requirements(['#0001', '#0002'])
    def test_get_triangle_invalid_all_int8(self):
        result = get_triangle_type(4, 6, 15)
        self.assertEqual(result, 'invalid')

    @requirements(['#0001', '#0002'])
    def test_get_triangle_invalid_all_int9(self):
        result = get_triangle_type(4, 5, 22)
        self.assertEqual(result, 'invalid')

    @requirements(['#0001', '#0002'])
    def test_get_triangle_invalid_all_int10(self):
        result = get_triangle_type(50, 50, 101)
        self.assertEqual(result, 'invalid')

# 10. Do you have at least three test cases in category 9 such that you have
# tried all three permutations (e.g., 1, 2, 4; 1, 4, 2; and 4, 1, 2)?
    @requirements(['#0001', '#0002'])
    def test_get_triangle_invalid_all_int11(self):
        result = get_triangle_type(101, 50, 50)
        self.assertEqual(result, 'invalid')

    @requirements(['#0001', '#0002'])
    def test_get_triangle_invalid_all_int12(self):
        result = get_triangle_type(22, 4, 5)
        self.assertEqual(result, 'invalid')

    @requirements(['#0001', '#0002'])
    def test_get_triangle_invalid_all_int13(self):
        result = get_triangle_type(50, 101, 50)
        self.assertEqual(result, 'invalid')

# 11. Do you have a test case in which all sides are zero (0, 0, 0)?
    @requirements(['#0001', '#0002'])
    def test_get_triangle_invalid_all_int14(self):
        result = get_triangle_type()
        self.assertEqual(result, 'invalid')

    @requirements(['#0001', '#0002'])
    def test_get_triangle_invalid_all_int15(self):
        result = get_triangle_type(0, 0, 0)
        self.assertEqual(result, 'invalid')

# 12. Do you have at least one test case specifying non-integer values
# (such as 2.5, 3.5, 5.5)?
    @requirements(['#0001', '#0002'])
    def test_get_triangle_equilateral_all_float(self):
        result = get_triangle_type(3.2, 3.2, 3.2)
        self.assertEqual(result, 'equilateral')

    @requirements(['#0001', '#0002'])
    def test_get_triangle_scalene_all_float(self):
        result = get_triangle_type(3.1, 3.2, 3.3)
        self.assertEqual(result, 'scalene')

    @requirements(['#0001', '#0002'])
    def test_get_triangle_isosceles_all_float(self):
        result = get_triangle_type(3.1, 3.1, 5.2)
        self.assertEqual(result, 'isosceles')

# 13. Do you have at least one test case specifying the wrong number of
# values (two rather than three integers, for example)?
    @requirements(['#0001', '#0002'])
    def test_get_triangle_invalid_args_all_int0(self):
        result = get_triangle_type()
        self.assertEqual(result, 'invalid')

    @requirements(['#0001', '#0002'])
    def test_get_triangle_invalid_args_all_int1(self):
        result = get_triangle_type(1)
        self.assertEqual(result, 'invalid')

    @requirements(['#0001', '#0002'])
    def test_get_triangle_invalid_args_all_int2(self):
        result = get_triangle_type(1, 2)
        self.assertEqual(result, 'invalid')

    @requirements(['#0001', '#0002'])
    def test_get_triangle_invalid_args_all_int3(self):
        self.assertRaises(Exception, get_triangle_type, 1, 2, 3, 4)

# 14. Tests to check improper inputs
    @requirements(['#0001', '#0002'])
    def test_get_triangle_invalid_args_all_wrong(self):
        result = get_triangle_type(1, 2, 'a')
        self.assertEqual(result, 'invalid')

    @requirements(['#0001', '#0002'])
    def test_get_triangle_invalid_args_all_wrong1(self):
        result = get_triangle_type('a', 'b', 'c')
        self.assertEqual(result, 'invalid')

    @requirements(['#0001', '#0002'])
    def test_get_triangle_invalid_args_all_wrong2(self):
        result = get_triangle_type('&', '%', '*')
        self.assertEqual(result, 'invalid')

# -----------------------------------------------------------#
# get_quad_type(a, b, c, d) test cases
# -----------------------------------------------------------#

# 1. Tests that check each type of quadrilateral
    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_all_types1(self):
        result = get_quad_type(1, 1, 1, 1)
        self.assertEqual(result, 'Square')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_all_types2(self):
        result = get_quad_type(1, 2, 1, 2)
        self.assertEqual(result, 'rectangle')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_all_types3(self):
        result = get_quad_type(1, 2, 1, 2, 45, 135, 45, 135)
        self.assertEqual(result, 'rhombus')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_all_types4(self):
        result = get_quad_type(1, 2, 1, 2, 45, 45, 45, 45)
        self.assertEqual(result, 'disconnected')

# 4. Do you have at least three test cases that check all permutations
    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_permutations1(self):
        result = get_quad_type(2, 1, 2, 1)
        self.assertEqual(result, 'rectangle')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_permutations2(self):
        result = get_quad_type(1, 2, 1, 2)
        self.assertEqual(result, 'rectangle')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_permutations3(self):
        result = get_quad_type(2, 1, 2, 1, 45, 135, 45, 135)
        self.assertEqual(result, 'rhombus')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_permutations4(self):
        result = get_quad_type(2, 1, 2, 1, 135, 45, 135, 45)
        self.assertEqual(result, 'rhombus')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_permutations5(self):
        result = get_quad_type(1, 2, 1, 2, 135, 45, 135, 45)
        self.assertEqual(result, 'rhombus')

# 5. Do you have a test case in which one side has a zero value?
    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_zeroes1(self):
        result = get_quad_type(0, 1, 2, 1, 135, 45, 135, 45)
        self.assertEqual(result, 'invalid')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_zeroes2(self):
        result = get_quad_type(2, 0, 2, 1, 135, 45, 135, 45)
        self.assertEqual(result, 'invalid')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_zeroes3(self):
        result = get_quad_type(0, 1, 0, 1, 135, 45, 135, 45)
        self.assertEqual(result, 'invalid')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_zeroes4(self):
        result = get_quad_type(0, 1, 2, 1)
        self.assertEqual(result, 'invalid')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_zeroes5(self):
        result = get_quad_type(2, 0, 2, 1)
        self.assertEqual(result, 'invalid')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_zeroes6(self):
        result = get_quad_type(0, 1, 0, 1)
        self.assertEqual(result, 'invalid')

# 6. Do you have a test case in which one side has a negative value?
    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_negative_inputs(self):
        result = get_quad_type(-2, 1, 2, 1)
        self.assertEqual(result, 'invalid')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_negative_inputs1(self):
        result = get_quad_type(2, -1, 2, -1, 45, 135, 45, 135)
        self.assertEqual(result, 'invalid')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_negative_inputs2(self):
        result = get_quad_type(-4, 2, -4, 2, 90, 90, 90, 90)
        self.assertEqual(result, 'invalid')

# 7. Test case with integers greater than zero that don't create a rectangle, square, or rhombus
    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_non_matching_values1(self):
        result = get_quad_type(4, 2, 3, 2, 90, 90, 90, 90)
        self.assertEqual(result, 'invalid')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_non_matching_values2(self):
        result = get_quad_type(7, 2, 2, 2, 90, 90, 90, 90)
        self.assertEqual(result, 'invalid')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_non_matching_values3(self):
        result = get_quad_type(2, 2, 2, 3, 90, 90, 90, 90)
        self.assertEqual(result, 'invalid')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_non_matching_values4(self):
        result = get_quad_type(2, 2, 3, 2, 90, 90, 90, 90)
        self.assertEqual(result, 'invalid')

# 11. Do you have a test case in which all sides are zero (0, 0, 0, 0)?
    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_all_zeroes1(self):
        result = get_quad_type(0, 0, 0, 0)
        self.assertEqual(result, 'invalid')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_all_zeroes2(self):
        result = get_quad_type(0, 0, 0, 0, 0, 0, 0, 0)
        self.assertEqual(result, 'invalid')

# 12. Do you have at least one test case specifying non-integer values
# (such as 2.5, 3.5, 5.5)?
    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_floats1(self):
        result = get_quad_type(2.5, 2.5, 2.5, 2.5)
        self.assertEqual(result, 'Square')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_floats2(self):
        result = get_quad_type(3.3, 3.3, 3.3, 3.3, 90, 90, 90, 90)
        self.assertEqual(result, 'Square')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_floats3(self):
        result = get_quad_type(2.5, 5.5, 2.5, 5.5)
        self.assertEqual(result, 'rectangle')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_floats4(self):
        result = get_quad_type(3.3, 3.7, 3.3, 3.7, 90, 90, 90, 90)
        self.assertEqual(result, 'rectangle')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_floats5(self):
        result = get_quad_type(2.5, 5.5, 2.5, 5.5, 45, 135, 45, 135)
        self.assertEqual(result, 'rhombus')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_floats6(self):
        result = get_quad_type(3.3, 3.7, 3.3, 3.7, 100, 125, 135, 60)
        self.assertEqual(result, 'disconnected')

# 13. Do you have at least one test case specifying the wrong number of
# values (two rather than three integers, for example)?
    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_number_of_inputs0(self):
        result = get_quad_type()
        self.assertEqual(result, 'invalid')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_number_of_inputs1(self):
        result = get_quad_type(1)
        self.assertEqual(result, 'invalid')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_number_of_inputs2(self):
        result = get_quad_type(1, 1)
        self.assertEqual(result, 'invalid')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_number_of_inputs3(self):
        result = get_quad_type(1, 1, 1)
        self.assertEqual(result, 'invalid')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_number_of_inputs4(self):
        result = get_quad_type(1, 1, 1, 1)
        self.assertEqual(result, 'Square')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_number_of_inputs5(self):
        result = get_quad_type(1, 1, 1, 1, 90)
        self.assertEqual(result, 'Square')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_number_of_inputs6(self):
        result = get_quad_type(1, 2, 1, 2, 45)
        self.assertEqual(result, 'disconnected')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_number_of_inputs7(self):
        result = get_quad_type(1, 2, 1, 2, 90)
        self.assertEqual(result, 'rectangle')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_number_of_inputs8(self):
        result = get_quad_type(1, 2, 1, 2, 45)
        self.assertEqual(result, 'disconnected')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_number_of_inputs9(self):
        result = get_quad_type(1, 1, 1, 1, 45, 45)
        self.assertEqual(result, 'disconnected')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_number_of_inputs10(self):
        result = get_quad_type(1, 2, 1, 2, 135, 45, 135)
        self.assertEqual(result, 'disconnected')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_number_of_inputs11(self):
        self.assertRaises(Exception, get_quad_type(), 1, 2, 1, 2, 45, 90, 45, 90, 111)

# 14. Tests to check improper inputs
    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_symbol_inputs0(self):
        result = get_quad_type('*', '%', '&', 'g')
        self.assertEqual(result, 'invalid')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_symbol_inputs1(self):
        result = get_quad_type(3.3, 3.7, 3.3, 3.7, 90, 'f', 90, 90)
        self.assertEqual(result, 'invalid')

# coverage
    @requirements(['#0002'])
    def test_ask_triangle_equilateral_tuple(self):
        result = get_triangle_type([1, 1, 1])
        self.assertEqual(result, 'equilateral')

    @requirements(['#0002'])
    def test_ask_triangle_equilateral_dict(self):
        dict1 = {'one': 1, 'two': 1.1, 'three': 1}
        result = get_triangle_type(dict1)
        self.assertEqual(result, 'isosceles')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_tuple(self):
        result = get_quad_type([3.3, 3.3, 3.3, 3.3, 90, 90, 90, 90])
        self.assertEqual(result, 'Square')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_dict_angles(self):
        dict2 = {'one': 1, 'two': 1, 'three': 1, 'four': 1, 'one1': 90, 'two1': 180, 'three1': 90, 'four1': 90}
        result = get_quad_type(dict2)
        self.assertEqual(result, 'disconnected')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_large_angle(self):
        result = get_quad_type([3.3, 3.3, 3.3, 3.3, 3690, 3690, 3690, 3690])
        self.assertEqual(result, 'Square')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_large_negative_angle(self):
        result = get_quad_type([3.3, 3.3, 3.3, 3.3, -3870, -3870, -3870, -3870])
        self.assertEqual(result, 'Square')