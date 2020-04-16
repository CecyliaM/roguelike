import util
import engine
import ui
'''--------------------Piotrek-----------------------------------------------------------------'''
import random 
inventory = {"Health": 100, "Power": 25, "Weapon": 0, "Keys": 0}
'''
$ is a key to unlock door
* is a weapon
! is health upgrade by 25%
'''
items = {"$":1, "*":1, "!":25}

'''--------------------Piotrek-----------------------------------------------------------------'''


PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3

BOARD_WIDTH = 30
BOARD_HEIGHT = 20



def create_player():
    player = {'PLAYER_ICON' : '@', 'PLAYER_X': 10, 'PLAYER_Y' : 10}
    return player

def main():
    player = create_player()
    board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
    
    util.clear_screen()

    is_running = True
    while is_running:
        engine.put_player_on_board(board, player)
        ui.display_board(board)
        key = util.key_pressed()
        if key == 'q':
            is_running = False
        
        # if key == 'I' or 'i': #Piotrek
        #     display_inventory(inventory, board)
        #     continue
        else:
            moving_ahead = list(moving(board, player))
            moving_ahead[0] = board
            playerX = moving_ahead[1] 
            playerY = moving_ahead[2] 
            player.update(PLAYER_X = playerX) 
            player.update(PLAYER_Y = playerY) 

            # util.clear_screen()

'''--------------------Piotrek-----------------------------------------------------------------'''


def display_inventory(inventory, board):
    line = ("-"*30)
    print(line)
    print("Player information:")
    for k, v in inventory.items():
        print(k, "|", v)
    print(line)
    items_append_on_board(items, board)
    

def random_item_row(board):
    return random.randint(0,len(board)-1)


def random_item_col(board):
    return random.randint(0, len(board[0])-1)


def place_is_aviable_for_item(board, coordinates):
    if board[coordinates[0]][coordinates[1]] == 'p':
        return True
    else:
        return False

        
def items_append_on_board(items, board):
    coordinates = [2,2]
    item_x_place = random_item_row(board)
    item_y_place = random_item_col(board) 
    print(random_item_row(board))
    print(random_item_col(board))
    print(board)
    print(board)
    while place_is_aviable_for_item(board, coordinates):
        board[[10][10]] =  "."
    else:
        print("nonono")
    print(board)
    return board


'''--------------------Piotrek-----------------------------------------------------------------'''


'''--------------------Cecylia-----------------------------------------------------------------'''
def moving(board, player):

    icon = player['PLAYER_ICON']
    player_start_X = player['PLAYER_X']
    player_start_Y = player['PLAYER_Y']
    board[player_start_X][player_start_Y] = icon
    # display_board()
    # for row in board:
    #     print(row)
    # for a in range(100): #this will be a while loop. for was just for tests - while is running w main()
    key = util.key_pressed()
    if key == "w": #up
        if not board[player_start_X -1][player_start_Y] == "w":
            board[player_start_X][player_start_Y] = "p"
            player_start_X -=1
            return board, player['PLAYER_X'], player['PLAYER_Y']
        else:
            print("invalid")
    if key == "s": #down
        if not board[player_start_X +1][player_start_Y] == "w":
            board[player_start_X][player_start_Y] = "p"
            player_start_X +=1
            return board, player['PLAYER_X'], player['PLAYER_Y']
        else:
            print("invalid")
    if key == "a": #left
        if not board[player_start_X][player_start_Y -1] == "w":
            board[player_start_X][player_start_Y] = "p"
            player_start_Y -=1
            return board, player['PLAYER_X'], player['PLAYER_Y']
        else:
            print("invalid")    
    if key == "d": #right
        if not board[player_start_X][player_start_Y+1] == "w":
            board[player_start_X][player_start_Y] = "p"
            player_start_Y +=1
            return board, player['PLAYER_X'], player['PLAYER_Y']
        else:
            print("invalid")
    #print(player_start_X,player_start_Y)
        # board[player_start_X][player_start_Y] = icon
        # print(player_start_X)
    # print(player['PLAYER_X'])
    # print(player['PLAYER_Y'])
    # return board, player['PLAYER_X'], player['PLAYER_Y']
    # os.system("clear")
    # display_board(board)
    # for row in board:
    #     print(row)

# moving(create_board(30,20))
'''-----------------------------------------Cecylia-------------------------------------'''

if __name__ == '__main__':
    
    main()
