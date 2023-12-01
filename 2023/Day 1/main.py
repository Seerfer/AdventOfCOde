from typing import Optional, List

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


def replace_sub_str(base_str: str, start_i: int, end_i: int, str_to_replace: str) -> str:
    if end_i > len(base_str)-1:
        raise ValueError("End index out of range")
    return base_str[:start_i]+str_to_replace+base_str[end_i+1:]


def find_first_value(s: str, values: List[str]) -> Optional[str]:
    appearance = []
    for v in values:
        i = s.find(v)
        if i != -1:
            appearance.append((i, v))
    appearance.sort(key=lambda a: a[0])
    if len(appearance):
        return appearance[0][1]
    else:
        return None


def find_last_value(s: str, values: List[str]) -> Optional[str]:
    appearance = []
    for v in values:
        i = s.rfind(v)
        if i != -1:
            appearance.append((i, v))
    appearance.sort(key=lambda a: a[0])
    if len(appearance):
        return appearance[-1][1]
    else:
        return None

def rreplace(s, old, new, occurrence):
    li = s.rsplit(old, occurrence)
    return new.join(li)


def replace_first_and_last_spelled_num_with_dig(s: str) -> str:
    replace_dic = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }
    values = list(replace_dic.keys())

    value_to_replace = find_first_value(s, values)
    if value_to_replace is not None:
        s = s.replace(value_to_replace, str(replace_dic[value_to_replace]), 1)

    value_to_replace = find_last_value(s, values)
    if value_to_replace is not None:
        s = rreplace(s, value_to_replace, str(replace_dic[value_to_replace]), 1)

    return s


if __name__ == "__main__":
    nums = []
    with open("input", "r") as f:
        while line := f.readline().strip():
            line_converted = replace_first_and_last_spelled_num_with_dig(line)
            first_dig = find_first_digit(line_converted)
            last_dig = find_last_digit(line_converted)
            num = create_number_from_digits(str(first_dig), str(last_dig))
            nums.append(num)
    print(sum(nums))

