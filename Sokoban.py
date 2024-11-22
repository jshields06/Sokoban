from game_settings import *
import copy
start_board = copy.deepcopy(board)

def move_w(ind):
    count = 0
    occur = 0
    for row in start_board:
        if occur != 1:

            if SPRITE in row and start_board[count-1][ind] == EMPTY:
                start_board[count][ind] = EMPTY
                start_board[count-1][ind] = SPRITE
                occur +=1
            elif SPRITE in row and start_board[count-1][ind] == WALL:
                start_board[count][ind] = SPRITE
                start_board[count-1][ind] = WALL
                occur +=1
            elif SPRITE in row and start_board[count-1][ind] == TARGET:
                start_board[count][ind] = EMPTY
                start_board[count-1][ind] = SPRITE_T
                occur +=1

            elif SPRITE in row and start_board[count-1][ind] == BOX_NS and start_board[count-2][ind] == EMPTY:
                start_board[count][ind] = EMPTY
                start_board[count-1][ind] = SPRITE
                start_board[count-2][ind] = BOX_NS
                occur +=1
            elif SPRITE in row and start_board[count-1][ind] == BOX_NS and start_board[count-2][ind] == WALL:
                start_board[count][ind] = SPRITE
                start_board[count-1][ind] = BOX_NS
                start_board[count-2][ind] = WALL
                occur +=1
            elif SPRITE in row and start_board[count-1][ind] == BOX_NS and start_board[count-2][ind] == BOX_S:
                start_board[count][ind] = SPRITE
                start_board[count-1][ind] = BOX_NS
                start_board[count-2][ind] = BOX_S
                occur +=1
            elif SPRITE in row and start_board[count-1][ind] == BOX_NS and start_board[count-2][ind] == BOX_NS:
                start_board[count][ind] = SPRITE
                start_board[count-1][ind] = BOX_NS
                start_board[count-2][ind] = BOX_NS
                occur +=1
            elif SPRITE in row and start_board[count-1][ind] == BOX_NS and start_board[count-2][ind] == TARGET:
                start_board[count][ind] = EMPTY
                start_board[count-1][ind] = SPRITE
                start_board[count-2][ind] = BOX_S
                occur +=1

            elif SPRITE in row and start_board[count-1][ind] == BOX_S and start_board[count-2][ind] == EMPTY:
                start_board[count][ind] = EMPTY
                start_board[count-1][ind] = SPRITE_T
                start_board[count-2][ind] = BOX_NS
                occur +=1
            elif SPRITE in row and start_board[count-1][ind] == BOX_S and start_board[count-2][ind] == WALL:
                start_board[count][ind] = SPRITE
                start_board[count-1][ind] = BOX_S
                start_board[count-2][ind] = WALL
                occur +=1
            elif SPRITE in row and start_board[count-1][ind] == BOX_S and start_board[count-2][ind] == BOX_S:
                start_board[count][ind] = SPRITE
                start_board[count-1][ind] = BOX_S
                start_board[count-2][ind] = BOX_S
                occur +=1
            elif SPRITE in row and start_board[count-1][ind] == BOX_S and start_board[count-2][ind] == BOX_NS:
                start_board[count][ind] = SPRITE
                start_board[count-1][ind] = BOX_S
                start_board[count-2][ind] = BOX_NS
                occur +=1
            elif SPRITE in row and start_board[count-1][ind] == BOX_S and start_board[count-2][ind] == TARGET:
                start_board[count][ind] = EMPTY
                start_board[count-1][ind] = SPRITE_T
                start_board[count-2][ind] = BOX_S
                occur +=1

            elif SPRITE_T in row and start_board[count-1][ind] == EMPTY:
                start_board[count][ind] = TARGET
                start_board[count-1][ind] = SPRITE  
                occur +=1  
            elif SPRITE_T in row and start_board[count-1][ind] == WALL:
                start_board[count][ind] = SPRITE_T
                start_board[count-1][ind] = WALL
                occur +=1
            elif SPRITE_T in row and start_board[count-1][ind] == TARGET:
                start_board[count][ind] = TARGET
                start_board[count-1][ind] = SPRITE_T
                occur +=1

            elif SPRITE_T in row and start_board[count-1][ind] == BOX_NS and start_board[count-2][ind] == EMPTY:
                start_board[count][ind] = TARGET
                start_board[count-1][ind] = SPRITE
                start_board[count-2][ind] = BOX_NS
                occur +=1
            elif SPRITE_T in row and start_board[count-1][ind] == BOX_NS and start_board[count-2][ind] == WALL:
                start_board[count][ind] = SPRITE_T
                start_board[count-1][ind] = BOX_NS
                start_board[count-2][ind] = WALL
                occur+=1
            elif SPRITE_T in row and start_board[count-1][ind] == BOX_NS and start_board[count-2][ind] == BOX_S:
                start_board[count][ind] = SPRITE_T
                start_board[count-1][ind] = BOX_NS
                start_board[count-2][ind] = BOX_S
                occur +=1
            elif SPRITE_T in row and start_board[count-1][ind] == BOX_NS and start_board[count-2][ind] == BOX_NS:
                start_board[count][ind] = SPRITE_T
                start_board[count-1][ind] = BOX_NS
                start_board[count-2][ind] = BOX_NS 
                occur +=1
            elif SPRITE_T in row and start_board[count-1][ind] == BOX_NS and start_board[count-2][ind] == TARGET:
                start_board[count][ind] = TARGET
                start_board[count-1][ind] = SPRITE
                start_board[count-2][ind] = BOX_S
                occur +=1

            elif SPRITE_T in row and start_board[count-1][ind] == BOX_S and start_board[count-2][ind] == EMPTY:
                start_board[count][ind] = TARGET
                start_board[count-1][ind] = SPRITE_T
                start_board[count-2][ind] = BOX_NS
                occur +=1
            elif SPRITE_T in row and start_board[count-1][ind] == BOX_S and start_board[count-2][ind] == WALL:
                start_board[count][ind] = SPRITE_T
                start_board[count-1][ind] = BOX_S
                start_board[count-2][ind] = WALL
                occur +=1
            elif SPRITE_T in row and start_board[count-1][ind] == BOX_S and start_board[count-2][ind] == BOX_S:
                start_board[count][ind] = SPRITE_T
                start_board[count-1][ind] = BOX_S
                start_board[count-2][ind] = BOX_S
                occur +=1
            elif SPRITE_T in row and start_board[count-1][ind] == BOX_S and start_board[count-2][ind] == BOX_NS:
                start_board[count][ind] = SPRITE_T
                start_board[count-1][ind] = BOX_S
                start_board[count-2][ind] = BOX_NS
                occur +=1
            elif SPRITE_T in row and start_board[count-1][ind] == BOX_S and start_board[count-2][ind] == TARGET:
                start_board[count][ind] = TARGET
                start_board[count-1][ind] = SPRITE_T
                start_board[count-2][ind] = BOX_S
                occur +=1
            count+=1        
        
