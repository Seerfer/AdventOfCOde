from typing import List

def get_full_list_of_sections(given_range: str) -> List[int]:
    splited = given_range.split("-")
    start, end = int(splited[0]), int(splited[1])
    return list(range(start, end+1))

def check_if_contains(list1: list, list2: list) -> bool:
    set1, set2 = set(list1), set(list2)
    return set1.union(set2) == set1 or set2.union(set1) == set2

def check_if_overlap_exists(list1: list, list2: list) -> bool:
    set1, set2 = set(list1), set(list2)
    return bool(set1 & set2)


if __name__ == '__main__':
    result = 0
    with open("input", "r") as f:
        while line := f.readline().strip():
            splited = line.split(",")
            range1, range2 = splited[0], splited[1]
            section1 = get_full_list_of_sections(range1)
            section2 = get_full_list_of_sections(range2)
            if check_if_contains(section1, section2):
                result += 1
    print(result)
