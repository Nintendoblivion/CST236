"""
Test for source.shape_checker
"""
from source.shape_checker import get_triangle_type
from source.shape_checker import get_quad_type
from source.shape_checker import get_quad_type_with_angle
from unittest import TestCase


class TestGetTriangleType(TestCase):

    def test_get_triangle_equilateral_all_int(self):
        result = get_triangle_type(1, 1, 1)
        self.assertEqual(result, 'equilateral')

    def test_get_triangle_scalene_all_int(self):
        result = get_triangle_type(1, 2, 3)
        self.assertEqual(result, 'scalene')

    def test_get_triangle_isosceles_all_int(self):
        result = get_triangle_type(1, 1, 2)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_invalid_all_zero(self):
        result = get_triangle_type(0, 0, 0)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_invalid_two_zero(self):
        result = get_triangle_type(1, 0, 0)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_invalid_one_zero(self):
        result = get_triangle_type(1, 1, 0)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_invalid_all_char(self):
        result = get_triangle_type('A', 'B', 'C')
        self.assertEqual(result, 'invalid')

    def test_get_triangle_invalid_two_char(self):
        result = get_triangle_type('A', 2, 'C')
        self.assertEqual(result, 'invalid')

    def test_get_triangle_invalid_one_char(self):
        result = get_triangle_type('A', 2, 2)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_equilateral_tuple(self):
        T = 1, 1, 1
        result = get_triangle_type(T)
        self.assertEqual(result, 'equilateral')

    def test_get_triangle_equilateral_list(self):
        L = [1, 1, 1]
        result = get_triangle_type(L)
        self.assertEqual(result, 'equilateral')

    def test_get_triangle_equilateral_dict(self):
        T = {"One": 1, "Two":1, "Three":1}
        result = get_triangle_type(T)
        self.assertEqual(result, 'equilateral')


class TestGetQuadType(TestCase):

    def test_get_quadrilateral_square(self):
        result = get_quad_type(1,1,1,1)
        self.assertEqual(result, 'square')

    def test_get_quadrilateral_rect_A(self):
        result = get_quad_type(1,2,1,2)
        self.assertEqual(result, 'rectangle')

    def test_get_quadrilateral_rect_B(self):
        result = get_quad_type(1,2,2,1)
        self.assertEqual(result, 'rectangle')

    def test_get_quadrilateral_rect_C(self):
        result = get_quad_type(1,1,2,2)
        self.assertEqual(result, 'rectangle')

    def test_get_quadrilateral_invalid_unequal_sides(self):
        result = get_quad_type(1,2,3,4)
        self.assertEqual(result, 'invalid')

    def test_get_quadrilateral_invalid_one_set_equal_sides(self):
        result = get_quad_type(1,1,2,3)
        self.assertEqual(result, 'invalid')

    def test_get_quadrilateral_invalid_three_equal_sides(self):
        result = get_quad_type(1,1,1,3)
        self.assertEqual(result, 'invalid')

    def test_get_quadrilateral_invalid_all_zero(self):
        result = get_quad_type(0,0,0,0)
        self.assertEqual(result, 'invalid')

    def test_get_quadrilateral_invalid_set_zero(self):
        result = get_quad_type(1,1,0,0)
        self.assertEqual(result, 'invalid')

    def test_get_quadrilateral_tuple(self):
        t = 1,1,1,1
        result = get_quad_type(t)
        self.assertEqual(result, 'square')

    def test_get_quadrilateral_list(self):
        l = [1,1,1,1]
        result = get_quad_type(l)
        self.assertEqual(result, 'square')

    def test_get_quadrilateral_dict(self):
        d = {"One":1,"Two":1,"Three":1,"Four":1}
        result = get_quad_type(d)
        self.assertEqual(result, 'square')

    def test_get_quadrilateral_char(self):
        result = get_quad_type('A', 'A', 'A', 'A')
        self.assertEqual(result, 'invalid')


