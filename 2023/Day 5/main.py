from typing import List

from mapper import Mapper, MappingConf

def read_seeds(line: str) -> List[int]:
    return [int(el) for el in line.replace("seeds:", "").strip().split(" ")]

def read_map_name(line):
    return line.replace("map:", "").strip()

if __name__ == "__main__":
    mapps_dict_values = {}
    with open("input", "r") as f:
        cards = []
        file_splited = [l for l in f.read().split("\n") if l != '']
        values = []
        name = None
        for line in file_splited:
            if line.startswith("seeds"):
                seeds = read_seeds(line)
            elif line.endswith("map:"):
                if name:
                    mapps_dict_values[name] = values
                    values = []
                name = read_map_name(line)
            else:
                values.append(line)

    mapps_dict_mappings = {}
    for key,values in mapps_dict_values.items():
        mapp_confs = []
        for v in values:
            splited_values = [int(el) for el in v.split(" ")]
            mapp_confs.append(MappingConf(*splited_values))
            mapps_dict_mappings[key] = Mapper(mapp_confs)


