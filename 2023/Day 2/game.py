class Game:
    def __init__(self, id: int):
        self.id = id
        self.cubes = {}

    def add_cubes(self, colour: str, amount: int):
        if colour in (self.cubes.keys()):
            self.cubes[colour] += amount
        else:
            self.cubes[colour] = amount


    def return_cubes_amount(self, colour: str) -> int:
        return self.cubes[colour]