def move_a(ind):
    count = 0
    occur = 0
    for row in start_board:
        if occur != 1:
            if SPRITE in row and start_board[count][ind-1] == EMPTY:
                start_board[count][ind] = EMPTY
                start_board[count][ind-1] = SPRITE
                occur +=1
            elif SPRITE in row and start_board[count][ind-1] == WALL:
                start_board[count][ind] = SPRITE
                start_board[count][ind-1] = WALL
                occur +=1
            elif SPRITE in row and start_board[count][ind-1] == TARGET:
                start_board[count][ind] = EMPTY
                start_board[count][ind-1] = SPRITE_T
                occur +=1
            
            elif SPRITE in row and start_board[count][ind-1] == BOX_NS and start_board[count][ind-2] == EMPTY:
                start_board[count][ind] = EMPTY
                start_board[count][ind-1] = SPRITE
                start_board[count][ind-2] = BOX_NS
                occur +=1
            elif SPRITE in row and start_board[count][ind-1] == BOX_NS and start_board[count][ind-2] == WALL:
                start_board[count][ind] = SPRITE
                start_board[count][ind-1] = BOX_NS
                start_board[count][ind-2] = WALL
                occur +=1
            elif SPRITE in row and start_board[count][ind-1] == BOX_NS and start_board[count][ind-2] == BOX_S:
                start_board[count][ind] = SPRITE
                start_board[count][ind-1] = BOX_NS
                start_board[count][ind-2] = BOX_S
                occur +=1
            elif SPRITE in row and start_board[count][ind-1] == BOX_NS and start_board[count][ind-2] == BOX_NS:
                start_board[count][ind] = SPRITE
                start_board[count][ind-1] = BOX_NS
                start_board[count][ind-2] = BOX_NS
                occur +=1
            elif SPRITE in row and start_board[count][ind-1] == BOX_NS and start_board[count][ind-2] == TARGET:
                start_board[count][ind] = EMPTY
                start_board[count][ind-1] = SPRITE
                start_board[count][ind-2] = BOX_S
                occur +=1

            elif SPRITE in row and start_board[count][ind-1] == BOX_S and start_board[count][ind-2] == EMPTY:
                start_board[count][ind] = EMPTY
                start_board[count][ind-1] = SPRITE_T
                start_board[count][ind-2] = BOX_NS
                occur +=1
            elif SPRITE in row and start_board[count][ind-1] == BOX_S and start_board[count][ind-2] == WALL:
                start_board[count][ind] = SPRITE
                start_board[count][ind-1] = BOX_S
                start_board[count][ind-2] = WALL
                occur +=1
            elif SPRITE in row and start_board[count][ind-1] == BOX_S and start_board[count][ind-2] == BOX_S:
                start_board[count][ind] = SPRITE
                start_board[count][ind-1] = BOX_S
                start_board[count][ind-2] = BOX_S
                occur +=1
            elif SPRITE in row and start_board[count][ind-1] == BOX_S and start_board[count][ind-2] == BOX_NS:
                start_board[count][ind] = SPRITE
                start_board[count][ind-1] = BOX_S
                start_board[count][ind-2] = BOX_NS
                occur +=1
            elif SPRITE in row and start_board[count][ind-1] == BOX_S and start_board[count][ind-2] == TARGET:
                start_board[count][ind] = EMPTY
                start_board[count][ind-1] = SPRITE_T
                start_board[count][ind-2] = BOX_S
                occur +=1

            elif SPRITE_T in row and start_board[count][ind-1] == EMPTY:
                start_board[count][ind] = TARGET
                start_board[count][ind-1] = SPRITE  
                occur +=1  
            elif SPRITE_T in row and start_board[count][ind-1] == WALL:
                start_board[count][ind] = SPRITE_T
                start_board[count][ind-1] = WALL
                occur +=1
            elif SPRITE_T in row and start_board[count][ind-1] == TARGET:
                start_board[count][ind] = TARGET
                start_board[count][ind-1] = SPRITE_T
                occur +=1

            elif SPRITE_T in row and start_board[count][ind-1] == BOX_NS and start_board[count][ind-2] == EMPTY:
                start_board[count][ind] = TARGET
                start_board[count][ind-1] = SPRITE
                start_board[count][ind-2] = BOX_NS
                occur +=1
            elif SPRITE_T in row and start_board[count][ind-1] == BOX_NS and start_board[count][ind-2] == WALL:
                start_board[count][ind] = SPRITE_T
                start_board[count][ind-1] = BOX_NS
                start_board[count][ind-2] = WALL
                occur+=1
            elif SPRITE_T in row and start_board[count][ind-1] == BOX_NS and start_board[count][ind-2] == BOX_S:
                start_board[count][ind] = SPRITE_T
                start_board[count][ind-1] = BOX_NS
                start_board[count][ind-2] = BOX_S
                occur +=1
            elif SPRITE_T in row and start_board[count][ind-1] == BOX_NS and start_board[count][ind-2] == BOX_NS:
                start_board[count][ind] = SPRITE_T
                start_board[count][ind-1] = BOX_NS
                start_board[count][ind-2] = BOX_NS 
                occur +=1
            elif SPRITE_T in row and start_board[count][ind-1] == BOX_NS and start_board[count][ind-2] == TARGET:
                start_board[count][ind] = TARGET
                start_board[count][ind-1] = SPRITE
                start_board[count][ind-2] = BOX_S
                occur +=1
            
            elif SPRITE_T in row and start_board[count][ind-1] == BOX_S and start_board[count][ind-2] == EMPTY:
                start_board[count][ind] = TARGET
                start_board[count][ind-1] = SPRITE_T
                start_board[count][ind-2] = BOX_NS
                occur +=1
            elif SPRITE_T in row and start_board[count][ind-1] == BOX_S and start_board[count][ind-2] == WALL:
                start_board[count][ind] = SPRITE_T
                start_board[count][ind-1] = BOX_S
                start_board[count][ind-2] = WALL
                occur +=1
            elif SPRITE_T in row and start_board[count][ind-1] == BOX_S and start_board[count][ind-2] == BOX_S:
                start_board[count][ind] = SPRITE_T
                start_board[count][ind-1] = BOX_S
                start_board[count][ind-2] = BOX_S
                occur +=1
            elif SPRITE_T in row and start_board[count][ind-1] == BOX_S and start_board[count][ind-2] == BOX_NS:
                start_board[count][ind] = SPRITE_T
                start_board[count][ind-1] = BOX_S
                start_board[count][ind-2] = BOX_NS
                occur +=1
            elif SPRITE_T in row and start_board[count][ind-1] == BOX_S and start_board[count][ind-2] == TARGET:
                start_board[count][ind] = TARGET
                start_board[count][ind-1] = SPRITE_T
                start_board[count][ind-2] = BOX_S
                occur +=1
            count+=1

