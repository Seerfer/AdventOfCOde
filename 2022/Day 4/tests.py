import unittest

from main import get_full_list_of_sections, check_if_contains, check_if_overlap_exists


class Test(unittest.TestCase):
    def test_get_full_list_of_sections(self):
        input = "2-4"
        expected = [2, 3, 4]
        out = get_full_list_of_sections(input)
        self.assertEqual(expected, out)

    def test_check_if_contains_true(self):
        list1 = [6]
        list2 = [4, 5, 6]
        expected = True
        out = check_if_contains(list1, list2)
        self.assertEqual(expected, out)

    def test_check_if_contains_false(self):
        list1 = [2, 3]
        list2 = [4, 5]
        expected = False
        out = check_if_contains(list1, list2)
        self.assertEqual(expected, out)

    def test_check_if_overlap_exists_true(self):
        list1 = [5, 6, 7]
        list2 = [7, 8, 9]
        expected = True
        out = check_if_overlap_exists(list1, list2)
        self.assertEqual(expected, out)

    def test_check_if_overlap_exists_false(self):
        list1 = [2, 3, 4]
        list2 = [6, 7, 8]
        expected = False
        out = check_if_overlap_exists(list1, list2)
        self.assertEqual(expected, out)


if __name__ == "__main__":
    unittest.main()
