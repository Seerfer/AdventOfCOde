from board import Board, FieldGroupNum

#TODO: Reverse x,y in board

with open("input", "r") as f:
    data = [line.strip() for line in f]
    gr = []
    board = Board(len(data[0]), len(data))
    for x,line in enumerate(data):
        for y,v in enumerate(line):
            board.set_field_value(x,y,v)
            if v.isdigit():
                gr.append((x,y))
                print(gr)
            elif not v.isdigit() and len(gr) != 0:
                board.add_group_num(gr)


    print(board.groups)



