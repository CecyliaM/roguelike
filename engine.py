import random

def create_board(BOARD_WIDTH, BOARD_HEIGHT):
    '''
    Creates a new game board based on input parameters.
    Args:
    int: The width of the board
    int: The height of the board
    Returns:
    list: Game board
    '''
    board_material = ((BOARD_WIDTH)//3)*['w']+(((BOARD_WIDTH)//3)*2)*['p']
    board_material.remove('w')
    board_material.remove('p')
    line = []
    board = []
    line_with_border = []
<<<<<<< HEAD
=======

    passages = []
    no_escape_cell =[]


    while not len(passages) >= BOARD_HEIGHT * 10:
        for row in range(BOARD_HEIGHT):
            for cell in range(BOARD_WIDTH):
                if row == 0 or row == BOARD_HEIGHT-1:
                    line_with_border= 30*['w']
                else:
                    line = board_material.copy()
                    random.shuffle(line)
                    line_with_border = ['w']+line+['w']
            board.append(line_with_border)

        for row in range(1,(len(board)-1)):
            for cell in range(1,BOARD_WIDTH-1):
                if board[row][cell] == 'p' and board[-row][cell] == 'p':
                    passages.append(1)
                if board[row][cell] == 'p' and board[row][-cell] == 'w' and board[row][+cell] == 'w'\
                    and board[-row][cell] == 'w' and board[+row][cell] == 'w':
                    continue
    return board

    # board = [list(30*'w'),\
    #             list(1*'w')+list(5*'p')+list(3*'w')+list(7*'p')+\
    #                 list(3*'p')+list(2*'w')+list(1*'p')+list(2*'w'),\
    #             list(1*'w')+list(1*'p')+list(2*'w')+list(8*'p')+list(2*'w')+\
    #                 list(4*'p')+list(3*'w')+list(4*'p')+list(2*'p')+list(2*'w'),\
    #             list(2*'w')+list(1*'p')+list(2*'w')+list(2*'p')+list(2*'w')\
    #                 +list(4*'p')+list(3*'w')+list(4*'p')+list(2*'p')+list(2*'w')]
    # return board
>>>>>>> 4de052447fc6400b7cac4c77364a0a02833e378a

    passages = []
    no_escape_cell =[]


    while not len(passages) >= BOARD_HEIGHT * 10:
        for row in range(BOARD_HEIGHT):
            for cell in range(BOARD_WIDTH):
                if row == 0 or row == BOARD_HEIGHT-1:
                    line_with_border= 30*['w']
                else:
                    line = board_material.copy()
                    random.shuffle(line)
                    line_with_border = ['w']+line+['w']
            board.append(line_with_border)

        for row in range(1,(len(board)-1)):
            for cell in range(1,BOARD_WIDTH-1):
                if board[row][cell] == 'p' and board[-row][cell] == 'p':
                    passages.append(1)
                if board[row][cell] == 'p' and board[row][-cell] == 'w' and board[row][+cell] == 'w'\
                    and board[-row][cell] == 'w' and board[+row][cell] == 'w':
                    continue
    return board

    # board = [list(30*'w'),\
    #             list(1*'w')+list(5*'p')+list(3*'w')+list(7*'p')+\
    #                 list(3*'p')+list(2*'w')+list(1*'p')+list(2*'w'),\
    #             list(1*'w')+list(1*'p')+list(2*'w')+list(8*'p')+list(2*'w')+\
    #                 list(4*'p')+list(3*'w')+list(4*'p')+list(2*'p')+list(2*'w'),\
    #             list(2*'w')+list(1*'p')+list(2*'w')+list(2*'p')+list(2*'w')\
    #                 +list(4*'p')+list(3*'w')+list(4*'p')+list(2*'p')+list(2*'w')]
    # return board


def put_player_on_board(board, player):
    icon = player['PLAYER_ICON']
    x = player['PLAYER_X']
    y = player['PLAYER_Y']

    if board[x][y] == 'p':
        board[x][y] = icon
    else: 
        print("Wall error!!!")
    pass