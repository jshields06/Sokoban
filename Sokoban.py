""" Sokoban is a game in which the player's goal is to move all boxes onto a target until no targets are left.
In this case, "o" are empty targets, "!" are boxes, and "." are fulfilled targets.
You can move by entering a singular letter "w", "a", "s", or "d". Use "q" to quit and space (" ") to reset the board.
"""
from game_settings import *
import copy
start_board = copy.deepcopy(board) #makes a uncanging copy of board for reset function

def move_w(ind): #move up
    count = 0
    occur = 0
    for row in start_board:
        if occur != 1: #only allows sprite to move one space
            if SPRITE in row: #checks for scenarios that may happen if there is a sprite "i" in row
                if start_board[count-1][ind] == EMPTY: #checks above for empty space and fills it if empty
                    start_board[count][ind] = EMPTY
                    start_board[count-1][ind] = SPRITE
                    occur +=1

                elif start_board[count-1][ind] == WALL: #checks above for wall and if there is a wall, no change
                    start_board[count][ind] = SPRITE
                    start_board[count-1][ind] = WALL
                    occur +=1

                elif start_board[count-1][ind] == TARGET: #checks above for target and if there is a target, "i" becomes "I"
                    start_board[count][ind] = EMPTY
                    start_board[count-1][ind] = SPRITE_T
                    occur +=1

                elif start_board[count-1][ind] == BOX_NS: #checks above for box NOT ON A TARGET and goes through various scenarios for collisions
                    if start_board[count-2][ind] == EMPTY:
                        start_board[count][ind] = EMPTY
                        start_board[count-1][ind] = SPRITE
                        start_board[count-2][ind] = BOX_NS
                        occur +=1
                    elif start_board[count-2][ind] == WALL:
                        start_board[count][ind] = SPRITE
                        start_board[count-1][ind] = BOX_NS
                        start_board[count-2][ind] = WALL
                        occur +=1
                    elif start_board[count-2][ind] == BOX_S:
                        start_board[count][ind] = SPRITE
                        start_board[count-1][ind] = BOX_NS
                        start_board[count-2][ind] = BOX_S
                        occur +=1
                    elif start_board[count-2][ind] == BOX_NS:
                        start_board[count][ind] = SPRITE
                        start_board[count-1][ind] = BOX_NS
                        start_board[count-2][ind] = BOX_NS
                        occur +=1
                    elif start_board[count-2][ind] == TARGET:
                        start_board[count][ind] = EMPTY
                        start_board[count-1][ind] = SPRITE
                        start_board[count-2][ind] = BOX_S
                        occur +=1

                elif start_board[count-1][ind] == BOX_S: #checks above for box ON A TARGET and goes through various scenarios for collisions
                    if start_board[count-2][ind] == EMPTY:
                        start_board[count][ind] = EMPTY
                        start_board[count-1][ind] = SPRITE_T
                        start_board[count-2][ind] = BOX_NS
                        occur +=1
                    elif start_board[count-2][ind] == WALL:
                        start_board[count][ind] = SPRITE
                        start_board[count-1][ind] = BOX_S
                        start_board[count-2][ind] = WALL
                        occur +=1
                    elif start_board[count-2][ind] == BOX_S:
                        start_board[count][ind] = SPRITE
                        start_board[count-1][ind] = BOX_S
                        start_board[count-2][ind] = BOX_S
                        occur +=1
                    elif start_board[count-2][ind] == BOX_NS:
                        start_board[count][ind] = SPRITE
                        start_board[count-1][ind] = BOX_S
                        start_board[count-2][ind] = BOX_NS
                        occur +=1
                    elif start_board[count-2][ind] == TARGET:
                        start_board[count][ind] = EMPTY
                        start_board[count-1][ind] = SPRITE_T
                        start_board[count-2][ind] = BOX_S
                        occur +=1

            elif SPRITE_T in row: #does the same as "if SPRITE in row", but if there is a sprite "I" in row
                if start_board[count-1][ind] == EMPTY: #checks above for empty space and fills it if empty
                    start_board[count][ind] = TARGET
                    start_board[count-1][ind] = SPRITE  
                    occur +=1  

                elif start_board[count-1][ind] == WALL: #checks above for wall and if there is a wall, no change
                    start_board[count][ind] = SPRITE_T
                    start_board[count-1][ind] = WALL
                    occur +=1

                elif start_board[count-1][ind] == TARGET: #checks above for target and if there is a target, "I" stays "I"
                    start_board[count][ind] = TARGET
                    start_board[count-1][ind] = SPRITE_T
                    occur +=1

                elif start_board[count-1][ind] == BOX_NS: #checks above for box NOT ON A TARGET and goes through various scenarios for collisions
                    if start_board[count-2][ind] == EMPTY:
                        start_board[count][ind] = TARGET
                        start_board[count-1][ind] = SPRITE
                        start_board[count-2][ind] = BOX_NS
                        occur +=1
                    elif start_board[count-2][ind] == WALL:
                         start_board[count][ind] = SPRITE_T
                         start_board[count-1][ind] = BOX_NS
                         start_board[count-2][ind] = WALL
                         occur+=1
                    elif start_board[count-2][ind] == BOX_S:
                        start_board[count][ind] = SPRITE_T
                        start_board[count-1][ind] = BOX_NS
                        start_board[count-2][ind] = BOX_S
                        occur +=1
                    elif start_board[count-2][ind] == BOX_NS:
                        start_board[count][ind] = SPRITE_T
                        start_board[count-1][ind] = BOX_NS
                        start_board[count-2][ind] = BOX_NS 
                        occur +=1
                    elif start_board[count-2][ind] == TARGET:
                        start_board[count][ind] = TARGET
                        start_board[count-1][ind] = SPRITE
                        start_board[count-2][ind] = BOX_S
                        occur +=1

                elif start_board[count-1][ind] == BOX_S: #checks above for box ON A TARGET and goes through various scenarios for collisions
                    if start_board[count-2][ind] == EMPTY:
                        start_board[count][ind] = TARGET
                        start_board[count-1][ind] = SPRITE_T
                        start_board[count-2][ind] = BOX_NS
                        occur +=1
                    elif start_board[count-2][ind] == WALL:
                        start_board[count][ind] = SPRITE_T
                        start_board[count-1][ind] = BOX_S
                        start_board[count-2][ind] = WALL
                        occur +=1
                    elif start_board[count-2][ind] == BOX_S:
                        start_board[count][ind] = SPRITE_T
                        start_board[count-1][ind] = BOX_S
                        start_board[count-2][ind] = BOX_S
                        occur +=1
                    elif start_board[count-2][ind] == BOX_NS:
                        start_board[count][ind] = SPRITE_T
                        start_board[count-1][ind] = BOX_S
                        start_board[count-2][ind] = BOX_NS
                        occur +=1
                    elif start_board[count-2][ind] == TARGET:
                        start_board[count][ind] = TARGET
                        start_board[count-1][ind] = SPRITE_T
                        start_board[count-2][ind] = BOX_S
                        occur +=1
        count+=1 #indicates specific row       
        
