from typing import List

from mapper import Mapper, MappingConf

def read_seeds(line: str) -> List[int]:
    return [int(el) for el in line.replace("seeds:", "").strip().split(" ")]

def read_map_name(line):
    return line.replace("map:", "").strip()

if __name__ == "__main__":
    mapps_dict_values = {}
    values = []
    name = None
    with open("input", "r") as f:
        file_splited = [l for l in f.read().split("\n\n") if l != '']
        seeds = file_splited[0]
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

    locs = []
    for s in seeds:
        soil = mapps_dict_mappings['seed-to-soil'].map(s)
        fertilizer = mapps_dict_mappings['soil-to-fertilizer'].map(soil)
        water = mapps_dict_mappings['fertilizer-to-water'].map(fertilizer)
        light = mapps_dict_mappings['water-to-light'].map(water)
        temperature = mapps_dict_mappings['light-to-temperature'].map(light)
        humidity = mapps_dict_mappings['temperature-to-humidity'].map(temperature)
        location = mapps_dict_mappings['humidity-to-location'].map(humidity)
        location.append(locs)
    print(min(locs))
