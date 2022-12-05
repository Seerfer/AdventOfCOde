import unittest

from main import split_string_by_half

class Test(unittest.TestCase):
    def test_split_string_by_half(self):
        input = "vJrwpWtwJgWrhcsFMMfFFhFp"
        expected = ["vJrwpWtwJgWr","hcsFMMfFFhFp"]
        out = split_string_by_half(input)
        self.assertEqual(expected, out)


if __name__ == '__main__':
    unittest.main()