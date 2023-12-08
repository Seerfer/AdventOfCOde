class Card:
    def __init__(self, card_nums, winning_nums):
        self.card_nums = card_nums
        self.winning_nums = winning_nums
        self.points = self._calculate_card_points()

    def _calculate_card_points(self):
        common_nums_count = len(list(set(self.card_nums).intersection(self.winning_nums)))
        if common_nums_count:
            return pow(2, common_nums_count - 1)
        else:
            return 0
