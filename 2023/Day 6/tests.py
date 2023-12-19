import unittest

from main import calculate_distance


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
