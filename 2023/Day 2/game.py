from typing import Optional
from math import inf

class Round:
    def __init__(self):
        self.cubes = {el:0 for el in ["red", "blue", "green"]}

    def add_cubes(self, colour: str, amount: int):
        if colour in (self.cubes.keys()):
            self.cubes[colour] += amount
        else:
            raise ValueError("Incorrect colour given ")


    def return_cubes_amount(self, colour: str) -> int:
        return self.cubes.get(colour, 0)


    def validate_round(self, max_values: dict):
        return all([self.return_cubes_amount(k)<=v for k,v in max_values.items()])


    def __str__(self):
        return str(self.cubes)


    def __repr__(self):
        return str(self)


class Game:
    def __init__(self, id: int, bag: Optional[dict] = None):
        self.id = id
        self.rounds = []
        self.bag = bag
        if bag is None:
            self.bag = {el: inf for el in ["red", "blue", "green"]}


    def add_round(self, round: Round):
        self.rounds.append(round)


    def validate_game(self):
        if self.bag is None:
            return None
        return all([r.validate_round(self.bag) for r in self.rounds])


    def __str__(self):
        rounds_str = ""
        for r in self.rounds:
            rounds_str = rounds_str + f" {str(r)} "
        return f"Gamed ID: {self.id} Rounds: " + rounds_str + " "


    def __repr__(self):
        return str(self)






