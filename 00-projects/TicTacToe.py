#----Global Variables----

#Drawing the board..
board = [
        '-', '-', '-',
        '-', '-', '-',
        '-', '-', '-',
        ]

#who wins 
winner = None

#First player starts
current_player = "X"

#While the game in progress 
game_progress = True

#Run the game
def play_game():


    display_board()
    #While game is still going
    while game_progress:

        #make current_player global to write to it 
        global current_player

        #take input from current player
        handle_turn(current_player)

        #Check if someone win or a tie!
        winner = check_game()

        #change turns
        current_player = flip_player(current_player)

    if winner == "X" or winner == "O":
        print(winner + " won!")

    else:
        print("Tie!")

def display_board():

    print(" | " + board[0] + ' | ' + board[1] + " | " + board[2] + " | ")
    print(" | " + board[3] + ' | ' + board[4] + " | " + board[5] + " | ")
    print(" | " + board[6] + ' | ' + board[7] + " | " + board[8] + " | ")

#takes input from the player whatever X or O and putting it on the board
def handle_turn(player):

    position = input("Enter position from 1-9: ")
    position = int(position) - 1 

    if board[position] == '-':
        board[position] = player
        display_board()

    else:
        print("You can't go there, try again!")

        display_board()

        handle_turn(player)
    # display_board()

#check if the game is over or not 
def check_game():

    winner = check_win()

    check_tie()

    return winner
#check if someone win
def check_win():

    global winner

    winner = check_rows()

    winner = check_columns()

    winner = check_diagnols()

    return winner

def check_rows():

    global winner,game_progress

    if board[0] == board[1] == board[2] == "X" or board[0] == board[1] == board[2] == "O":
        winner = board[0]
        game_progress = False

    elif board[3] == board[4] == board[5] == "X" or board[3] == board[4] == board[5] == "O":
        winner = board[3]
        game_progress = False

    elif board[6] == board[7] == board[8] == "X" or board[6] == board[7] == board[8] == "O":
        winner = board[6]
        game_progress = False

    return winner

def check_columns():

    global winner,game_progress

    if board[0] == board[3] == board[6] == "X" or board[0] == board[3] == board[6] == "O":
        winner = board[0]
        game_progress = False

    elif board[1] == board[4] == board[7] == "X" or board[1] == board[4] == board[7] == "O":
        winner = board[1]
        game_progress = False

    elif board[2] == board[5] == board[8] == "X" or board[2] == board[5] == board[8] == "O":
        winner = board[2]
        game_progress = False

    return winner

def check_diagnols():

    global winner,game_progress

    if board[0] == board[4] == board[8] == "X" or board[0] == board[4] == board[8] == "O":
        winner = board[0]
        game_progress = False

    elif board[2] == board[4] == board[6] == "X" or board[2] == board[4] == board[6] == "O":
        winner = board[2]
        game_progress = False

    return winner


def check_tie():
    global game_progress
    if "-" not in board and winner == None:
        game_progress = False

def flip_player(current):

    if current == "X":
        current = "O"

    else:
        current = "X"

    return current


if __name__ == "__main__":
    play_game()
