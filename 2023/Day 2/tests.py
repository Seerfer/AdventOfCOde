import unittest

from game import Game


class Test_game_add_cubes(unittest.TestCase):
    def test_game_add_cubes_init_cube(self):
        game = Game(1)
        game.add_cubes("red", 2)
        expected = 2
        self.assertEqual(expected, game.return_cubes_amount("red"))


    def test_game_add_cubes_add_to_existing_colour(self):
        game = Game(1)
        game.add_cubes("red", 2)
        game.add_cubes("red", 4)
        expected = 6
        self.assertEqual(expected, game.return_cubes_amount("red"))




if __name__ == "__main__":
    unittest.main()
