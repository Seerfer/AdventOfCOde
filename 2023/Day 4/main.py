from card import Card

with open("input", "r") as f:
    while line := f.readline().strip():
        striped_line = line.split(":")[1]
        winning_nums, card_nums = striped_line.split("|")
        winning_nums_transofmred = [int(num) for num in winning_nums.split(" ") if num.isdigit()]
        card_nums_transofmred = [int(num) for num in card_nums.split(" ") if num.isdigit()]
