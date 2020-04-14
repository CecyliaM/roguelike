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
    seq = 'wp'
    board = []
    row = []

    for ele in range(BOARD_HEIGHT):
        for i in range(BOARD_WIDTH):
            # if i == 0 or i == 29:
            #     row = (30*['w'])
            # else:
            row.append(random.choice(seq))
    board.append(row)
    return board

    # game_board = [list(30*'w'),\
    #             list(1*'w')+list(5*'p')+list(3*'w')+list(7*'p')+\
    #                 list(3*'p')+list(2*'w')+list(1*'p')+list(2*'w'),\
    #             list(1*'w')+list(1*'p')+list(2*'w')+list(8*'p')+list(2*'w')+\
    #                 list(4*'p')+list(3*'w')+list(4*'p')+list(2*'p')+list(2*'w'),\
    #             list(2*'w')+list(1*'p')+list(2*'w')+list(2*'p')+list(2*'w')\
    #                 +list(4*'p')+list(3*'w')+list(4*'p')+list(2*'p')+list(2*'w')]
    


def put_player_on_board(board, player):
    '''
    Modifies the game board by placing the player icon at its coordinates.

    Args:
    list: The game board
    dictionary: The player information containing the icon and coordinates

    Returns:
    Nothing
    '''
    pass
