from card import Card

with open("input", "r") as f:
    cards = []
    while line := f.readline().strip():
        splited_line = line.split(":")
        id = int(splited_line[0].replace("Card", "").strip())
        winning_nums, card_nums = splited_line[1].split("|")
        winning_nums_transformed = [int(num) for num in winning_nums.split(" ") if num.isdigit()]
        card_nums_transformed = [int(num) for num in card_nums.split(" ") if num.isdigit()]
        card = Card(card_nums_transformed, winning_nums_transformed, id)
        cards.append(card)

    print(f"Result part 1: {sum([card.points for card in cards])}")


cards_deck_with_copies = []
for c in cards:
    print(c.common_nums_count)