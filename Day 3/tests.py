import unittest

from main import split_string_by_half, common_element, take_prio

class Test(unittest.TestCase):
    def test_split_string_by_half(self):
        input = "vJrwpWtwJgWrhcsFMMfFFhFp"
        expected = ["vJrwpWtwJgWr","hcsFMMfFFhFp"]
        out = split_string_by_half(input)
        self.assertEqual(expected, out)


    def test_common_element(self):
        str1 = "vJrwpWtwJgWr"
        str2 = "hcsFMMfFFhFp"
        expected = "p"
        out = common_element(str1, str2)
        self.assertEqual(expected, out)

    def test_common_element_three_elements(self):
        str1 = "vJrwpWtwJgWrhcsFMMfFFhFp"
        str2 = "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL"
        str3 = "PmmdzqPrVvPwwTWBwg"
        expected = "r"
        out = common_element(str1, str2, str3)
        self.assertEqual(expected, out)


    def test_take_prio(self):
        symbol = "p"
        out = take_prio(symbol)
        expected = 16
        self.assertEqual(expected, out)

if __name__ == '__main__':
    unittest.main()