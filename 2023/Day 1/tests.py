import unittest

from main import find_first_digit, find_last_digit, create_number_from_digits


class Test_find_first_digit(unittest.TestCase):
    def test_find_first_digit_digit_at_start(self):
        input = "1dfrgv"
        expected = 1
        out = find_first_digit(input)
        self.assertEqual(expected, out)


    def test_find_first_digit_in_the_middle(self):
        input = "df5rgv"
        expected = 5
        out = find_first_digit(input)
        self.assertEqual(expected, out)


    def test_find_first_no_digit(self):
        input = "dfrgv"
        expected = None
        out = find_first_digit(input)
        self.assertEqual(expected, out)


    def test_find_first_multiple_digits(self):
        input = "d2fr4gv"
        expected = 2
        out = find_first_digit(input)
        self.assertEqual(expected, out)



class Test_find_last_digit(unittest.TestCase):
    def test_find_last_digit_digit_at_end(self):
        input = "dfrgv3"
        expected = 3
        out = find_last_digit(input)
        self.assertEqual(expected, out)


    def test_find_last_digit_in_the_middle(self):
        input = "df5rgv"
        expected = 5
        out = find_last_digit(input)
        self.assertEqual(expected, out)


    def test_find_last_no_digit(self):
        input = "dfrgv"
        expected = None
        out = find_last_digit(input)
        self.assertEqual(expected, out)


    def test_find_last_multiple_digits(self):
        input = "d2fr4gv"
        expected = 4
        out = find_last_digit(input)
        self.assertEqual(expected, out)


class Test_create_number_from_digits(unittest.TestCase):
    def test_create_number_from_digits_one_digit(self):
        expected = 1
        out = create_number_from_digits("1")
        self.assertEqual(expected, out)


    def test_create_number_from_digits_multiple_digit(self):
        expected = 123
        out = create_number_from_digits("1", "2", "3")
        self.assertEqual(expected, out)


    def test_create_number_from_digits_non_digit_char(self):
        with self.assertRaises(ValueError):
            create_number_from_digits("1", "2", "e", "3")


    def test_create_number_from_digits_two_digit_num(self):
        with self.assertRaises(ValueError):
            create_number_from_digits("13", "2", "e", "3")


if __name__ == "__main__":
    unittest.main()
