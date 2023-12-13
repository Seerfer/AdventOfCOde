from board import Board


with open("input", "r") as f:
    data = [line.strip() for line in f]
    gr = []
    gears_cords = []
    board = Board(len(data[0]), len(data))
    for y, line in enumerate(data):
        for x, v in enumerate(line):
            board.set_field_value(x, y, v)
            if v == "*":
                gears_cords.append((x, y))
            if v.isdigit():
                gr.append((x, y))
            elif (not v.isdigit()) and len(gr) != 0:
                board.add_group_num(gr)
                gr = []

    result1 = 0
    for group in board.groups:
        borders = board.get_group_borders(group)
        border_values = set(board.get_list_of_values(borders))
        if len(border_values - set([str(el) for el in range(0, 10)] + ["."])) != 0:
            result1 += group.num
    print(f"result part 1: {result1}")

    result2 = 0
    for gear_cord in gears_cords:
        neigh = board.find_neighbour_nums(gear_cord[0], gear_cord[1])
        if len(neigh) == 2:
            result2 += neigh[0] * neigh[1]
    print(f"result part 2: {result2}")
