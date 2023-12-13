import unittest

from card import Card


class Test_Card_calculate_points(unittest.TestCase):
    def test_Card_no_points(self):
        winning_nums = [1, 2, 4]
        card_nums = [5, 6, 78, 9]
        card = Card(card_nums, winning_nums)
        self.assertEqual(card.points, 0)

    def test_Card_eight_points(self):
        winning_nums = [41, 48, 83, 86, 17]
        card_nums = [83, 86, 6, 31, 17, 9, 48, 53]
        card = Card(card_nums, winning_nums)
        self.assertEqual(card.points, 8)

    def test_Card_one_point(self):
        winning_nums = [41, 92, 73, 84, 69]
        card_nums = [59, 84, 76, 51, 58, 5, 54, 83]
        card = Card(card_nums, winning_nums)
        self.assertEqual(card.points, 1)
