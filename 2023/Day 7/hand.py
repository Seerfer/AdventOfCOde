class Hand:
    def __init__(self, hand: str):
        self.hand = list(hand)


    @staticmethod
    def check_five_of_kind(hand: list) -> bool:
        return all(i == hand[0] for i in hand)


    @staticmethod
    def check_four_of_kind(hand: list) -> bool:
        pass

    @staticmethod
    def check_full_house(hand: list) -> bool:
        pass

    @staticmethod
    def check_three_of_kind(hand: list) -> bool:
        pass

    @staticmethod
    def check_two_pair(hand: list) -> bool:
        pass

    @staticmethod
    def check_one_pair(hand: list) -> bool:
        pass