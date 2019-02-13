# Creator	: Joshua Navarro
# Date		: 02/12/2019

# This will be the Tic-Tac-Toe Game
# Still learning OOP with Python

#from IPython.display import clear_output
#import time
from random import randint

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

def select_marker():
	player1 = input("Player 1: Do you want to be 'X' or 'O' : ")

	# Check if user selection is valid
	while player1 != 'X' and player1 != 'O':
		player1 = input("Please pick a valid marker 'X' or 'O' : ")

	return player1

def place_marker(board, marker, position):
	# Place the marker at position on the board
	board[position] = marker
	return board

def rand_player():
	# Randomize which player will go first
	turn = randint(0,100)

	# Even number will let player 1 go first
	if turn%2 == 0:
		print('Player 1 will go first.')
	# Odd number will let player 2 go first
	else:
		print('Player 2 will go first.')

def check_win(board):
	# Create winning set possibilities
	x_win = ['X','X','X']
	o_win = ['O','O','O']

	# Create winning possibilities on board -- total 8
	win_list = [[board[7],board[5],board[3]],[board[1],board[5],board[9]],
	[board[7],board[8],board[9]],[board[4],board[5],board[6]],[board[1],board[2],board[3]],
	[board[7],board[4],board[1]],[board[8],board[5],board[2]],[board[9],board[6],board[3]]]

	# Determine if there is a winner of the game
	if x_win in win_list:
		return True, 'X'
	elif o_win in win_list:
		return True, 'O'
	else:
		return False, ''



print('Welcome to my Tic-Tac-Toe game!')
player1 = select_marker()
print(f'Player 1 has selected : {player1}')
rand_player()
#test_board = ['#','X','O','X','O','X','O','X','O','X']
test_board = ['#','X','O',' ',' ','O',' ',' ','O','X']
display_board(test_board)
win, who_win = check_win(test_board)
if win:
	print(f'{who_win} has won!')
else:
	print('No one has won.')
#test_board = place_marker(test_board, '$', 8)
#display_board(test_board)
