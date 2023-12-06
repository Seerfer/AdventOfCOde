from board import Board


with open("input", "r") as f:
    data = [line.strip() for line in f]
    gr = []
    board = Board(len(data[0]), len(data))
    for x,line in enumerate(data):
        for y,v in enumerate(line):
            board.set_field_value(x,y,v)
            if v.isdigit():
                gr.append((x,y))
            elif (not v.isdigit()) and len(gr) != 0:
                board.add_group_num(gr)
                gr = []

    print(board.get_board_el(7,0))
    result = 0
    for group in board.groups:
        borders = board.get_group_borders(group)
        border_values = set(board.get_list_of_values(borders))
        print(f"{group.num}: {board.get_list_of_values(borders)}")
        # if len (border_values-set([str(el) for el in range(0,10)]+ ['.'])) != 0:
        #     result += group.num