def move_a(ind): #move left
    count = 0
    occur = 0
    for row in start_board:
        if occur != 1: #only allows sprite to move one space
            if SPRITE in row: #checks for scenarios that may happen if there is a sprite "i" in row
                if start_board[count][ind-1] == EMPTY: #checks left for empty space and fills it if empty
                    start_board[count][ind] = EMPTY
                    start_board[count][ind-1] = SPRITE
                    occur +=1
                elif start_board[count][ind-1] == WALL: #checks left for wall and if there is a wall, no change
                    start_board[count][ind] = SPRITE
                    start_board[count][ind-1] = WALL
                    occur +=1
                elif start_board[count][ind-1] == TARGET: #checks left for target and if there is a target, "i" becomes "I"
                    start_board[count][ind] = EMPTY
                    start_board[count][ind-1] = SPRITE_T
                    occur +=1
            
                elif start_board[count][ind-1] == BOX_NS: #checks left for box NOT ON A TARGET and goes through various scenarios for collisions
                    if start_board[count][ind-2] == EMPTY:
                        start_board[count][ind] = EMPTY
                        start_board[count][ind-1] = SPRITE
                        start_board[count][ind-2] = BOX_NS
                        occur +=1
                    elif start_board[count][ind-2] == WALL:
                        start_board[count][ind] = SPRITE
                        start_board[count][ind-1] = BOX_NS
                        start_board[count][ind-2] = WALL
                        occur +=1
                    elif start_board[count][ind-2] == BOX_S:
                        start_board[count][ind] = SPRITE
                        start_board[count][ind-1] = BOX_NS
                        start_board[count][ind-2] = BOX_S
                        occur +=1
                    elif start_board[count][ind-2] == BOX_NS:
                        start_board[count][ind] = SPRITE
                        start_board[count][ind-1] = BOX_NS
                        start_board[count][ind-2] = BOX_NS
                        occur +=1
                    elif start_board[count][ind-2] == TARGET:
                        start_board[count][ind] = EMPTY
                        start_board[count][ind-1] = SPRITE
                        start_board[count][ind-2] = BOX_S
                        occur +=1

                elif start_board[count][ind-1] == BOX_S: #checks left for box ON A TARGET and goes through various scenarios for collisions
                    if start_board[count][ind-2] == EMPTY:
                        start_board[count][ind] = EMPTY
                        start_board[count][ind-1] = SPRITE_T
                        start_board[count][ind-2] = BOX_NS
                        occur +=1
                    elif start_board[count][ind-2] == WALL: 
                        start_board[count][ind] = SPRITE
                        start_board[count][ind-1] = BOX_S
                        start_board[count][ind-2] = WALL
                        occur +=1
                    elif start_board[count][ind-2] == BOX_S: 
                        start_board[count][ind] = SPRITE
                        start_board[count][ind-1] = BOX_S
                        start_board[count][ind-2] = BOX_S
                        occur +=1
                    elif start_board[count][ind-2] == BOX_NS:
                        start_board[count][ind] = SPRITE
                        start_board[count][ind-1] = BOX_S
                        start_board[count][ind-2] = BOX_NS
                        occur +=1
                    elif start_board[count][ind-2] == TARGET:
                        start_board[count][ind] = EMPTY
                        start_board[count][ind-1] = SPRITE_T
                        start_board[count][ind-2] = BOX_S
                        occur +=1

            elif SPRITE_T in row: #does the same as "if SPRITE in row", but if there is a sprite "I" in row
                if start_board[count][ind-1] == EMPTY: #checks left for empty space and fills it if empty
                    start_board[count][ind] = TARGET
                    start_board[count][ind-1] = SPRITE  
                    occur +=1  
                elif start_board[count][ind-1] == WALL: #checks left for wall and if there is a wall, no change
                    start_board[count][ind] = SPRITE_T
                    start_board[count][ind-1] = WALL
                    occur +=1
                elif start_board[count][ind-1] == TARGET: #checks left for target and if there is a target, "I" stays "I"
                    start_board[count][ind] = TARGET
                    start_board[count][ind-1] = SPRITE_T
                    occur +=1

                elif start_board[count][ind-1] == BOX_NS: #checks left for box NOT ON A TARGET and goes through various scenarios for collisions
                    if start_board[count][ind-2] == EMPTY:
                        start_board[count][ind] = TARGET
                        start_board[count][ind-1] = SPRITE
                        start_board[count][ind-2] = BOX_NS
                        occur +=1
                    elif start_board[count][ind-2] == WALL:
                        start_board[count][ind] = SPRITE_T
                        start_board[count][ind-1] = BOX_NS
                        start_board[count][ind-2] = WALL
                        occur+=1
                    elif start_board[count][ind-2] == BOX_S:
                        start_board[count][ind] = SPRITE_T
                        start_board[count][ind-1] = BOX_NS
                        start_board[count][ind-2] = BOX_S
                        occur +=1
                    elif start_board[count][ind-2] == BOX_NS:
                        start_board[count][ind] = SPRITE_T
                        start_board[count][ind-1] = BOX_NS
                        start_board[count][ind-2] = BOX_NS 
                        occur +=1
                    elif start_board[count][ind-2] == TARGET:
                        start_board[count][ind] = TARGET
                        start_board[count][ind-1] = SPRITE
                        start_board[count][ind-2] = BOX_S
                        occur +=1
            
                elif start_board[count][ind-1] == BOX_S: #checks left for box ON A TARGET and goes through various scenarios for collisions
                    if start_board[count][ind-2] == EMPTY:
                        start_board[count][ind] = TARGET
                        start_board[count][ind-1] = SPRITE_T
                        start_board[count][ind-2] = BOX_NS
                        occur +=1
                    elif start_board[count][ind-2] == WALL:
                        start_board[count][ind] = SPRITE_T
                        start_board[count][ind-1] = BOX_S
                        start_board[count][ind-2] = WALL
                        occur +=1
                    elif start_board[count][ind-2] == BOX_S:
                        start_board[count][ind] = SPRITE_T
                        start_board[count][ind-1] = BOX_S
                        start_board[count][ind-2] = BOX_S
                        occur +=1
                    elif start_board[count][ind-2] == BOX_NS:
                        start_board[count][ind] = SPRITE_T
                        start_board[count][ind-1] = BOX_S
                        start_board[count][ind-2] = BOX_NS
                        occur +=1
                    elif start_board[count][ind-2] == TARGET:
                        start_board[count][ind] = TARGET
                        start_board[count][ind-1] = SPRITE_T
                        start_board[count][ind-2] = BOX_S
                        occur +=1
        count+=1 #indicates specific row  

