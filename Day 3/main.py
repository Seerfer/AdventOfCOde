import string
from typing import List
def creat_item_prio() -> dict:
    out = dict()
    alphabet_lower = list(string.ascii_lowercase)
    alphabet_upper = list(string.ascii_uppercase)
    alphabet = alphabet_lower + alphabet_upper
    for prio, letter in enumerate(alphabet, 1):
        out[letter] = prio
    return out

def split_string_by_half(input: str) -> List[str]:
    pass

if __name__ == '__main__':
    print(creat_item_prio())

