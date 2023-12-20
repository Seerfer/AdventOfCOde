from hand import Hand

if __name__ == "__main__":
  hands = []
  with open("input", "r") as f:
    while line := f.readline().strip():
      cards, bid = line.split(" ")
      hands.append(Hand(cards, int(bid)))

  res1 = sum([i*h.bid for i,h in enumerate(sorted(hands), 1)])
  print(f"Result for part 1: {res1}")


