def create_board(BOARD_WIDTH, BOARD_HEIGHT):
    board = []
    board.append(['w'] * BOARD_WIDTH)
    for i in range(BOARD_HEIGHT-2):
            board.append('w')
            board.append(['p']* BOARD_WIDTH)
            board.append('w')
    board.append(['w'] * BOARD_WIDTH)
    return board

#print(create_board(30,20))