import unittest

from game import Game, Round
from main import create_cubes_list, read_game_id_from_str, read_rounds_from_str, split_rounds_str

class Test_round_add_cubes(unittest.TestCase):

    def setUp(self):
        self.round = Round()

    def test_round_add_cubes_init_cube(self):
        self.round.add_cubes("red", 2)
        expected = 2
        self.assertEqual(expected, self.round.return_cubes_amount("red"))


    def test_round_add_cubes_add_to_existing_colour(self):
        self.round.add_cubes("red", 2)
        self.round.add_cubes("red", 4)
        expected = 6
        self.assertEqual(expected, self.round.return_cubes_amount("red"))


class Test_round_validate(unittest.TestCase):

    def setUp(self):
        self.round = Round()
        self.round.add_cubes("green", 20)
        self.round.add_cubes("red", 40)

    def test_round_validate_positive(self):
        valid = self.round.validate_round({"green": 100, "red": 100})
        expected = True
        self.assertEqual(expected, valid)


    def test_round_validate_one_negative(self):
        valid = self.round.validate_round({"green": 10, "red": 100})
        expected = False
        self.assertEqual(expected, valid)


    def test_round_validate_both_negative(self):
        valid = self.round.validate_round({"green": 20, "red": 40})
        expected = True
        self.assertEqual(expected, valid)


    def test_round_validate_postive_equal(self):
        valid = self.round.validate_round({"green": 10, "red": 10})
        expected = False
        self.assertEqual(expected, valid)


class Test_game_validate(unittest.TestCase):

    def setUp(self):
        self.game = Game(1)
        round1 = Round()
        round1.add_cubes("green", 20)
        round1.add_cubes("red", 40)
        self.game.add_round(round1)
        round2 = Round()
        round2.add_cubes("green", 2)
        round2.add_cubes("red", 4)
        self.game.add_round(round2)

    def test_game_validate_positive(self):
        valid = self.game.validate_game({"green": 100, "red": 100})
        expected = True
        self.assertEqual(expected, valid)


    def test_game_validate_one_negative(self):
        valid = self.game.validate_game({"green": 10, "red": 10})
        expected = False
        self.assertEqual(expected, valid)


    def test_game_validate_both_negative(self):
        valid = self.game.validate_game({"green": 1, "red": 1})
        expected = False
        self.assertEqual(expected, valid)

class Test_create_cubes_list(unittest.TestCase):
    def test_create_cubes_list(self):
        s = "3 blue, 4 red, 1 red, 2 green, 6 blue, 2 green"
        expected = [{"colour": "blue", "amount": 3},
                    {"colour": "red", "amount": 4},
                    {"colour": "red", "amount": 1},
                    {"colour": "green", "amount": 2},
                    {"colour": "blue", "amount": 6},
                    {"colour": "green", "amount": 2}]
        self.assertEqual(expected, create_cubes_list(s))


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



if __name__ == "__main__":
    unittest.main()
