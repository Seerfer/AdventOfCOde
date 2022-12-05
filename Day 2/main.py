from typing import List


def translate_to_shape(symbol: str) -> str:
    translation = {"X": "r", "Y": "p", "Z": "s",
                   "A": "r", "B": "p", "C": "s",
                   "r": "r", "p": "p", "s": "s"}
    return translation.get(symbol)


def translate_to_result(symbol: str) -> str:
    translation = {"X": "l", "Y": "d", "Z": "w"}
    return translation.get(symbol)


def calculate_shape_points(shape: str) -> int:
    shape_points = {"r": 1, "p": 2, "s": 3}
    return shape_points.get(shape)


def get_result(choose_player1: str, choose_player2: str) -> str:
    if choose_player1 == choose_player2:
        return "d"
    winners_dict = {"r": "s", "p": "r", "s": "p"}
    if choose_player1 == winners_dict.get(choose_player2):
        return "pl2"
    else:
        return "pl1"


def read_startegies(filename: str) -> List[str]:
    with open(filename, "r") as f:
        strategies = list()
        while line := f.readline():
            strategies.append(line.strip())
    return strategies


def calculate_round(chs1: str, chs2: str) -> dict:
    points = {"pl1": 0, "pl2": 0}
    pl1 = translate_to_shape(chs1)
    pl2 = translate_to_shape(chs2)
    points["pl1"] += calculate_shape_points(pl1)
    points["pl2"] += calculate_shape_points(pl2)
    result = get_result(pl1, pl2)
    if result == "d":
        points["pl1"] += 3
        points["pl2"] += 3
    else:
        points[result] += 6

    return points


def choose_shape(result: str, oponent_shape: str) -> str:
    result_dict = {
        "w": {"r": "p", "p": "s", "s": "r"},
        "d": {"r": "r", "p": "p", "s": "s"},
        "l": {"r": "s", "p": "r", "s": "p"}
    }

    return result_dict.get(result).get(oponent_shape)


strategies = read_startegies("input")
my_points = 0
for strategy in strategies:
    splited = strategy.split()
    result = translate_to_result(splited[1])
    oponent_shape = translate_to_shape(splited[0])
    my_shape = choose_shape(result, oponent_shape)
    result = calculate_round(my_shape, oponent_shape)
    my_points += result["pl1"]

print(my_points)
