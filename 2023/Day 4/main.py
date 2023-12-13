from card import Card

with open("input", "r") as f:
    cards = []
    while line := f.readline().strip():
        splited_line = line.split(":")
        id = int(splited_line[0].replace("Card", "").strip())
        winning_nums, card_nums = splited_line[1].split("|")
        winning_nums_transformed = [
            int(num) for num in winning_nums.split(" ") if num.isdigit()
        ]
        card_nums_transformed = [
            int(num) for num in card_nums.split(" ") if num.isdigit()
        ]
        card = Card(card_nums_transformed, winning_nums_transformed, id)
        cards.append(card)

print(f"Result part 1: {sum([card.points for card in cards])}")


max_id = max([c.id for c in cards])
cards_ids_with_copies = [c.id for c in cards]
for id_to_process in range(1, max_id + 1):
    cards_num_to_process = cards_ids_with_copies.count(id_to_process)
    cards_won = list(
        range(
            id_to_process + 1,
            1 + id_to_process + cards[id_to_process - 1].common_nums_count,
        )
    )
    for c in range(cards_num_to_process):
        cards_ids_with_copies += cards_won


print(f"Result part 2: {len(cards_ids_with_copies)}")
