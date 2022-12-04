from typing import List

sums = list()

with open("input", "r") as f:
    sum_ = 0
    while line := f.readline():
        if line == "\n":
            sums.append(sum_)
            sum_ = 0
        else:
            sum_ += int(line)


def topn_total(list_: List[int], n: int) -> int:
    sorted_list = sorted(list_)
    sliced_list = sorted_list[-1*n:]
    print(sliced_list)
    return sum(sliced_list)


print(topn_total(sums, 3))
