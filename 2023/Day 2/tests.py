import unittest

from game import Game, Round
from main import create_cubes_dict, read_game_id_from_str, read_rounds_from_str, split_rounds_str


class Test_round_validate(unittest.TestCase):

    def setUp(self):
        self.round = Round({"green": 20, "red": 40})

    def test_round_validate_positive(self):
        self.round.bag = {"green": 100, "red": 100}
        valid = self.round.validate_round()
        expected = True
        self.assertEqual(expected, valid)


    def test_round_validate_one_negative(self):
        self.round.bag = {"green": 10, "red": 100}
        valid = self.round.validate_round()
        expected = False
        self.assertEqual(expected, valid)


    def test_round_validate_both_negative(self):
        self.round.bag = {"green": 20, "red": 40}
        valid = self.round.validate_round()
        expected = True
        self.assertEqual(expected, valid)


    def test_round_validate_postive_equal(self):
        self.round.bag = {"green": 10, "red": 10}
        valid = self.round.validate_round()
        expected = False
        self.assertEqual(expected, valid)


class Test_game_validate(unittest.TestCase):

    def setUp(self):
        self.game = Game(1)
        self.game.add_round({"green": 20, "red": 40})
        self.game.add_round({"green": 2, "red": 4})

    def test_game_validate_positive(self):
        self.game.bag={"green": 100, "red": 100}
        valid = self.game.validate_game()
        expected = True
        self.assertEqual(expected, valid)


    def test_game_validate_one_negative(self):
        self.game.bag = {"green": 10, "red": 10}
        valid = self.game.validate_game()
        expected = False
        self.assertEqual(expected, valid)


    def test_game_validate_both_negative(self):
        self.game.bag = {"green": 1, "red": 1}
        valid = self.game.validate_game()
        expected = False
        self.assertEqual(expected, valid)

class Test_create_cubes_dict(unittest.TestCase):
    def test_create_cubes_dict(self):
        s = "3 blue, 4 red, 2 green"
        expected = {"blue": 3, "red": 4, "green": 2}
        self.assertEqual(expected, create_cubes_dict(s))


class Test_read_game_id_from_str(unittest.TestCase):
    def test_read_game_id_from_str(self):
        s = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
        expected = 1
        self.assertEqual(expected, read_game_id_from_str(s))


class Test_read_rounds_from_str(unittest.TestCase):
    def test_read_rounds_from_str(self):
        s = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
        expected = "3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
        self.assertEqual(expected, read_rounds_from_str(s))


class Test_split_rounds_str(unittest.TestCase):
    def test_read_rounds_from_str_multiple_rounds(self):
        s = "3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
        expected = ["3 blue, 4 red", "1 red, 2 green, 6 blue", "2 green"]
        self.assertEqual(expected, split_rounds_str(s))

    def test_read_rounds_from_str_one_round(self):
        s = "3 blue, 4 red"
        expected = ["3 blue, 4 red"]
        self.assertEqual(expected, split_rounds_str(s))


class Test_highest_cube_score(unittest.TestCase):
    def setUp(self):
        game = Game(1)
        game.add_round({"blue": 1, "red": 20})
        game.add_round({"blue": 4, "red": 8})
        self.game = game
    def test_highest_cube_score(self):
        input_expected = [("blue", 4), ("red", 20)]
        for input, expected in input_expected:
            self.assertEqual(expected, self.game.highest_cube_score(input))

    def test_highest_cube_score_zero_score(self):
        self.assertEqual(0, self.game.highest_cube_score("green"))



if __name__ == "__main__":
    unittest.main()
