from typing import Optional, List


def create_number_from_digits(*args: str) -> int:
    s = ""
    for a in args:
        if a.isdigit():
            s = f"{s}{a}"
        else:
            raise ValueError(f"Value {a} is not a digit")
    return int(s)


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

def transform_to_digit(s: str) -> Optional[str]:
    digits_dict = {
        "one":'1', "two":'2', "three":'3', "four":'4', "five":'5', "six":'6', "seven":'7', "eight":'8', "nine":'9'
    }
    return digits_dict.get(s, None)

if __name__ == "__main__":
    nums = []
    values_to_find_part1 = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    values_to_find_part2 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    with open("input", "r") as f:
        while line := f.readline().strip():
            first_dig = find_first_value(line, values_to_find_part2)
            if not first_dig.isdigit():
                first_dig=transform_to_digit(first_dig)
            last_dig = find_last_value(line, values_to_find_part2)
            if not last_dig.isdigit():
                last_dig=transform_to_digit(last_dig)
            num = create_number_from_digits(str(first_dig), str(last_dig))
            nums.append(num)
    print(sum(nums))

