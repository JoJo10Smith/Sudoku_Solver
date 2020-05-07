#You will need the numpy library to run this program
import numpy as np 
from math import sqrt

"""
STEP 1: Change the "LENGTH_OF_BLOCK" variable to be equal to the length of EACH individual block,
        in 'normal' 9 by 9 each block is 3 units long
STEP 2: Change the "LOOP_MAX" variable to any number that you feel is withing the range of how long the program should run
        most boards can be done in  < 5 loops. This will also stop the program if the board cannot be done
STEP 3: Change the "CURRENT_VALID_NUMBERS" variable to be a list of all the numbers that can be played in the game. On a 9 * 9 sudoku
        grid it is the numbers from 1 to 9 inclusive
STPE 4: Change the "grid_inputs" variable to be equal to your sudoku board with 0 being empty spots and the other umbers being the 
        corresponding numbers on the board. The example board is the first board on: https://dingo.sbs.arizona.edu/~sandiway/sudoku/examples.html
"""
LENGTH_OF_BLOCK = 3
lOOP_MAX = 50
CURRENT_VALID_NUMBERS = [1,2,3,4,5,6,7,8,9]

grid_inputs = [
[0,0,0,2,6,0,7,0,1],
[6,8,0,0,7,0,0,9,0],
[1,9,0,0,0,4,5,0,0],
[8,2,0,1,0,0,0,4,0],
[0,0,4,6,0,2,9,0,0],
[0,5,0,0,0,3,0,2,8],
[0,0,9,3,0,0,0,7,4],
[0,4,0,0,5,0,0,3,6],
[7,0,3,0,1,8,0,0,0]
]

#DONT CHANGE THE CODE BELOW

#This prints the board in a grid format that is easy for th euser to interpret
SUDOKU = np.array(grid_inputs)
print("Unsolved board")
print (SUDOKU)

#function that checks what number can be played at each position of the board and return a list of possible numbers
def valid_number(x_pos,y_pos,board,local_current_valid_numbers):
  if board[x_pos][y_pos] == 0:
    current_valid_numbers = list(local_current_valid_numbers)
    #CHECK FOR THE SAME NUMBER IN ROWS
    for row in range(len(board)):
      if board[x_pos][row] in current_valid_numbers:
        current_valid_numbers.remove(board[x_pos][row])
    #CHECK FOR THE SAME NUMBER IN COLUMNS
    for column in range(len(board[0])):
      if board[column][y_pos] in current_valid_numbers:
        current_valid_numbers.remove(board[column][y_pos])
    #CHECK FOR THE SAME NUMBER IN THE CURRENT BLOCK
    range_to_check = [x_pos//LENGTH_OF_BLOCK,y_pos//LENGTH_OF_BLOCK]
    for row in range(range_to_check[0]*LENGTH_OF_BLOCK, range_to_check[0]*LENGTH_OF_BLOCK+LENGTH_OF_BLOCK):
      for column in range(range_to_check[1]*LENGTH_OF_BLOCK, range_to_check[1]*LENGTH_OF_BLOCK+LENGTH_OF_BLOCK):
        if board[row][column] in current_valid_numbers:
          current_valid_numbers.remove(board[row][column])

    return current_valid_numbers

#function that check if the board is completely full
def check_if_done(board):
  for row in range(len(board)):
    for column in range(len(board[0])):
      if board[row][column] == 0:
        return False
  return True

#initialize the 'current loop' and 'done' variable
current_loop = 0
done = check_if_done(grid_inputs)

#the actual program that calls the 'valid number' function for each position of the board that is empty
while check_if_done(grid_inputs) == False and current_loop < lOOP_MAX:
  current_loop += 1
  for row in range(len(grid_inputs)):
    for column in range(len(grid_inputs[0])):
      if grid_inputs[row][column] == 0:
        possible_answers = valid_number(row,column,grid_inputs,CURRENT_VALID_NUMBERS)
        if len(possible_answers) == 1:
          grid_inputs[row][column] = possible_answers[0]
  done = check_if_done(grid_inputs)

#when the loop ends, print the board
if current_loop == lOOP_MAX:
  print ("ERROR: could not be solved within loop max")
  SOLVED_SUDOKU = np.array(grid_inputs)
  print("unsolved board after loop:")
  print (SOLVED_SUDOKU)
else:
  SOLVED_SUDOKU = np.array(grid_inputs)
  print("Solved board in: "+str(current_loop)+ " loops")
  print (SOLVED_SUDOKU)