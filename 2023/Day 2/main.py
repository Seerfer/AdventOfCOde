from typing import List

from game import Game, Round

def create_cubes_dict(s: str) -> dict:
    result = {}
    for c in s.split(","):
        amount, colour = c.strip(" ").split(" ")
        result[colour] = int(amount)
    return result


def read_game_id_from_str(s: str) -> int:
    return int(s.split(":")[0].replace("Game ", ""))


def read_rounds_from_str(s: str) -> str:
    return s.split(":")[1].strip()


def split_rounds_str(s: str) -> List[str]:
    return [r.strip() for r in s.split(";")]


if __name__ == "__main__":
    valid_dict = {"red": 12, "green": 13, "blue": 14}
    games = []
    with open("input", "r") as f:
        while line := f.readline().strip():
            g = Game(read_game_id_from_str(line), valid_dict)
            for round_s in split_rounds_str(read_rounds_from_str(line)):
                c = create_cubes_dict(round_s)
                g.add_round(c)
            games.append(g)
    print(sum([g.id for g in games if g.validate_game()]))


