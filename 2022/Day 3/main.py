import string
from typing import List
import math


def creat_item_prio() -> dict:
    out = dict()
    alphabet_lower = list(string.ascii_lowercase)
    alphabet_upper = list(string.ascii_uppercase)
    alphabet = alphabet_lower + alphabet_upper
    for prio, letter in enumerate(alphabet, 1):
        out[letter] = prio
    return out


def common_element(*args) -> str:
    sets = [set(el) for el in args]
    return "".join(sets[0].intersection(*sets[1:]))


def take_prio(symbol: str) -> int:
    prios = creat_item_prio()
    return prios.get(symbol, 0)


def split_string_by_half(input_str: str) -> List[str]:
    length = len(input_str)
    half_pos = math.floor(length / 2)
    return [input_str[:half_pos], input_str[half_pos:]]


if __name__ == "__main__":
    result = 0
    tmp = list()
    with open("input", "r") as f:
        while line := f.readline().strip():
            tmp.append(line)
            if len(tmp) == 3:
                common = common_element(tmp[0], tmp[1], tmp[2])
                prio = take_prio(common)
                result += prio
                tmp = []

    print(result)
