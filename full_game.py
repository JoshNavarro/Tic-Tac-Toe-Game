# Creator	: Joshua Navarro
# Date		: 02/12/2019

# This will be the Tic-Tac-Toe Game
# Still learning OOP with Python

#from IPython.display import clear_output
#import time

'''
print('Welcome to my Tic-Tac-Toe game!')
play_game = input('Would you like to play? (Yes or No)')
if play_game == 'Yes':
	print(':)')
else:
	print(':(')

player1 = input("Please pick a marker 'X' or 'O' : ")
'''

def display_board(board):
	# Clear the screen so that it can be printed again
	print('\n'*15)

	# Create the board patterns
	board_patterns = [ '   |   |   ','-----------', 
	f' {board[7]} | {board[8]} | {board[9]} ',
	f' {board[4]} | {board[5]} | {board[6]} ',
	f' {board[1]} | {board[2]} | {board[3]} ',
	]

	# Print the board
	print(board_patterns[0] + '\n' + board_patterns[2] + '\n' + board_patterns[0] + '\n' + board_patterns[1])
	print(board_patterns[0] + '\n' + board_patterns[3] + '\n' + board_patterns[0] + '\n' + board_patterns[1])
	print(board_patterns[0] + '\n' + board_patterns[4] + '\n' + board_patterns[0])


test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)