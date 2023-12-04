from board import Board, FieldGroupNum


with open("input", "r") as f:
    data = [line.strip() for line in f]
    board = Board(len(data[0]), len(data))
    for x,line in enumerate(data):
        for y,v in enumerate(line):
            board.set_field_value(x,y,v)

    board.print_board()