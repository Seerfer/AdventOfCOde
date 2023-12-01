import unittest

from main import take_next_n_el, list_count_distinct


class Test_take_next_n_el(unittest.TestCase):
    def test_take_next_n_el_start_begining(self):
        input_data = [1, 2, 3, 4, 5, 6]
        starting = 0
        n = 3
        expected = [2, 3, 4]
        out = take_next_n_el(input_data, starting, n)
        self.assertEqual(expected, out)

    def test_take_next_n_el_start_n_is_0(self):
        input_data = [1, 2, 3, 4, 5, 6]
        starting = 0
        n = 0
        expected = []
        out = take_next_n_el(input_data, starting, n)
        self.assertEqual(expected, out)

    def test_take_next_n_el_start_middle(self):
        input_data = [1, 2, 3, 4, 5, 6]
        starting = 2
        n = 2
        expected = [4, 5]
        out = take_next_n_el(input_data, starting, n)
        self.assertEqual(expected, out)

    def test_take_next_n_negative_n(self):
        input_data = [1, 2, 3, 4, 5, 6]
        starting = 0
        n = -3
        with self.assertRaises(ValueError):
            out = take_next_n_el(input_data, starting, n)

    def test_take_next_n_index_error(self):
        input_data = [1, 2, 3, 4, 5, 6]
        starting = 0
        n = 8
        with self.assertRaises(IndexError):
            out = take_next_n_el(input_data, starting, n)

    def test_take_next_n_negative_starting(self):
        input_data = [1, 2, 3, 4, 5, 6]
        starting = -2
        n = 8
        with self.assertRaises(ValueError):
            out = take_next_n_el(input_data, starting, n)


class Test_list_count_distinct(unittest.TestCase):
    def test_list_count_distinct_no_duplicates(self):
        input_data = [1, 2, 3, 4, 5]
        expected = 5
        out = list_count_distinct(input_data)
        self.assertEqual(expected, out)

    def test_list_count_distinct_with_duplicates(self):
        input_data = [1, 2, 3, 4, 5, 5, 4]
        expected = 5
        out = list_count_distinct(input_data)
        self.assertEqual(expected, out)

    def test_list_count_distinct_empty_list(self):
        input_data = []
        expected = 0
        out = list_count_distinct(input_data)
        self.assertEqual(expected, out)


if __name__ == "__main__":
    unittest.main()
