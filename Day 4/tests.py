import unittest

from main import get_full_list_of_sections

class Test(unittest.TestCase):
    def test_get_full_list_of_sections(self):
        input = "2-4"
        expected = [2,3,4]
        out = get_full_list_of_sections(input)
        self.assertEqual(expected, out)



if __name__ == '__main__':
    unittest.main()