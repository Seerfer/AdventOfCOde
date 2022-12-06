from typing import List

def get_full_list_of_sections(given_range: str) -> List[int]:
    splited = given_range.split("-")
    start, end = int(splited[0]), int(splited[1])
    return list(range(start, end+1))

def check_if_contains(list1: list, list2: list) -> bool:
    set1, set2 = set(list1), set(list2)
    return set1.union(set2) == set1 or set2.union(set1) == set2