import unittest
from hand import Hand


class Test_Hand_check_five_of_kind(unittest.TestCase):
    def test_check_five_of_kind_positive(self):
        cards = ["Q", "Q", "Q", "Q", "Q"]
        expected = True
        self.assertEqual(Hand.check_five_of_kind(cards), expected)

    def test_check_five_of_kind_negative(self):
        cards = ["Q", "A", "5", "Q", "Q"]
        expected = False
        self.assertEqual(Hand.check_five_of_kind(cards), expected)


class Test_Hand_check_four_of_kind(unittest.TestCase):
    def test_check_four_of_kind_positive(self):
        cards = ["Q", "Q", "Q", "Q", "A"]
        expected = True
        self.assertEqual(Hand.check_four_of_kind(cards), expected)

    def test_check_four_of_kind_negative(self):
        cards = ["Q", "A", "5", "Q", "Q"]
        expected = False
        self.assertEqual(Hand.check_four_of_kind(cards), expected)


class Test_Hand_check_full_house(unittest.TestCase):
    def test_check_full_house_positive(self):
        cards = ["A", "Q", "Q", "Q", "A"]
        expected = True
        self.assertEqual(Hand.check_full_house(cards), expected)

    def test_check_full_house_negative_three_of_kinds_and_two_different(self):
        cards = ["Q", "A", "5", "Q", "Q"]
        expected = False
        self.assertEqual(Hand.check_full_house(cards), expected)

    def test_check_full_house_negative_two_pairs(self):
        cards = ["Q", "A", "5", "A", "Q"]
        expected = False
        self.assertEqual(Hand.check_full_house(cards), expected)


class Test_Hand_check_three_of_kind(unittest.TestCase):
    def test_check_three_of_kind_positive(self):
        cards = ["Q", "Q", "Q", "K", "A"]
        expected = True
        self.assertEqual(Hand.check_three_of_kind(cards), expected)

    def test_check_three_of_kind_negative(self):
        cards = ["Q", "A", "5", "4", "3"]
        expected = False
        self.assertEqual(Hand.check_three_of_kind(cards), expected)


class Test_Hand_check_two_pair(unittest.TestCase):
    def test_check_three_of_kinds_positive(self):
        cards = ["Q", "A", "Q", "K", "A"]
        expected = True
        self.assertEqual(Hand.check_two_pair(cards), expected)

    def test_check_three_of_kinds_negative_one_pair(self):
        cards = ["Q", "4", "5", "4", "3"]
        expected = False
        self.assertEqual(Hand.check_two_pair(cards), expected)

    def test_check_three_of_kinds_negative_no_pairs(self):
        cards = ["Q", "2", "5", "4", "3"]
        expected = False
        self.assertEqual(Hand.check_two_pair(cards), expected)


class Test_Hand_check_one_pair(unittest.TestCase):
    def test_check_one_pair_positive(self):
        cards = ["Q", "Q", "2", "K", "A"]
        expected = True
        self.assertEqual(Hand.check_one_pair(cards), expected)

    def test_check_one_pair_negative(self):
        cards = ["Q", "A", "5", "4", "3"]
        expected = False
        self.assertEqual(Hand.check_one_pair(cards), expected)


class Test_Hand_calculate_hand_score(unittest.TestCase):
    def test_calculate_hand_score_high_card(self):
        cards = '32T4K'
        expected = 0
        h = Hand(cards, 0)
        self.assertEqual(h._score, expected)

    def test_calculate_hand_score_one_pair(self):
        cards = '32T3K'
        expected = 1
        h = Hand(cards, 0)
        self.assertEqual(h._score, expected)


    def test_calculate_hand_score_two_pair(self):
        cards = 'KK677'
        expected = 2
        h = Hand(cards, 0)
        self.assertEqual(h._score, expected)


    def test_calculate_hand_score_three_kind(self):
        cards = 'KKK87'
        expected = 3
        h = Hand(cards, 0)
        self.assertEqual(h._score, expected)

    def test_calculate_hand_score_full_house(self):
        cards = 'KKK77'
        expected = 4
        h = Hand(cards, 0)
        self.assertEqual(h._score, expected)

    def test_calculate_hand_score_four_kind(self):
        cards = 'KKKK7'
        expected = 5
        h = Hand(cards, 0)
        self.assertEqual(h._score, expected)

    def test_calculate_hand_score_five_kind(self):
        cards = 'KKKKK'
        expected = 6
        h = Hand(cards, 0)
        self.assertEqual(h._score, expected)
