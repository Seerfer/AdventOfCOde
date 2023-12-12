from typing import List, Optional

from dataclasses import dataclass


@dataclass
class MappingConf:
    destination_start: int
    source_start: int
    length: int


class Mapper:
    def __init__(self, mappings: List[MappingConf]):
        self._mapping_list_source = []
        self._mapping_list_desc = []
        for mapping in mappings:
            self._mapping_list_source.append(self.calculate_range_nums(mapping.source_start, mapping.length))
            self._mapping_list_desc.append(self.calculate_range_nums(mapping.destination_start, mapping.length))

    @property
    def mapping_list_source(self):
        return self._mapping_list_source

    @property
    def mapping_list_desc(self):
        return self._mapping_list_desc

    @staticmethod
    def calculate_range_nums(start: int, length: int):
        return range(start, start + length)

    def map(self, source):
        ranges = [source in r for r in self._mapping_list_source]
        if any(ranges):
            r_index = ranges.index(True)
            v_index = self.find_el(self._mapping_list_source[r_index], source)
            return self._mapping_list_desc[r_index][v_index]
        else:
            return source


    def map_reverse(self, desc):
        ranges = [desc in r for r in self._mapping_list_desc]
        if any(ranges):
            r_index = ranges.index(True)
            v_index = self.find_el(self._mapping_list_desc[r_index], desc)
            return self._mapping_list_source[r_index][v_index]
        else:
            return desc

    @staticmethod
    def find_el(array, value) -> Optional[int]:
        if value not in array:
            return None
        return array.index(value)



