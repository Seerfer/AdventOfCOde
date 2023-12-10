import unittest

from mapper import Mapper, MappingConf
from main import read_seeds, read_map_name, split_list_to_chunks

class Test_Mapper_calculate_range_nums(unittest.TestCase):
    def test_Mapper_calculate_range_nums(self):
        range_start = 98
        len = 2
        expected = range(98, 100)
        output = Mapper.calculate_range_nums(range_start,len)
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
        array = range(0,5)
        value = 0
        expected = 0
        self.assertEqual(Mapper.find_el(array,value), expected)


    def test_Mapper_find_el_not_existing_in_array(self):
        array = range(0,3)
        value = 70
        expected = None
        self.assertEqual(Mapper.find_el(array, value), expected)


    def test_Mapper_find_el_list_of_ranges(self):
        array = [range(0,3), range(5,6)]
        value = range(5,6)
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
        l = [1,2,3,4,5,6]
        chunks_size = 2
        expected = [[1,2],[3,4],[5,6]]
        self.assertEqual(split_list_to_chunks(l, chunks_size), expected)

    def test_split_list_to_chunks_not_equal_chunks(self):
        l = [1,2,3,4,5]
        chunks_size = 2
        expected = [[1,2],[3,4],[5]]
        self.assertEqual(split_list_to_chunks(l, chunks_size), expected)

