import random

def menu_init():
    items = ["CLASSES:","🎅 Santa", "🧙‍♂Wizard", "🧟Zombie"]
    return items

def create_board(BOARD_WIDTH, BOARD_HEIGHT):
    '''
    Creates a new game board based on input parameters.
    Args:
    int: The width of the board
    int: The height of the board
    Returns:
    list: Game board
    '''
    board_material = (((BOARD_WIDTH)//10)*2)*['w']+(((BOARD_WIDTH)//10)*8)*['p']
    board_material.remove('w')
    board_material.remove('p')
    line = []
    board = []
    line_with_border = []

    passages = []
    no_escape_cell =[]

    while not len(passages) >= BOARD_HEIGHT * 10 or len(no_escape_cell) != 0:
        passages = []
        no_escape_cell =[]
        line = []
        board = []
        line_with_border = []
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
                if board[row][cell] == 'p' and board[row-1][cell] == 'p':
                    passages.append(1)
                if board[row][cell] == 'p' and board[row][cell-1] == 'w' and board[row][cell+1] == 'w'\
                    and board[row-1][cell] == 'w' and board[row+1][cell] == 'w':
                    no_escape_cell.append(1)
        
    return board

    # board = [list(30*'w'),\
    #             list(1*'w')+list(5*'p')+list(3*'w')+list(7*'p')+\
    #                 list(3*'p')+list(2*'w')+list(1*'p')+list(2*'w'),\
    #             list(1*'w')+list(1*'p')+list(2*'w')+list(8*'p')+list(2*'w')+\
    #                 list(4*'p')+list(3*'w')+list(4*'p')+list(2*'p')+list(2*'w'),\
    #             list(2*'w')+list(1*'p')+list(2*'w')+list(2*'p')+list(2*'w')\
    #                 +list(4*'p')+list(3*'w')+list(4*'p')+list(2*'p')+list(2*'w')]
    # return board

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