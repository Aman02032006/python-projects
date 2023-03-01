import math
import random

# Defining the initial state of the game board
Game_Board = ['_', '_', '_',
              '_', '_', '_',
              '_', '_', '_',]

# function that prints the game board

def boardprint(board):
    print(f'| {board[0]} | {board[1]} | {board[2]} |')
    print(f'| {board[3]} | {board[4]} | {board[5]} |')
    print(f'| {board[6]} | {board[7]} | {board[8]} |')

# | 0 | 1 | 2 |
# | 3 | 4 | 5 |
# | 6 | 7 | 8 |

# Function to check whether there is a winner on the board using the normal conditions of TicTacToe. Returns true if
# there is a winner

def win(board):

    # Condition for horizontal lines

    if board[0] == board[1] and board[1] == board[2] and board[2] != '_':
        return True
    elif board[3] == board[4] and board[4] == board[5] and board[5] != '_':
        return True
    elif board[6] == board[7] and board[7] == board[8] and board[8] != '_':
        return True

    # condition for vertical lines

    elif board[0] == board[3] and board[3] == board[6] and board[6] != '_':
        return True
    elif board[1] == board[4] and board[4] == board[7] and board[7] != '_':
        return True
    elif board[2] == board[5] and board[5] == board[8] and board[8] != '_':
        return True

    # Condition for diagnols

    elif board[0] == board[4] and board[4] == board[8] and board[8] != '_':
        return True
    elif board[2] == board[4] and board[4] == board[6] and board[6] != '_':
        return True

    else:
        return False

# Function for PvP Game mode

def PvPGame(board):

    # Instructions to the user

    print('Grid is of the format : ')
    print(' ')
    print('''| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |''')

    gameRunning = True
    index = list(range(0,9)) # a list of the indexes of available positions on the game board
    print(' ')

    p1 = input("Player 1 wants X or O : ").upper()
    if p1=='X':
        p2 = 'O'
    else:
        p2 = 'X'

    # Loop which iterates until the game runs
    while gameRunning:

        inp = '' # variable to store 'fine' if the index entered by the user is available on the Game Board
        # This iterates till the user enters a valid index
        while inp != 'fine':
            X = int(input('Player 1 go : '))

            if X-1 in index:
                inp = 'fine'
                board[X-1] = p1 # this statement replaces the '_' with either X or O depending upon the choice made
                # earlier by the user
                index.remove(X-1) # this statement removes the used index from the index list
                boardprint(board)
            else:
                print('That space is already occupied!!...You can not enter there!')
        # Condtition for a win on the board
        if win(board):
            print('Player 1 wins!!')
            gameRunning = False
            break
        if len(index) == 0: # This condition will come true if the index list becomes empty i.e. all the places in the
            # board are used up
            break

        # Player 2's turn. Same logic
        print(' ')
        inp = ''
        while inp != 'fine':
            O = int(input("Player 2 go : "))
            if O-1 in index:
                inp = 'fine'
                board[O-1] = p2
                index.remove(O-1)
                boardprint(board)
            else:
                print('That space is already occupied!!...You can not enter there!')
        if win(board):
            print('Player 2 wins!!')
            gameRunning = False
            break
        if len(index) == 0:
            break
        print(' ')

    # If the entire loop runs without breaking then this condition will get applied
    else:
        print("It's a tie")

# Function for Computer vs Player mode. Same logic for player's input

def CvPGame(board):
    print('Grid is of the format : ')
    print(' ')
    print('''| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |''')
    gameRunning = True
    index = list(range(0, 9))
    print(' ')
    p = input("Player wants X or O : ").upper()
    if p == 'X':
        c = 'O'
    else:
        c = 'X'

    while gameRunning:
        inp = ''
        while inp != 'fine':
            X = int(input('Player go : '))
            if X - 1 in index:
                inp = 'fine'
                board[X - 1] = p
                index.remove(X - 1)
                boardprint(board)
                print(' ')
            else:
                print('That space is already occupied!!...You can not enter there!')
        if win(board):
            print('Player won!!')
            gameRunning = False
            break
        if len(index) == 0:
            break

        # Computer's turn. Computer selects randomly from the index list so it cannot choose something that is not in the index.
        # So no need to check its input
        print("Computer's turn")
        print(' ')
        O = random.choice(index)
        board[O] = c
        index.remove(O)
        boardprint(board)
        if win(board):
            print('Computer wins!!')
            gameRunning = False
            break
        if len(index) == 0:
            break
        print(' ')

    else:
        print("It's a tie")


game_mode = input('Do you want to play vs another player(PvP) or vs computer(CvP) : ')
if game_mode.lower() == 'pvp':
    PvPGame(Game_Board)
elif game_mode.lower() == 'cvp':
    CvPGame(Game_Board)
else:
    print('Invalid Input')
