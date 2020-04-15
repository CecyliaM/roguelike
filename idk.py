from engine import create_board
from util import key_pressed
import os
from ui import display_board
player_icon = " @"

def board():
    board = []
    for a in range(10):
        board.append(["[]"]*10)
    board[3][3] = player_icon
    return board

def print_board(board):
    for row in board:
        print("".join(row))
    print("")

def player_on_board(board):
    board[player_start_X][player_start_Y] = player_icon
    print_board(board)


def moving(board):
    player_start_X = 3
    player_start_Y = 3
    board[player_start_X][player_start_Y] = player_icon
    display_board()
    for row in board:
        print(row)
    for a in range(100):
        key = key_pressed()
        if key == "w": #up
            if not board[player_start_X -1][player_start_Y] == "w":
                board[player_start_X][player_start_Y] = "p"
                player_start_X -=1
            else:
                print("invalid")
        if key == "s": #down
            if not board[player_start_X +1][player_start_Y] == "w":
                board[player_start_X][player_start_Y] = "p"
                player_start_X +=1
            else:
                print("invalid")
        if key == "a": #left
            if not board[player_start_X][player_start_Y -1] == "w":
                board[player_start_X][player_start_Y] = "p"
                player_start_Y -=1
            else:
                print("invalid")    
        if key == "d": #right
            if not board[player_start_X][player_start_Y+1] == "w":
                board[player_start_X][player_start_Y] = "p"
                player_start_Y +=1
            else:
                print("invalid")
        #print(player_start_X,player_start_Y)
        board[player_start_X][player_start_Y] = player_icon
        os.system("clear")
        display_board()
        for row in board:
            print(row)

moving(create_board(30,20))