def move_s(ind):
    count = 0
    occur = 0
    for row in start_board:
        if occur != 1:
            if SPRITE in row and start_board[count+1][ind] == EMPTY:
                start_board[count][ind] = EMPTY
                start_board[count+1][ind] = SPRITE   
                occur +=1 
            elif SPRITE in row and start_board[count+1][ind] == WALL:
                start_board[count][ind] = SPRITE
                start_board[count+1][ind] = WALL
                occur +=1
            elif SPRITE in row and start_board[count+1][ind] == TARGET:
                start_board[count][ind] = EMPTY
                start_board[count+1][ind] = SPRITE_T
                occur +=1

            elif SPRITE in row and start_board[count+1][ind] == BOX_NS and start_board[count+2][ind] == EMPTY:
                start_board[count][ind] = EMPTY
                start_board[count+1][ind] = SPRITE
                start_board[count+2][ind] = BOX_NS
                occur +=1
            elif SPRITE in row and start_board[count+1][ind] == BOX_NS and start_board[count+2][ind] == WALL:
                start_board[count][ind] = SPRITE
                start_board[count+1][ind] = BOX_NS
                start_board[count+2][ind] = WALL
                occur +=1
            elif SPRITE in row and start_board[count+1][ind] == BOX_NS and start_board[count+2][ind] == BOX_S:
                start_board[count][ind] = SPRITE
                start_board[count+1][ind] = BOX_NS
                start_board[count+2][ind] = BOX_S
                occur +=1
            elif SPRITE in row and start_board[count+1][ind] == BOX_NS and start_board[count+2][ind] == BOX_NS:
                start_board[count][ind] = SPRITE
                start_board[count+1][ind] = BOX_NS
                start_board[count+2][ind] = BOX_NS
                occur +=1
            elif SPRITE in row and start_board[count+1][ind] == BOX_NS and start_board[count+2][ind] == TARGET:
                start_board[count][ind] = EMPTY
                start_board[count+1][ind] = SPRITE
                start_board[count+2][ind] = BOX_S
                occur +=1

            elif SPRITE in row and start_board[count+1][ind] == BOX_S and start_board[count+2][ind] == EMPTY:
                start_board[count][ind] = EMPTY
                start_board[count+1][ind] = SPRITE_T
                start_board[count+2][ind] = BOX_NS
                occur +=1
            elif SPRITE in row and start_board[count+1][ind] == BOX_S and start_board[count+2][ind] == WALL:
                start_board[count][ind] = SPRITE
                start_board[count+1][ind] = BOX_S
                start_board[count+2][ind] = WALL
                occur +=1
            elif SPRITE in row and start_board[count+1][ind] == BOX_S and start_board[count+2][ind] == BOX_S:
                start_board[count][ind] = SPRITE
                start_board[count+1][ind] = BOX_S
                start_board[count+2][ind] = BOX_S
                occur +=1
            elif SPRITE in row and start_board[count+1][ind] == BOX_S and start_board[count+2][ind] == BOX_NS:
                start_board[count][ind] = SPRITE
                start_board[count+1][ind] = BOX_S
                start_board[count+2][ind] = BOX_NS
                occur +=1
            elif SPRITE in row and start_board[count+1][ind] == BOX_S and start_board[count+2][ind] == TARGET:
                start_board[count][ind] = EMPTY
                start_board[count+1][ind] = SPRITE_T
                start_board[count+2][ind] = BOX_S
                occur +=1

            elif SPRITE_T in row and start_board[count+1][ind] == EMPTY:
                start_board[count][ind] = TARGET
                start_board[count+1][ind] = SPRITE   
                occur +=1 
            elif SPRITE_T in row and start_board[count+1][ind] == WALL:
                start_board[count][ind] = SPRITE_T
                start_board[count+1][ind] = WALL
                occur +=1
            elif SPRITE_T in row and start_board[count+1][ind] == TARGET:
                start_board[count][ind] = TARGET
                start_board[count+1][ind] = SPRITE_T
                occur +=1

            elif SPRITE_T in row and start_board[count+1][ind] == BOX_NS and start_board[count+2][ind] == EMPTY:
                start_board[count][ind] = TARGET
                start_board[count+1][ind] = SPRITE
                start_board[count+2][ind] = BOX_NS
                occur +=1
            elif SPRITE_T in row and start_board[count+1][ind] == BOX_NS and start_board[count+2][ind] == WALL:
                start_board[count][ind] = SPRITE_T
                start_board[count+1][ind] = BOX_NS
                start_board[count+2][ind] = WALL
                occur +=1
            elif SPRITE_T in row and start_board[count+1][ind] == BOX_NS and start_board[count+2][ind] == BOX_S:
                start_board[count][ind] = SPRITE_T
                start_board[count+1][ind] = BOX_NS
                start_board[count+2][ind] = BOX_S
                occur +=1
            elif SPRITE_T in row and start_board[count+1][ind] == BOX_NS and start_board[count+2][ind] == BOX_NS:
                start_board[count][ind] = SPRITE_T
                start_board[count+1][ind] = BOX_NS
                start_board[count+2][ind] = BOX_NS 
                occur +=1
            elif SPRITE_T in row and start_board[count+1][ind] == BOX_NS and start_board[count+2][ind] == TARGET:
                start_board[count][ind] = TARGET
                start_board[count+1][ind] = SPRITE
                start_board[count+2][ind] = BOX_S
                occur +=1

            elif SPRITE_T in row and start_board[count+1][ind] == BOX_S and start_board[count+2][ind] == EMPTY:
                start_board[count][ind] = TARGET
                start_board[count+1][ind] = SPRITE_T
                start_board[count+2][ind] = BOX_NS
                occur +=1
            elif SPRITE_T in row and start_board[count+1][ind] == BOX_S and start_board[count+2][ind] == WALL:
                start_board[count][ind] = SPRITE_T
                start_board[count+1][ind] = BOX_S
                start_board[count+2][ind] = WALL
                occur +=1
            elif SPRITE_T in row and start_board[count+1][ind] == BOX_S and start_board[count+2][ind] == BOX_S:
                start_board[count][ind] = SPRITE_T
                start_board[count+1][ind] = BOX_S
                start_board[count+2][ind] = BOX_S
                occur +=1
            elif SPRITE_T in row and start_board[count+1][ind] == BOX_S and start_board[count+2][ind] == BOX_NS:
                start_board[count][ind] = SPRITE_T
                start_board[count+1][ind] = BOX_S
                start_board[count+2][ind] = BOX_NS
                occur +=1
            elif SPRITE_T in row and start_board[count+1][ind] == BOX_S and start_board[count+2][ind] == TARGET:
                start_board[count][ind] = TARGET
                start_board[count+1][ind] = SPRITE_T
                start_board[count+2][ind] = BOX_S
                occur +=1
            count+=1  

