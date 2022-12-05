import unittest

from main import split_string_by_half, common_element

class Test(unittest.TestCase):
    def test_split_string_by_half(self):
        input = "vJrwpWtwJgWrhcsFMMfFFhFp"
        expected = ["vJrwpWtwJgWr","hcsFMMfFFhFp"]
        out = split_string_by_half(input)
        self.assertEqual(expected, out)


    def test_common_element(self):
        str1 = "vJrwpWtwJgWr"
        str2 = "hcsFMMfFFhFp"
        expeted = "p"
        out = common_element(str1, str2)
        self.assertEqual(expeted, out)




if __name__ == '__main__':
    unittest.main()