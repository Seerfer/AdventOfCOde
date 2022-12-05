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

def common_element(str1: str, str2:str) -> List[str]:
    pass

def split_string_by_half(input: str) -> List[str]:
    lenght = len(input)
    half_pos = math.floor(lenght/2)
    return [input[:half_pos], input[half_pos:]]

if __name__ == '__main__':
    print(creat_item_prio())

