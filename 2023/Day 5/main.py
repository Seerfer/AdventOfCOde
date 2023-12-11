from typing import List

from mapper import Mapper, MappingConf

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
    return (ranges[0].stop >= ranges[1].start)

def group_overlapping_ranges(ranges: List[range]) -> List[range]:
    result = []
    current_start = -1
    current_stop = -1
    sorted_ranges = sorted(ranges, key=lambda x:x.start)
    
    return result


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

    locs1 = []
    seeds1 = seeds
    for s in seeds:
        val = s
        for k,mapping in mapps_dict_mappings.items():
            val = mapping.map(val)
        locs1.append(val)

    print(f"Part 1 result = {min(locs1)}")
