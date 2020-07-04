"""
Tic-Tac Toe
--------------------------------------------------
Created on Tue Jun 30 17:38:56 2020
"""

import random

board = [i for i in range(0, 9)]

# Initialize player and computer
player, computer = '',''

## Define moves
## Visualize board as:
# 1 # 2 # 3
# 4 # 5 # 6
# 7 # 8 # 9

# corners, center, and remaining locations
moves = ( (1, 3, 7, 9), (5,), (2, 4, 6, 9) )

## Winning combinations
# indices of the board positions 

winning_combinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2,5,8),(0,4,8),(2,4,6) )

# Table
tab = range(1, 10)


## Display board in CUI
def display_board():
    position = 1
    
    for i in board:
        end = ' | '             # vertical bar after each space
        if position % 3 == 0:
            end = ' \n'         # change row after three spaces
            if i != 1: 
                end += '---------\n' # add horizontal bar between rows
        
        char = ' '               # empty if the space isn't used yet 
        if i in ('X', 'O' ): 
            char = i            # if space is filled, use respective character
        
        print(char, end = end)     
        position += 1           # next position
            

def select_character():
    chars = ('X', 'O')
    
    # generate character sequence at random
    if random.randint(0, 1) == 0:
        return chars[::-1]
    return chars


def can_move(brd, player, move):
    if move in tab and brd[move - 1] == move - 1:
        return True
    return False


# test if the player can win
def can_win(brd, player, move):
    places = []
    x = 0
    
    for i in brd:
        if i == player:
            places.append(x)
        x += 1
    win = True
    
    for tup in winning_combinations:
        win = True
        for ix in tup:
            if brd[ix] != player:
                win = False
                break
        if win == True:
            break
    return win


# make move for the current board situation and given player
def make_move(brd, player, move, undo=False):
    if can_move(brd, player, move):
        brd[move - 1] = player
        win = can_win(brd, player, move)
        
        if undo:
            brd[move - 1] = move - 1
        return (True, win)
    
    return (False, False)


# select computer's move
def computer_move():
    move = -1
    # If computer can win, player doesn't matter.
    # Brute force
    for i in range(1,10):
        if make_move(board, computer, i, True)[1]:
            move = i
            break

    if move == -1:
        # If player can win, block the player's winning place.
        for i in range(1,10):
            if make_move(board, player, i, True)[1]:
                move = i
                break
            
    if move == -1:
        # Otherwise, try to take a favorable place.
        for j in moves:
            for mv in j:
                if move == -1 and can_move(board, computer, mv):
                    move = mv
                    break
    return make_move(board, computer, move)


# test if the board is full or not
def space_exist():
    return board.count('X') + board.count('O') != 9


# select and display character for user and computer
player, computer = select_character()
print('Player is \'%s\' and computer is \'%s\'' % (player, computer))

# initialize result
result = '%%% It is a tie! %%%'


# until the board is full
while space_exist():
    display_board()
    print('# Make your move! Select position [1-9] : ', end = '')
    move = int(input())
    moved, won = make_move(board, player, move)
    
    # check if the move is invalid
    if not moved:
        print('>>> This choice is invalid! Please, try again.')
        continue
    
    if won:
        result = '*** Congratulations! You are the Winner! ***'
        break
    # if computer's move results in the computer winning
    elif computer_move()[1]:
        result = '=== Unfortunately, the computer wins! =='
        break

    
display_board()
print(result)
        
