def take_next_n_el(collection: list, starting_index: int, n: int) -> list:
    if n < 0:
        raise ValueError("n must be positive")
    if starting_index < 0:
        raise ValueError("starting_index must be positive")
    if starting_index + n + 1 > len(collection):
        raise IndexError("Not enough element in the list to return")
    return collection[starting_index + 1 : starting_index + 1 + n]


def list_count_distinct(collection: list) -> int:
    return len(set(collection))


if __name__ == "__main__":
    result = 0
    with open("input", "r") as f:
        input_data = list(f.readline())

    n = 14
    for count, value in enumerate(input_data):
        n4 = take_next_n_el(input_data, count, n)
        if list_count_distinct(n4) == n:
            print(count + n + 1)  # add 1 because we need position that not count from 0
            break
