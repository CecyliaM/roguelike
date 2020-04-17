import engine

def display_board(board):
    '''
    Displays complete game board on the screen
    Returns:
    Nothing
    '''

    #board = engine.create_board(30,20)
    color_scheme = {'p': '  ', 'w': '⬛', 'g': '[|]', 's': '👲', '$': '🥚', '!': '💟',
     '*': '🔪', 'm': '🐥', '1': '🎅', '2': '🧙', '3': '🧟', 'boss': '🐣', 'door': '🚪',
      'shield': '🛡', '%': '🗝', 1: '⚪', 2: '⚫', 3: '⚫' }
    
    for row in board:
        for cell in row: 
            print(color_scheme[cell], end='')
        print()
    print()

def display_menu(items):
    for i in range(len(items)):
        print(items[i])


#🍗🔥⬜⬛🔲🗡💁‍♂️🧙👲⚫
