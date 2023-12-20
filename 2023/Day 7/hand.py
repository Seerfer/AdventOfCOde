from collections import Counter
from functools import total_ordering

@total_ordering
class Hand:
    def __init__(self, cards: str, bid:int):
        if len(cards) != 5:
            raise ValueError(f"5 cards are required, {len(cards)} were provided")
        self.bid = bid
        self.cards = list(cards)
        self._score = self.calculate_calculate_score()

    def calculate_calculate_score(self):
        order = [
            self.check_five_of_kind,
            self.check_four_of_kind,
            self.check_full_house,
            self.check_three_of_kind,
            self.check_two_pair,
            self.check_one_pair
        ]
        i = 6
        for func in order:
            if func(self.cards):
                return i
            else:
                i -= 1
        return i

    @staticmethod
    def check_five_of_kind(hand: list) -> bool:
        return all(i == hand[0] for i in hand)

    @staticmethod
    def check_four_of_kind(hand: list) -> bool:
        counter = Counter(hand)
        return any(i >= 4 for i in counter.values())

    @staticmethod
    def check_full_house(hand: list) -> bool:
        counter = Counter(hand)
        return set(counter.values()) == {2, 3}

    @staticmethod
    def check_three_of_kind(hand: list) -> bool:
        counter = Counter(hand)
        return any(i >= 3 for i in counter.values())

    @staticmethod
    def check_two_pair(hand: list) -> bool:
        counter = Counter(hand)
        return sum([c for c in counter.values() if c>1]) >= 4

    @staticmethod
    def check_one_pair(hand: list) -> bool:
        counter = Counter(hand)
        return any(i >= 2 for i in counter.values())

    def __eq__(self, other):
        return self.cards == other.cards


    def __gt__(self, other):
        cards_vals = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
        if not self._score == other._score:
            return self._score > other._score
        else:
            for i in range(0,4):
                self_hc = self.cards[i]
                other_hc = other.cards[i]
                if self_hc != other_hc:
                    return cards_vals.index(self_hc) > cards_vals.index(other_hc)


    def __str__(self):
        return "".join(self.cards)


    def __repr__(self):
        return str(self)