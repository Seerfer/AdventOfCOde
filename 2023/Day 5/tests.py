import unittest

from mapper import Mapper, MappingConf

class Test_Mapper_calculate_range_nums(unittest.TestCase):
    def test_Mapper_calculate_range_nums(self):
        range_start = 98
        len = 2
        expected = [98,99]
        output = Mapper.calculate_range_nums(range_start,len)
        self.assertEqual(output, expected)


class Test_Mapper_init_mappings_lists(unittest.TestCase):
    def setUp(self):
        configs = [MappingConf(50, 98, 2), MappingConf(54, 100, 2)]
        self.m = Mapper(configs)
    def test_Mapper_init_mappings_list_sources(self):
        expected = [98, 99, 100, 101]
        self.assertEqual(self.m.mapping_list_source, expected)


    def test_Mapper_init_mappings_list_descs(self):
        expected = [50, 51, 54, 55]
        self.assertEqual(self.m.mapping_list_desc, expected)


class Test_Mapper_find_el(unittest.TestCase):
    def test_Mapper_find_el_existing_in_array(self):
        array = [0, 1, 2, 4]
        value = 0
        expected = 0
        self.assertEqual(Mapper.find_el(array,value), expected)


    def test_Mapper_find_el_not_existing_in_array(self):
        array = [0, 1, 2, 4]
        value = 70
        expected = None
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
