from typing import Optional
from math import inf


class Round:
    def __init__(self, cubes_dict, bag: Optional[dict] = None):
        self.cubes = {}
        self._bag = bag
        colours = ["red", "blue", "green"]
        for c in colours:
            self.cubes[c] = cubes_dict.get(c, 0)

    def return_cubes_amount(self, colour: str) -> int:
        return self.cubes.get(colour, 0)

    def validate_round(self):
        if self._bag:
            return all([self.return_cubes_amount(k) <= v for k, v in self._bag.items()])
        return True

    @property
    def bag(self):
        return self._bag

    @bag.setter
    def bag(self, value):
        self._bag = value

    def __str__(self):
        return str(self.cubes)

    def __repr__(self):
        return str(self)


class Game:
    def __init__(self, id: int, bag: Optional[dict] = None):
        self.id = id
        self.rounds = []
        self._bag = bag
        if bag is None:
            self._bag = {el: inf for el in ["red", "blue", "green"]}

    def add_round(self, round_dict: dict):
        self.rounds.append(Round(round_dict, self._bag))

    def highest_cube_score(self, colour):
        high = 0
        for r in self.rounds:
            k = r.return_cubes_amount(colour)
            if k > high:
                high = k
        return high

    def validate_game(self):
        if self._bag is None:
            return True
        return all([r.validate_round() for r in self.rounds])

    @property
    def bag(self):
        return self._bag

    @bag.setter
    def bag(self, value):
        self._bag = value
        for r in self.rounds:
            r.bag = value

    def __str__(self):
        rounds_str = ""
        for r in self.rounds:
            rounds_str = rounds_str + f" {str(r)} "
        return f"Gamed ID: {self.id} Rounds: " + rounds_str + " "

    def __repr__(self):
        return str(self)
