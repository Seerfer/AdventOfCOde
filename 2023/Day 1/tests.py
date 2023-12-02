import unittest

from main import create_number_from_digits, find_first_value, find_last_value, transform_to_digit



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



class Test_find_first_value(unittest.TestCase):

    def test_find_first_value_no_apperance(self):
        input = "sadjsksd"
        values = ["eight", "two", "seven"]
        expected = None
        out = find_first_value(input, values)
        self.assertEqual(expected, out)

    def test_find_first_value_one_apperance(self):
        input = "dfftwoxxve"
        values = ["eight", "two", "seven"]
        expected = "two"
        out = find_first_value(input, values)
        self.assertEqual(expected, out)

    def test_find_first_value_multiple_apperance(self):
        input = "sdseightdsfvtwo"
        values = ["eight", "two", "seven"]
        expected = "eight"
        out = find_first_value(input, values)
        self.assertEqual(expected, out)



class Test_find_last_value(unittest.TestCase):

    def test_find_last_value_no_apperance(self):
        input = "sadjsksd"
        values = ["eight", "two", "seven"]
        expected = None
        out = find_last_value(input, values)
        self.assertEqual(expected, out)

    def test_find_last_value_one_apperance(self):
        input = "dfftwoxxve"
        values = ["eight", "two", "seven"]
        expected = "two"
        out = find_last_value(input, values)
        self.assertEqual(expected, out)

    def test_find_last_value_multiple_apperance(self):
        input = "sdseightdsfvtwo"
        values = ["eight", "two", "seven"]
        expected = "two"
        out = find_last_value(input, values)
        self.assertEqual(expected, out)

class Test_transform_to_digit(unittest.TestCase):

    def test_transform_to_digit(self):
        input = "one"
        expected = "1"
        out = transform_to_digit(input)
        self.assertEqual(expected, out)

    def test_transform_to_digit_wrong_value(self):
        input = "wrong_val"
        expected = None
        out = transform_to_digit(input)
        self.assertEqual(expected, out)


if __name__ == "__main__":
    unittest.main()