class TestGetQuadTypeWithAngle(TestCase):

    def test_get_quadrilateral_with_angle_square(self):
        result = get_quad_type_with_angle(1, 1, 1, 1, 90, 90, 90, 90)
        self.assertEqual(result, 'square')

    def test_get_quadrilateral_with_angle_rect_A(self):
        result = get_quad_type_with_angle(1, 2, 1, 2, 90, 90, 90, 90)
        self.assertEqual(result, 'rectangle')

    def test_get_quadrilateral_with_angle_rect_B(self):
        result = get_quad_type_with_angle(1, 2, 2, 1, 90, 90, 90, 90)
        self.assertEqual(result, 'rectangle')

    def test_get_quadrilateral_with_angle_rect_C(self):
        result = get_quad_type_with_angle(1, 1, 2, 2, 90, 90, 90, 90)
        self.assertEqual(result, 'rectangle')

    def test_get_quadrilateral_with_angle_rhombus_A(self):
        result = get_quad_type_with_angle(1, 1, 1, 1, 60, 60, 120, 120)
        self.assertEqual(result, 'rhombus')

    def test_get_quadrilateral_with_angle_rhombus_B(self):
        result = get_quad_type_with_angle(1, 1, 1, 1, 60, 120, 60, 120)
        self.assertEqual(result, 'rhombus')

    def test_get_quadrilateral_with_angle_rhombus_C(self):
        result = get_quad_type_with_angle(1, 1, 1, 1, 60, 120, 120, 60)
        self.assertEqual(result, 'rhombus')

    def test_get_quadrilateral_with_angle_parallelogram_A(self):
        result = get_quad_type_with_angle(1, 2, 1, 2, 60, 60, 120, 120)
        self.assertEqual(result, 'parallelogram')

    def test_get_quadrilateral_with_angle_parallelogram_B(self):
        result = get_quad_type_with_angle(1, 2, 1, 2, 60, 120, 60, 120)
        self.assertEqual(result, 'parallelogram')

    def test_get_quadrilateral_with_angle_parallelogram_C(self):
        result = get_quad_type_with_angle(1, 2, 1, 2, 60, 120, 120, 60)
        self.assertEqual(result, 'parallelogram')

    def test_get_quadrilateral_with_angle_invalid__too_high_angle(self):
        result = get_quad_type_with_angle(1, 1, 1, 1, 360, 360, 360, 360)
        self.assertEqual(result, 'invalid')

    def test_get_quadrilateral_with_angle_invalid__too_low_angle(self):
        result = get_quad_type_with_angle(1, 1, 1, 1, 30, 30, 30, 30)
        self.assertEqual(result, 'invalid')

    def test_get_quadrilateral_with_angle_invalid__angles_not_equal(self):
        result = get_quad_type_with_angle(1, 1, 1, 1, 60, 30, 150, 120)
        self.assertEqual(result, 'invalid')

    def test_get_quadrilateral_with_angle_invalid__one_off_angle(self):
        result = get_quad_type_with_angle(1, 1, 1, 1, 60, 60, 60, 180)
        self.assertEqual(result, 'invalid')

    def test_get_quadrilateral_with_angle_invalid__zero_angles(self):
        result = get_quad_type_with_angle(1, 1, 1, 1, 0, 0, 0, 0)
        self.assertEqual(result, 'invalid')

    def test_get_quadrilateral_with_angle_invalid__zero_sides(self):
        result = get_quad_type_with_angle(0, 0, 0, 0, 90, 90, 90, 90)
        self.assertEqual(result, 'invalid')

    def test_get_quadrilateral_with_angle_invalid__zero_all(self):
        result = get_quad_type_with_angle(0, 0, 0, 0, 0, 0, 0, 0)
        self.assertEqual(result, 'invalid')

    def test_get_quadrilateral_with_angle_tuple(self):
        t = 1, 1, 1, 1, 90, 90, 90, 90
        result = get_quad_type_with_angle(t)
        self.assertEqual(result, 'square')

    def test_get_quadrilateral_with_angle_list(self):
        l = [1, 1, 1, 1, 90, 90, 90, 90]
        result = get_quad_type_with_angle(l)
        self.assertEqual(result, 'square')

    def test_get_quadrilateral_with_angle_dict(self):
        d = {1: 1,2: 1, 3: 1, 4: 1, 5: 90, 6: 90, 7: 90, 8: 90}
        result = get_quad_type_with_angle(d)
        self.assertEqual(result, 'square')