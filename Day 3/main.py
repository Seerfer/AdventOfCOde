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


def common_element(str1: str, str2: str) -> str:
    set1 = set(str1)
    set2 = set(str2)
    return ''.join(set(set1).intersection(set2))


def take_prio(symbol: str) -> int:
    prios = creat_item_prio()
    return prios.get(symbol, 0)


def split_string_by_half(input_str: str) -> List[str]:
    length = len(input_str)
    half_pos = math.floor(length / 2)
    return [input_str[:half_pos], input_str[half_pos:]]


if __name__ == '__main__':
    result = 0
    with open("input", "r") as f:
        while line:= f.readline():
            splited = split_string_by_half(line.strip())
            str1, str2 = splited[0], splited[1]
            common = common_element(str1, str2)
            prio = take_prio(common)
            result += prio
    print(result)
