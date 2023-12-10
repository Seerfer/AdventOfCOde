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
            self._mapping_list_source += self.calculate_range_nums(mapping.source_start, mapping.length)
            self._mapping_list_desc += self.calculate_range_nums(mapping.destination_start, mapping.length)


    @property
    def mapping_list_source(self):
        return self._mapping_list_source

    @property
    def mapping_list_desc(self):
        return self._mapping_list_desc


    @staticmethod
    def calculate_range_nums(start: int, length: int):
        return list(range(start, start+length))


    def map(self, source):
        index = self.find_el(self._mapping_list_source, source)
        if index is None:
            return source
        return self._mapping_list_desc[index]


    @staticmethod
    def find_el(array: list, value: int) -> Optional[int]:
        if value not in array:
            return None
        return array.index(value)