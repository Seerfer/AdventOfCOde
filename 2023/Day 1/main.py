from typing import Optional

def find_first_digit(s: str) -> Optional[int]:
    for char in s:
        if char.isdigit():
            return int(char)
    return None


def find_last_digit(s: str) -> Optional[int]:
    s_reversed = s[::-1]
    for char in s_reversed:
        if char.isdigit():
            return int(char)
    return None


def create_number_from_digits(*args: str) -> int:
    s = ""
    for a in args:
        if a.isdigit():
            s = f"{s}{a}"
        else:
            raise ValueError(f"Value {a} is not a digit")
    return int(s)
