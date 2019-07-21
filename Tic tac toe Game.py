from IPython.display import clear_output


# Board is taken as a list
# This will display the board
def display_board(board):
    #This will clear the output each time so previous result not shown
    clear_output()  

    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
	


# Give player the option to choose the 'X' or 'O' 	
def player_input():
    marker = '' 
    while not (marker == 'X' or marker == 'O'):
        # .upper() will upper case the letter if small typed 
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        # this is a tuple of (Player 1, Player 2)
        return ('X', 'O')
    else:
        return ('O', 'X')



# this is used to place the marker at desired position
def place_marker(board, marker, position):
    board[position] = marker



# this will check the Player is wins or not
# Numbering equivalent to keyboard layout , you can choose any layout
# You can't take board[x]==board[x+1]==board[x+2] because it also accepts the empty string
def win_check(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal



# Import random for which Player go first
import random

def choose_first():
    # It is equivalent to flip of a coin
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'



# This checks the space available
def space_check(board, position):
    # this return the boolean True or False
    return board[position] == ' '



# This checks full board for free space available
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            # If space available than full_board_check returns False
            return False  
    return True
	
	
	
# This function checks whether Player move is appropriate or not  
def player_choice(board):
    position = 0
    # 1st- It keeps looping if anything other than number is entered
    # 2nd- It checks space available or not
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))   
    return position
	
	

# Player wants to play again or not	
def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')



# This is main part coding of game
print('Welcome to Tic Tac Toe!')
while True:
    # Reset the board
    # It will create all empty spaces 
    theBoard = [' '] * 10
    # Player 1 or Player 2 got opposite markers
    player1_marker, player2_marker = player_input()
    # choose_first() randomly choose the player option
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                # Because game is end
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break	
	
