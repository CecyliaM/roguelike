import engine

def display_board():
    '''
    Displays complete game board on the screen

    Returns:
    Nothing
    '''

    board = engine.create_board(30,20)
    color_scheme = {'p': '  ', 'w': '▓▓', 'g': '[|]'}

    for row in board:
        for cell in row: 
            print(color_scheme[cell], end='')
        print()


print(display_board())