def move_s(ind): #move down
    count = 0
    occur = 0
    for row in start_board:
        if occur != 1: #only allows sprite to move one space
            if SPRITE in row: #checks for scenarios that may happen if there is a sprite "i" in row
                if start_board[count+1][ind] == EMPTY: #checks below for empty space and fills it if empty
                    start_board[count][ind] = EMPTY
                    start_board[count+1][ind] = SPRITE
                    occur +=1

                elif start_board[count+1][ind] == WALL: #checks below for wall and if there is a wall, no change
                    start_board[count][ind] = SPRITE
                    start_board[count+1][ind] = WALL
                    occur +=1

                elif start_board[count+1][ind] == TARGET: #checks below for target and if there is a target, "i" becomes "I"
                    start_board[count][ind] = EMPTY
                    start_board[count+1][ind] = SPRITE_T
                    occur +=1

                elif start_board[count+1][ind] == BOX_NS: #checks below for box NOT ON A TARGET and goes through various scenarios for collisions
                    if start_board[count+2][ind] == EMPTY:
                        start_board[count][ind] = EMPTY
                        start_board[count+1][ind] = SPRITE
                        start_board[count+2][ind] = BOX_NS
                        occur +=1
                    elif start_board[count+2][ind] == WALL:
                        start_board[count][ind] = SPRITE
                        start_board[count+1][ind] = BOX_NS
                        start_board[count+2][ind] = WALL
                        occur +=1
                    elif start_board[count+2][ind] == BOX_S:
                        start_board[count][ind] = SPRITE
                        start_board[count+1][ind] = BOX_NS
                        start_board[count+2][ind] = BOX_S
                        occur +=1
                    elif start_board[count+2][ind] == BOX_NS:
                        start_board[count][ind] = SPRITE
                        start_board[count+1][ind] = BOX_NS
                        start_board[count+2][ind] = BOX_NS
                        occur +=1
                    elif start_board[count+2][ind] == TARGET:
                        start_board[count][ind] = EMPTY
                        start_board[count+1][ind] = SPRITE
                        start_board[count+2][ind] = BOX_S
                        occur +=1

                elif start_board[count+1][ind] == BOX_S: #checks below for box ON A TARGET and goes through various scenarios for collisions
                    if start_board[count+2][ind] == EMPTY:
                        start_board[count][ind] = EMPTY
                        start_board[count+1][ind] = SPRITE_T
                        start_board[count+2][ind] = BOX_NS
                        occur +=1
                    elif start_board[count+2][ind] == WALL:
                        start_board[count][ind] = SPRITE
                        start_board[count+1][ind] = BOX_S
                        start_board[count+2][ind] = WALL
                        occur +=1
                    elif start_board[count+2][ind] == BOX_S:
                        start_board[count][ind] = SPRITE
                        start_board[count+1][ind] = BOX_S
                        start_board[count+2][ind] = BOX_S
                        occur +=1
                    elif start_board[count+2][ind] == BOX_NS:
                        start_board[count][ind] = SPRITE
                        start_board[count+1][ind] = BOX_S
                        start_board[count+2][ind] = BOX_NS
                        occur +=1
                    elif start_board[count+2][ind] == TARGET:
                        start_board[count][ind] = EMPTY
                        start_board[count+1][ind] = SPRITE_T
                        start_board[count+2][ind] = BOX_S
                        occur +=1

            elif SPRITE_T in row: #does the same as "if SPRITE in row", but if there is a sprite "I" in row
                if start_board[count+1][ind] == EMPTY: #checks below for empty space and fills it if empty
                    start_board[count][ind] = TARGET
                    start_board[count+1][ind] = SPRITE  
                    occur +=1  

                elif start_board[count+1][ind] == WALL: #checks below for wall and if there is a wall, no change
                    start_board[count][ind] = SPRITE_T
                    start_board[count+1][ind] = WALL
                    occur +=1

                elif start_board[count+1][ind] == TARGET: #checks below for target and if there is a target, "I" stays "I"
                    start_board[count][ind] = TARGET
                    start_board[count+1][ind] = SPRITE_T
                    occur +=1

                elif start_board[count+1][ind] == BOX_NS: #checks below for box NOT ON A TARGET and goes through various scenarios for collisions
                    if start_board[count+2][ind] == EMPTY:
                        start_board[count][ind] = TARGET
                        start_board[count+1][ind] = SPRITE
                        start_board[count+2][ind] = BOX_NS
                        occur +=1
                    elif start_board[count+2][ind] == WALL:
                         start_board[count][ind] = SPRITE_T
                         start_board[count+1][ind] = BOX_NS
                         start_board[count+2][ind] = WALL
                         occur+=1
                    elif start_board[count+2][ind] == BOX_S:
                        start_board[count][ind] = SPRITE_T
                        start_board[count+1][ind] = BOX_NS
                        start_board[count+2][ind] = BOX_S
                        occur +=1
                    elif start_board[count+2][ind] == BOX_NS:
                        start_board[count][ind] = SPRITE_T
                        start_board[count+1][ind] = BOX_NS
                        start_board[count+2][ind] = BOX_NS 
                        occur +=1
                    elif start_board[count+2][ind] == TARGET:
                        start_board[count][ind] = TARGET
                        start_board[count+1][ind] = SPRITE
                        start_board[count+2][ind] = BOX_S
                        occur +=1

                elif start_board[count+1][ind] == BOX_S: #checks below for box ON A TARGET and goes through various scenarios for collisions
                    if start_board[count+2][ind] == EMPTY:
                        start_board[count][ind] = TARGET
                        start_board[count+1][ind] = SPRITE_T
                        start_board[count+2][ind] = BOX_NS
                        occur +=1
                    elif start_board[count+2][ind] == WALL:
                        start_board[count][ind] = SPRITE_T
                        start_board[count+1][ind] = BOX_S
                        start_board[count+2][ind] = WALL
                        occur +=1
                    elif start_board[count+2][ind] == BOX_S:
                        start_board[count][ind] = SPRITE_T
                        start_board[count+1][ind] = BOX_S
                        start_board[count+2][ind] = BOX_S
                        occur +=1
                    elif start_board[count+2][ind] == BOX_NS:
                        start_board[count][ind] = SPRITE_T
                        start_board[count+1][ind] = BOX_S
                        start_board[count+2][ind] = BOX_NS
                        occur +=1
                    elif start_board[count+2][ind] == TARGET:
                        start_board[count][ind] = TARGET
                        start_board[count+1][ind] = SPRITE_T
                        start_board[count+2][ind] = BOX_S
                        occur +=1
        count+=1 #indicates specific row  

