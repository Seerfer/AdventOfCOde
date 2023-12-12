from typing import List
import math

from mapper import Mapper, MappingConf


def is_val_in_ranges(val: int, ranges: List[range]) -> bool:
    conds = [val in r for r in ranges]
    return any(conds)

def read_seeds(line: str) -> List[int]:
    return [int(el) for el in line.replace("seeds:", "").strip().split(" ")]

def read_map_name(line):
    return line.replace("map:", "").strip()

def split_list_to_chunks(array, chunk_size)->list:
    chunks = []
    for i in range(0, len(array), chunk_size):
        chunks.append(array[i:i + chunk_size])
    return chunks

def is_overlapping(r1: range, r2: range) -> bool:
    ranges = sorted([r1, r2], key=lambda x:x.start)
    return ranges[0].stop >= ranges[1].start

def group_overlapping_ranges(ranges: List[range]) -> List[range]:
    result = []
    sorted_ranges = sorted(ranges, key=lambda x:x.start)
    current_range = sorted_ranges.pop(0)
    while len(sorted_ranges) > 0:
        r = sorted_ranges.pop(0)
        if is_overlapping(current_range, r):
            current_range = range(min([current_range.start, r.start]), max([current_range.stop, r.stop]))
        else:
            result.append(current_range)
            current_range = r
    result.append(current_range)
    return sorted(result, key=lambda x:x.start)


if __name__ == "__main__":
    mapps_dict_values = {}
    with open("input", "r") as f:
        file_splited = [l for l in f.read().split("\n\n") if l != '']
        seeds = read_seeds(file_splited[0])
        for mapping in file_splited[1:]:
            splited_mapping = mapping.split("\n")
            name = read_map_name(splited_mapping[0])
            mapps_dict_values[name] = splited_mapping[1:]

    mapps_dict_mappings = {}
    for key,values in mapps_dict_values.items():
        mapp_confs = []
        for v in values:
            splited_values = [int(el) for el in v.split(" ")]
            mapp_confs.append(MappingConf(*splited_values))
            mapps_dict_mappings[key] = Mapper(mapp_confs)

    seeds1 = seeds
    min_val = math.inf
    for s in seeds1:
        val = s
        for k, mapping in mapps_dict_mappings.items():
            val = mapping.map(val)
        if val < min_val:
            min_val = val
    print(f"Part 1 result = {min_val}")

    seeds2_chunks = split_list_to_chunks(seeds, 2)
    seeds2_not_grouped = []
    for s in seeds2_chunks:
        seeds2_not_grouped.append(range(s[0], s[0] + s[1]))
    seeds2 = group_overlapping_ranges(seeds2_not_grouped)
    min_val = math.inf
    possible_locs = mapps_dict_mappings['humidity-to-location'].mapping_list_desc
    for lr in possible_locs:
        for l in lr:
            val = l
            for k,mapping in reversed(mapps_dict_mappings.items()):
                val = mapping.map(val)
            if l < min_val and is_val_in_ranges(val, seeds2):
                min_val = l
    print(f"Part 2 result = {min_val}")


