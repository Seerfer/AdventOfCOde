import unittest

from mapper import Mapper, MappingConf
from main import (
    read_seeds,
    read_map_name,
    split_list_to_chunks,
    group_overlapping_ranges,
    is_overlapping,
    is_val_in_ranges,
)


class Test_Mapper_calculate_range_nums(unittest.TestCase):
    def test_Mapper_calculate_range_nums(self):
        range_start = 98
        len = 2
        expected = range(98, 100)
        output = Mapper.calculate_range_nums(range_start, len)
        self.assertEqual(output, expected)


class Test_Mapper_init_mappings_lists(unittest.TestCase):
    def setUp(self):
        configs = [MappingConf(50, 98, 2), MappingConf(54, 100, 2)]
        self.m = Mapper(configs)

    def test_Mapper_init_mappings_list_sources(self):
        expected = [range(98, 100), range(100, 102)]
        self.assertEqual(self.m.mapping_list_source, expected)

    def test_Mapper_init_mappings_list_descs(self):
        expected = [range(50, 52), range(54, 56)]
        self.assertEqual(self.m.mapping_list_desc, expected)


class Test_Mapper_find_el(unittest.TestCase):
    def test_Mapper_find_el_existing_in_array(self):
        array = range(0, 5)
        value = 0
        expected = 0
        self.assertEqual(Mapper.find_el(array, value), expected)

    def test_Mapper_find_el_not_existing_in_array(self):
        array = range(0, 3)
        value = 70
        expected = None
        self.assertEqual(Mapper.find_el(array, value), expected)

    def test_Mapper_find_el_list_of_ranges(self):
        array = [range(0, 3), range(5, 6)]
        value = range(5, 6)
        expected = 1
        self.assertEqual(Mapper.find_el(array, value), expected)


class Test_Mapper_map_elements(unittest.TestCase):
    def setUp(self):
        configs = [MappingConf(50, 98, 2), MappingConf(54, 100, 2)]
        self.m = Mapper(configs)

    def test_Mapper_map_element_existing(self):
        v = 98
        expected = 50
        self.assertEqual(self.m.map(v), expected)

    def test_Mapper_map_element_not_existing(self):
        v = 4
        expected = 4
        self.assertEqual(self.m.map(v), expected)


class Test_read_seed(unittest.TestCase):
    def test_read_seeds(self):
        l = "seeds: 92 46 24 21 37"
        expected = [92, 46, 24, 21, 37]
        self.assertEqual(read_seeds(l), expected)


class Test_read_map_name(unittest.TestCase):
    def test_read_map_name(self):
        l = "seed-to-soil map:"
        expected = "seed-to-soil"
        self.assertEqual(read_map_name(l), expected)


class Test_split_list_to_chunks(unittest.TestCase):
    def test_split_list_to_chunks_equal_chunks(self):
        l = [1, 2, 3, 4, 5, 6]
        chunks_size = 2
        expected = [[1, 2], [3, 4], [5, 6]]
        self.assertEqual(split_list_to_chunks(l, chunks_size), expected)

    def test_split_list_to_chunks_not_equal_chunks(self):
        l = [1, 2, 3, 4, 5]
        chunks_size = 2
        expected = [[1, 2], [3, 4], [5]]
        self.assertEqual(split_list_to_chunks(l, chunks_size), expected)


class Test_is_overlapping(unittest.TestCase):
    def test_is_overlapping_positive(self):
        input1 = range(1, 6)
        input2 = range(3, 8)
        expected = True
        self.assertEqual(expected, is_overlapping(input1, input2))

    def test_is_overlapping_negative(self):
        input1 = range(1, 6)
        input2 = range(9, 12)
        expected = False
        self.assertEqual(expected, is_overlapping(input1, input2))

    def test_is_overlapping_positive_one_in_another(self):
        input1 = range(1, 8)
        input2 = range(5, 7)
        expected = True
        self.assertEqual(expected, is_overlapping(input1, input2))

    def test_is_overlapping_positive_one_common_element(self):
        input1 = range(1, 12)
        input2 = range(12, 18)
        expected = True
        self.assertEqual(expected, is_overlapping(input1, input2))


class Test_group_overlapping_ranges(unittest.TestCase):
    def test_group_overlapping_ranges_non_overlapping(self):
        input = [range(1, 3), range(5, 7), range(10, 12)]
        expected = input
        self.assertEqual(expected, group_overlapping_ranges(input))

    def test_group_overlapping_ranges_all_overlapping(self):
        input = [range(1, 8), range(5, 7), range(7, 13)]
        expected = [range(1, 13)]
        self.assertEqual(expected, group_overlapping_ranges(input))

    def test_group_overlapping_ranges_not_all_overlapping(self):
        input = [range(1, 8), range(5, 7), range(7, 13), range(15, 16)]
        expected = [range(1, 13), range(15, 16)]
        self.assertEqual(expected, group_overlapping_ranges(input))

    def test_group_overlapping_ranges_one_range(self):
        input = [range(1, 8)]
        expected = input
        self.assertEqual(expected, group_overlapping_ranges(input))


class Test_is_val_in_ranges(unittest.TestCase):
    def test_is_val_in_ranges_positive(self):
        input = [range(1, 3), range(5, 7), range(10, 12)]
        val = 2
        expected = True
        self.assertEqual(expected, is_val_in_ranges(val, input))

    def test_is_val_in_ranges_negative(self):
        input = [range(1, 3), range(5, 7), range(10, 12)]
        val = 200
        expected = False
        self.assertEqual(expected, is_val_in_ranges(val, input))
