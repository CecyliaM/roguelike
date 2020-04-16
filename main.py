import util
import engine
import ui
import time
import os
'''--------------------Piotrek-----------------------------------------------------------------'''
import random 
inventory = {"Health": 15, "Weapon": 0, "Eggs": 0}
'''
$ is a key to unlock door
* is a weapon
! is health upgrade by 25%
'''
#items = {"$":1, "*":1, "!":25}

'''--------------------Piotrek-----------------------------------------------------------------'''
'''
story
< When life gives you eggs, make an omelette > 
Welcome, Eggbert!
You have been teleported to this creepy dungeon.
Your task is to collect enough eggs to make an omelette.
Be careful! You are going to encounter chickens that will try to stop you.
'''

PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3

BOARD_WIDTH = 30
BOARD_HEIGHT = 20



def create_player():
    player = {'PLAYER_ICON' : '@', 'PLAYER_X': 10, 'PLAYER_Y' : 10}
    return player


def random_position(board, BOARD_WIDTH, BOARD_HEIGHT):
    PLAYER_START_X = 0
    PLAYER_START_Y = 0
    while board[PLAYER_START_X][PLAYER_START_Y] != 'p':
        PLAYER_START_X = random.randint(1, BOARD_HEIGHT-1)
        PLAYER_START_Y = random.randint(1, BOARD_WIDTH-1)
    
    return PLAYER_START_X, PLAYER_START_Y

random_position(engine.create_board(BOARD_WIDTH, BOARD_HEIGHT), 30,20)

def main():
    player = create_player()
    board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)

    for i in range(8):
        item_place = list(random_position(board, BOARD_WIDTH, BOARD_HEIGHT))
        item_x = item_place[0]
        item_y = item_place[1]
        board[item_x][item_y] = "$"
    for i in range(2):
        weapon_place = list(random_position(board, BOARD_WIDTH, BOARD_HEIGHT))
        weapon_x = weapon_place[0]
        weapon_y = weapon_place[1]
        board[weapon_x][weapon_y] = "*"
    for i in range(5):
        health_place = list(random_position(board, BOARD_WIDTH, BOARD_HEIGHT))
        health_x = health_place[0]
        health_y = health_place[1]
        board[health_x][health_y] = "!"
    
    for i in range(4):
        monster_place = list(random_position(board, BOARD_WIDTH, BOARD_HEIGHT))
        monster_x = monster_place[0]
        monster_y = monster_place[1]
        board[monster_x][monster_y] = "m"

    position = list(random_position(board, BOARD_WIDTH, BOARD_HEIGHT))

    player_start_X = position[0]
    player_start_Y = position[1]
    
    is_running = True
    while is_running:
        board[player_start_X][player_start_Y] = "s"
        util.clear_screen()
        ui.display_board(board)
        key = util.key_pressed()
        if key == 'q':
            is_running = False
        if inventory['Eggs'] == 5:
            print("🍳 You have collected enough eggs to make an omelette! 🍳")
            print("You won!")
            break
        if key == 'i':
            display_inventory(inventory)
            os.system("""bash -c 'read -s -n 1 -p "Press any key to continue..."'""")
        if key == "w": #up
            if not board[player_start_X -1][player_start_Y] == "w":
                board[player_start_X][player_start_Y] = "p"
                player_start_X -=1
        if key == "s": #down
            if not board[player_start_X +1][player_start_Y] == "w":
                board[player_start_X][player_start_Y] = "p"
                player_start_X +=1
        if key == "a": #left
            if not board[player_start_X][player_start_Y -1] == "w":
                board[player_start_X][player_start_Y] = "p"
                player_start_Y -=1   
        if key == "d": #right
            if not board[player_start_X][player_start_Y+1] == "w":
                board[player_start_X][player_start_Y] = "p"
                player_start_Y +=1
        if board[player_start_X][player_start_Y] == "!":
            inventory['Health'] += 1
        if board[player_start_X][player_start_Y] == "*":
            inventory['Weapon'] += 1
        if board[player_start_X][player_start_Y] == "$":
            inventory['Eggs'] += 1
     #   if board[player_start_X][player_start_Y] == "m":
      #      print("The chicken attacks you! You lose 1 health point")
       #     inventory['Health'] -=1
        #    print("Press o to attack")
         #   time.sleep(2)
          #  print("You defeated the chicken!")
           # time.sleep(2)
            #else:
             #   print("You were defeated!")
              #  inventory['Health'] -=3
               # time.sleep(2)
        if inventory['Health'] == 0:
            print(inventory['Health'])
            print("You die!")
            break
        
        # if key == 'I' or 'i': #Piotrek
        #     display_inventory(inventory, board)
        #     continue

'''--------------------Piotrek-----------------------------------------------------------------'''


def display_inventory(inventory):
    line = ("-"*30)
    print(line)
    print("Player information:")
    for k, v in inventory.items():
        print(k, "|", v)
    print(line)

    

        


'''--------------------Piotrek-----------------------------------------------------------------'''


if __name__ == '__main__':
    
    main()