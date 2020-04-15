import engine


def display_board(board):
    # board = engine.create_board(30,20)
    
    color_scheme = {'p': '  ', 'w': '░░', 'g': '[|]', '@':'██'}
    for row in board:
        for cell in row: 
            print(color_scheme[cell], end='')
        print()
    print()

