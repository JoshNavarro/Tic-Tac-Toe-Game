# Creator	: Joshua Navarro
# Date		: 02/12/2019

# This will be the Tic-Tac-Toe Game
# Still learning OOP with Python

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
	while player1 != 'X' and player1 != 'x' and player1 != 'O' and player1 != 'o':
		player1 = input("Please pick a valid marker 'X' or 'O' : ")

	return player1.upper()

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
	win_list = [[board[7],board[5],board[3]],
	[board[1],board[5],board[9]],
	[board[7],board[8],board[9]],
	[board[4],board[5],board[6]],
	[board[1],board[2],board[3]],
	[board[7],board[4],board[1]],
	[board[8],board[5],board[2]],
	[board[9],board[6],board[3]]]

	# Determine if there is a winner of the game
	if x_win in win_list:
		return True, 'X'
	elif o_win in win_list:
		return True, 'O'
	else:
		return False, ''

def choose_move(board):
	position = 0
	while position not in range(1,10) or board[position] in ('X','O'):
		position = int(input('Choose your next position: (1-9) '))
	return position

def full_board(board):
	return not ' ' in board

def replay():
	# Let players decide if they want to play again
	play = input('Do you want to play again? Enter Yes or No: ')

	# Check for a valid answer
	while play.lower() != 'yes' and play.lower() != 'no':
		play = input('Do you want to play again? Enter Yes or No: ')

	# Return players' choice
	return play.lower() == 'yes'

#################################################################################

# main program
while True:
	print('Welcome to my Tic-Tac-Toe game!')

	# Allow first player to decide which marker they want
	player1 = select_marker()

	# Assign other marker to second player
	if player1 == 'X':
		player2 = 'O'
	else:
		player2 = 'X'

	#rand_player()

	# Initial game setup
	win = False
	marker_count = 0
	test_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
	display_board(test_board)

	# Playing the game
	while not win:

		# Let player choose move
		position = choose_move(test_board)

		# Fill the board with alternating X and O at player's choice of position
		if marker_count%2 == 0:
			test_board = place_marker(test_board, player1, position)
		else:
			test_board = place_marker(test_board, player2, position)

		# Check if anyone has won the game
		win, who_win = check_win(test_board)

		# Alternate the marker counter
		marker_count += 1

		# Display board every turn
		display_board(test_board)

		# End game if board is full
		if full_board(test_board):
			break

	# Tell players who has won the game
	if win:
		print(f'Congratulations! {who_win} has won the game!')
	else:
		print('No one has won.')

	# End game or replay
	if not replay():
		break
print('Thank you for playing!')

#################################################################################