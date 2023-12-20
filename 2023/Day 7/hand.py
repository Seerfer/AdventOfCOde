from collections import Counter


class Hand:
    def __init__(self, hand: str, bid:int):
        self.bid = bid
        self.hand = list(hand)
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
            if func(self.hand):
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
