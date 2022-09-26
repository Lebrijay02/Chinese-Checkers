#Juan Ignacio Lebrija    A01721659   Oct 2021
#   The porpuse of this program is to first, generate a 6x6 board with two letter A's on the positions 2,0 and 3,0
#   and then generate 6 *'s across the board but not on the exterior lines and columns.
import random
from random import randrange

def generate_board():
    '''this function generates the board with the random *'s scattered across the board but not on the exterior lines and columns aswell as two A's on the positions 2,0 and 3,0.'''
    board=[["-","-","-","-","-","-"],["-","-","-","-","-","-"],["A","-","-","-","-","-"],["A","-","-","-","-","-"],["-","-","-","-","-","-"],["-","-","-","-","-","-"]]
    cont=0
    while(6>cont):
        col=random.randrange(1,5)
        row=random.randrange(1,5)
        if board[row][col]!= "*":
            board[row][col]= "*"
            cont +=1
    return board

def print_board(board):
    '''at the end of each round, after the board has been modified, this function prints the resulting board.'''
    print("  0 1 2 3 4 5")
    cont=0
    for i in range(len(board)):
        print(cont, end=" ")
        cont += 1
        for j in range(len(board[i])):
            print(board[i][j], end=" ")
        print()
        
def turn(board):
    '''this function plays out the rest of the turn. This includes the inputs of the current position of the A the player wishes to
    move aswell as the direction of which the A will move.'''
    v_row = 0
    v_col = 0
    while v_row !=1 or v_col !=1:
        v_row = 0
        v_col = 0
        row=int(input("Row: "))
        column=int(input("Column: "))
        if row < 0 or row > 5:
            print("Row is invalid")
        else:
            v_row += 1
        
        if column < 0 or column > 5:
            print("Column is invalid")
        else:
            v_col += 1
            
        if v_row ==1 and v_col ==1:
            if board[row][column]!= "A":
                print("There is not an A on those coordinates")
                v_row = 0
                v_col = 0
    
    direction = "a"
    while direction != "e" and direction != "d" and direction != "x":
        print("Where to move?")
        print("e - up ; d - forward ; x - downward")
        direction = input()
    
        if direction == "e" and row-1 >= 0 and board[row-1][column+1]!= "*":
            board[row-1][column+1]= "A"
            board[row][column]="-"
        elif direction == "d" and board[row][column+1]!= "*": 
            board[row][column+1]= "A"
            board[row][column]="-"
        elif direction == "x" and row+1 <= 5 and board[row+1][column+1]!= "*": 
            board[row+1][column+1]= "A"
            board[row][column]="-"
        else:
            print("There is a * in that position")
            direction="a"
        
    return board

def game_over(board):
    '''after the turn has ended, this function checks if the player has reached the end of the board.'''
    conti=0
    for val in range(6):
        if board[val][5]=="A":
            conti += 1  
    return conti
    
def main():
    '''this function is where all of the other functions come together. It first generates the board, displays it and then as long as the game
    has not ended, the game will loop until the game has ended by the player deciding not to play or the game ending in a win.'''
    board = generate_board()
    print_board(board)
    play="s"
    conti=0
    while play=="s"and conti != 1:
        turn(board)
        print_board(board)
        conti = game_over(board)
        if conti == 0:
            play = input("Would you like to continue playing?: ")
            while play != "s" and play != "n":
                play=input("Would you like to continue playing?: ")
        if conti == 1:
            print("You Won!!!")
main()