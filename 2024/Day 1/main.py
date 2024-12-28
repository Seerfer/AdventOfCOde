

if __name__ == "__main__":
  l1, l2 = [], []
  diff = 0
  sim = 0
  with open("input", "r") as f:
    while line := f.readline().strip():
      el1, el2 = line.split("   ")
      l1.append(el1)
      l2.append(el2)
  l1s = sorted(l1)
  l2s = sorted(l2)
  for i, id1 in enumerate(l1s):
    diff += abs(int(id1)-int(l2s[i]))
  print(f"Part 1: {diff}")

  for id1 in l1:
    sim += int(id1)*l2.count(id1)
  print(f"Part 2: {sim}")
