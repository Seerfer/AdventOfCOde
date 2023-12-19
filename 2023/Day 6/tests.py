import unittest

from main import calculate_distance, find_zeros_quadratic_func


class Test_calculate_distance(unittest.TestCase):
    def test_calculate_distance_no_hold(self):
        hold_time = 0
        time = 100

        output = calculate_distance(hold_time, time)
        expected = 0
        self.assertEqual(output, expected)

    def test_calculate_distance_non_zero_hold(self):
        hold_time = 2
        time = 7

        output = calculate_distance(hold_time, time)
        expected = 10
        self.assertEqual(output, expected)

    def test_calculate_distance_negative_hold_time(self):
        hold_time = -2
        time = 7

        with self.assertRaises(ValueError):
            calculate_distance(hold_time, time)

    def test_calculate_distance_negative_race_time(self):
        hold_time = 2
        time = -7

        with self.assertRaises(ValueError):
            calculate_distance(hold_time, time)


class Test_find_zeros_quadratic_func(unittest.TestCase):

    def test_find_zeros_quadratic_func_two_zeros(self):
        a = 1
        b = 12
        c = 32
        expected = (-4, -8)
        output = find_zeros_quadratic_func(a, b, c)
        self.assertEqual(output, expected)

    def test_find_zeros_quadratic_func_non_zeros(self):
        a = 1
        b = 0
        c = 1
        expected = None
        output = find_zeros_quadratic_func(a, b, c)
        self.assertEqual(output, expected)


    def test_find_zeros_quadratic_func_one_zero(self):
        a = 1
        b = -6
        c = 9
        expected = 3
        output = find_zeros_quadratic_func(a, b, c)
        self.assertEqual(output, expected)

