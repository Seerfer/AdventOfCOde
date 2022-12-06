from typing import List
def get_full_list_of_sections(given_range: str) -> List[int]:
    splited = given_range.split("-")
    start, end = int(splited[0]), int(splited[1])
    return list(range(start, end+1))