import engine

<<<<<<< HEAD

def display_board(board):
    # board = engine.create_board(30,20)
    
    color_scheme = {'p': '  ', 'w': '░░', 'g': '[|]', '@':'██'}
    for row in board:
        for cell in row: 
            print(color_scheme[cell], end='')
        print()
    print()

=======
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
>>>>>>> 4de052447fc6400b7cac4c77364a0a02833e378a