def move_d(ind): #move right
    count = 0
    occur = 0
    for row in start_board:
        if occur != 1: #only allows sprite to move one space
            if SPRITE in row: #checks for scenarios that may happen if there is a sprite "i" in row
                if start_board[count][ind+1] == EMPTY: #checks right for empty space and fills it if empty
                    start_board[count][ind] = EMPTY
                    start_board[count][ind+1] = SPRITE
                    occur +=1
                elif start_board[count][ind+1] == WALL: #checks right for wall and if there is a wall, no change
                    start_board[count][ind] = SPRITE
                    start_board[count][ind+1] = WALL
                    occur +=1
                elif start_board[count][ind+1] == TARGET:  #checks right for target and if there is a target, "i" becomes "I"
                    start_board[count][ind] = EMPTY
                    start_board[count][ind+1] = SPRITE_T
                    occur +=1
            
                elif start_board[count][ind+1] == BOX_NS:  #checks right for box NOT ON A TARGET and goes through various scenarios for collisions
                    if start_board[count][ind+2] == EMPTY:
                        start_board[count][ind] = EMPTY
                        start_board[count][ind+1] = SPRITE
                        start_board[count][ind+2] = BOX_NS
                        occur +=1
                    elif start_board[count][ind+2] == WALL:
                        start_board[count][ind] = SPRITE
                        start_board[count][ind+1] = BOX_NS
                        start_board[count][ind+2] = WALL
                        occur +=1
                    elif start_board[count][ind+2] == BOX_S:
                        start_board[count][ind] = SPRITE
                        start_board[count][ind+1] = BOX_NS
                        start_board[count][ind+2] = BOX_S
                        occur +=1
                    elif start_board[count][ind+2] == BOX_NS:
                        start_board[count][ind] = SPRITE
                        start_board[count][ind+1] = BOX_NS
                        start_board[count][ind+2] = BOX_NS
                        occur +=1
                    elif start_board[count][ind+2] == TARGET:
                        start_board[count][ind] = EMPTY
                        start_board[count][ind+1] = SPRITE
                        start_board[count][ind+2] = BOX_S
                        occur +=1

                elif start_board[count][ind+1] == BOX_S: #checks right for box ON A TARGET and goes through various scenarios for collisions
                    if start_board[count][ind+2] == EMPTY:
                        start_board[count][ind] = EMPTY
                        start_board[count][ind+1] = SPRITE_T
                        start_board[count][ind+2] = BOX_NS
                        occur +=1
                    elif start_board[count][ind+2] == WALL:
                        start_board[count][ind] = SPRITE
                        start_board[count][ind+1] = BOX_S
                        start_board[count][ind+2] = WALL
                        occur +=1
                    elif start_board[count][ind+2] == BOX_S:
                        start_board[count][ind] = SPRITE
                        start_board[count][ind+1] = BOX_S
                        start_board[count][ind+2] = BOX_S
                        occur +=1
                    elif start_board[count][ind+2] == BOX_NS:
                        start_board[count][ind] = SPRITE
                        start_board[count][ind+1] = BOX_S
                        start_board[count][ind+2] = BOX_NS
                        occur +=1
                    elif start_board[count][ind+2] == TARGET:
                        start_board[count][ind] = EMPTY
                        start_board[count][ind+1] = SPRITE_T
                        start_board[count][ind+2] = BOX_S
                        occur +=1

            elif SPRITE_T in row: #does the same as "if SPRITE in row", but if there is a sprite "I" in row
                if start_board[count][ind+1] == EMPTY: #checks right for empty space and fills it if empty
                    start_board[count][ind] = TARGET
                    start_board[count][ind+1] = SPRITE  
                    occur +=1  
                elif start_board[count][ind+1] == WALL: #checks right for wall and if there is a wall, no change
                    start_board[count][ind] = SPRITE_T
                    start_board[count][ind+1] = WALL
                    occur +=1
                elif start_board[count][ind+1] == TARGET:  #checks right for target and if there is a target, "I" stays "I"
                    start_board[count][ind] = TARGET
                    start_board[count][ind+1] = SPRITE_T
                    occur +=1

                elif start_board[count][ind+1] == BOX_NS: #checks right for box NOT ON A TARGET and goes through various scenarios for collisions
                    if start_board[count][ind+2] == EMPTY:
                        start_board[count][ind] = TARGET
                        start_board[count][ind+1] = SPRITE
                        start_board[count][ind+2] = BOX_NS
                        occur +=1
                    elif start_board[count][ind+2] == WALL:
                        start_board[count][ind] = SPRITE_T
                        start_board[count][ind+1] = BOX_NS
                        start_board[count][ind+2] = WALL
                        occur+=1
                    elif start_board[count][ind+2] == BOX_S:
                        start_board[count][ind] = SPRITE_T
                        start_board[count][ind+1] = BOX_NS
                        start_board[count][ind+2] = BOX_S
                        occur +=1
                    elif start_board[count][ind+2] == BOX_NS:
                        start_board[count][ind] = SPRITE_T
                        start_board[count][ind+1] = BOX_NS
                        start_board[count][ind+2] = BOX_NS 
                        occur +=1
                    elif start_board[count][ind+2] == TARGET:
                        start_board[count][ind] = TARGET
                        start_board[count][ind+1] = SPRITE
                        start_board[count][ind+2] = BOX_S
                        occur +=1
            
                elif start_board[count][ind+1] == BOX_S: #checks right for box ON A TARGET and goes through various scenarios for collisions
                    if start_board[count][ind+2] == EMPTY:
                        start_board[count][ind] = TARGET
                        start_board[count][ind+1] = SPRITE_T
                        start_board[count][ind+2] = BOX_NS
                        occur +=1
                    elif start_board[count][ind+2] == WALL:
                        start_board[count][ind] = SPRITE_T
                        start_board[count][ind+1] = BOX_S
                        start_board[count][ind+2] = WALL
                        occur +=1
                    elif start_board[count][ind+2] == BOX_S:
                        start_board[count][ind] = SPRITE_T
                        start_board[count][ind+1] = BOX_S
                        start_board[count][ind+2] = BOX_S
                        occur +=1
                    elif start_board[count][ind+2] == BOX_NS:
                        start_board[count][ind] = SPRITE_T
                        start_board[count][ind+1] = BOX_S
                        start_board[count][ind+2] = BOX_NS
                        occur +=1
                    elif start_board[count][ind+2] == TARGET:
                        start_board[count][ind] = TARGET
                        start_board[count][ind+1] = SPRITE_T
                        start_board[count][ind+2] = BOX_S
                        occur +=1
        count+=1 #indicates specific row  