def move_d(ind):
    count = 0
    occur = 0
    for row in start_board:
        if occur != 1:
            if SPRITE in row and start_board[count][ind+1] == EMPTY:
                start_board[count][ind] = EMPTY
                start_board[count][ind+1] = SPRITE
                occur +=1
            elif SPRITE in row and start_board[count][ind+1] == WALL:
                start_board[count][ind] = SPRITE
                start_board[count][ind+1] = WALL
                occur +=1
            elif SPRITE in row and start_board[count][ind+1] == TARGET:
                start_board[count][ind] = EMPTY
                start_board[count][ind+1] = SPRITE_T
                occur +=1

            elif SPRITE in row and start_board[count][ind+1] == BOX_NS and start_board[count][ind+2] == EMPTY:
                start_board[count][ind] = EMPTY
                start_board[count][ind+1] = SPRITE
                start_board[count][ind+2] = BOX_NS
                occur +=1
            elif SPRITE in row and start_board[count][ind+1] == BOX_NS and start_board[count][ind+2] == WALL:
                start_board[count][ind] = SPRITE
                start_board[count][ind+1] = BOX_NS
                start_board[count][ind+2] = WALL
                occur +=1
            elif SPRITE in row and start_board[count][ind+1] == BOX_NS and start_board[count][ind+2] == BOX_S:
                start_board[count][ind] = SPRITE
                start_board[count][ind+1] = BOX_NS
                start_board[count][ind+2] = BOX_S
                occur +=1
            elif SPRITE in row and start_board[count][ind+1] == BOX_NS and start_board[count][ind+2] == BOX_NS:
                start_board[count][ind] = SPRITE
                start_board[count][ind+1] = BOX_NS
                start_board[count][ind+2] = BOX_NS
                occur +=1
            elif SPRITE in row and start_board[count][ind+1] == BOX_NS and start_board[count][ind+2] == TARGET:
                start_board[count][ind] = EMPTY
                start_board[count][ind+1] = SPRITE
                start_board[count][ind+2] = BOX_S
                occur +=1

            elif SPRITE in row and start_board[count][ind+1] == BOX_S and start_board[count][ind+2] == EMPTY:
                start_board[count][ind] = EMPTY
                start_board[count][ind+1] = SPRITE_T
                start_board[count][ind+2] = BOX_NS
                occur +=1
            elif SPRITE in row and start_board[count][ind+1] == BOX_S and start_board[count][ind+2] == WALL:
                start_board[count][ind] = SPRITE
                start_board[count][ind+1] = BOX_S
                start_board[count][ind+2] = WALL
                occur +=1
            elif SPRITE in row and start_board[count][ind+1] == BOX_S and start_board[count][ind+2] == BOX_S:
                start_board[count][ind] = SPRITE
                start_board[count][ind+1] = BOX_S
                start_board[count][ind+2] = BOX_S
                occur +=1
            elif SPRITE in row and start_board[count][ind+1] == BOX_S and start_board[count][ind+2] == BOX_NS:
                start_board[count][ind] = SPRITE
                start_board[count][ind+1] = BOX_S
                start_board[count][ind+2] = BOX_NS
                occur +=1
            elif SPRITE in row and start_board[count][ind+1] == BOX_S and start_board[count][ind+2] == TARGET:
                start_board[count][ind] = EMPTY
                start_board[count][ind+1] = SPRITE_T
                start_board[count][ind+2] = BOX_S
                occur +=1

            elif SPRITE_T in row and start_board[count][ind+1] == EMPTY:
                start_board[count][ind] = TARGET
                start_board[count][ind+1] = SPRITE  
                occur +=1  
            elif SPRITE_T in row and start_board[count][ind+1] == WALL:
                start_board[count][ind] = SPRITE_T
                start_board[count][ind+1] = WALL
                occur +=1
            elif SPRITE_T in row and start_board[count][ind+1] == TARGET:
                start_board[count][ind] = TARGET
                start_board[count][ind+1] = SPRITE_T
                occur +=1
            
            elif SPRITE_T in row and start_board[count][ind+1] == BOX_NS and start_board[count][ind+2] == EMPTY:
                start_board[count][ind] = TARGET
                start_board[count][ind+1] = SPRITE
                start_board[count][ind+2] = BOX_NS
                occur +=1
            elif SPRITE_T in row and start_board[count][ind+1] == BOX_NS and start_board[count][ind+2] == WALL:
                start_board[count][ind] = SPRITE_T
                start_board[count][ind+1] = BOX_NS
                start_board[count][ind+2] = WALL
                occur+=1
            elif SPRITE_T in row and start_board[count][ind+1] == BOX_NS and start_board[count][ind+2] == BOX_S:
                start_board[count][ind] = SPRITE_T
                start_board[count][ind+1] = BOX_NS
                start_board[count][ind+2] = BOX_S
                occur +=1
            elif SPRITE_T in row and start_board[count][ind+1] == BOX_NS and start_board[count][ind+2] == BOX_NS:
                start_board[count][ind] = SPRITE_T
                start_board[count][ind+1] = BOX_NS
                start_board[count][ind+2] = BOX_NS 
                occur +=1
            elif SPRITE_T in row and start_board[count][ind+1] == BOX_NS and start_board[count][ind+2] == TARGET:
                start_board[count][ind] = TARGET
                start_board[count][ind+1] = SPRITE
                start_board[count][ind+2] = BOX_S
                occur +=1
            
            elif SPRITE_T in row and start_board[count][ind+1] == BOX_S and start_board[count][ind+2] == EMPTY:
                start_board[count][ind] = TARGET
                start_board[count][ind+1] = SPRITE_T
                start_board[count][ind+2] = BOX_NS
                occur +=1
            elif SPRITE_T in row and start_board[count][ind+1] == BOX_S and start_board[count][ind+2] == WALL:
                start_board[count][ind] = SPRITE_T
                start_board[count][ind+1] = BOX_S
                start_board[count][ind+2] = WALL
                occur +=1
            elif SPRITE_T in row and start_board[count][ind+1] == BOX_S and start_board[count][ind+2] == BOX_S:
                start_board[count][ind] = SPRITE_T
                start_board[count][ind+1] = BOX_S
                start_board[count][ind+2] = BOX_S
                occur +=1
            elif SPRITE_T in row and start_board[count][ind+1] == BOX_S and start_board[count][ind+2] == BOX_NS:
                start_board[count][ind] = SPRITE_T
                start_board[count][ind+1] = BOX_S
                start_board[count][ind+2] = BOX_NS
                occur +=1
            elif SPRITE_T in row and start_board[count][ind+1] == BOX_S and start_board[count][ind+2] == TARGET:
                start_board[count][ind] = TARGET
                start_board[count][ind+1] = SPRITE_T
                start_board[count][ind+2] = BOX_S
                occur +=1
            count+=1

def reset(b):
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

    if num == 0:
        print("You Win!")
        break
    choice = str(input())
    print()

    while choice not in CONTROLS:
        choice = input("enter a valid move:\n")

    if choice in CONTROLS and choice == EMPTY:
        start_board = copy.deepcopy(board)
        continue
    elif choice in CONTROLS and choice == QUIT:
        print("Goodbye")
        break
    elif choice in CONTROLS and choice == 'w':
        move_w(index_sprite)
        continue
    elif choice in CONTROLS and choice == 'a':
        move_a(index_sprite)
        continue
    elif choice in CONTROLS and choice == 's':
        move_s(index_sprite)
        continue
    elif choice in CONTROLS and choice == 'd':
        move_d(index_sprite)
        continue