def reset(b): #calls deepcopied board
    for i in b:
        print(*i, sep=" ") #print og board
    print()
    
num = 0
index_sprite = 0

for row in start_board:
    for col in row:
        if TARGET == col:
            num +=1
while num > 0:
    num = 0
    for row in start_board:
        print(*row, sep=" ") #print start_board
        if SPRITE in row:
            index_sprite = row.index(SPRITE) #find where i is
        elif SPRITE_T in row:
            index_sprite = row.index(SPRITE_T) #find where I is
        for col in row:
            if TARGET == col:
                num +=1

    if num == 0: #check if any open targets and if not, player wins
        print("You Win!")
        break
    choice = str(input())
    print()

    while choice not in CONTROLS:
        choice = input("enter a valid move:\n") #choice error

    if choice in CONTROLS and choice == EMPTY: #reset board
        start_board = copy.deepcopy(board)
        continue
    elif choice in CONTROLS and choice == QUIT: #quit game
        print("Goodbye")
        break
    elif choice in CONTROLS and choice == 'w': #move up
        move_w(index_sprite)
        continue
    elif choice in CONTROLS and choice == 'a': #move left
        move_a(index_sprite)
        continue
    elif choice in CONTROLS and choice == 's': #move down
        move_s(index_sprite)
        continue
    elif choice in CONTROLS and choice == 'd': #move right
        move_d(index_sprite)
        continue
