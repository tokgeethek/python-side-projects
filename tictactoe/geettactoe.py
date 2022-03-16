
board = list(range(0,10))
player_1_turn = True
turns_left = 9
player = 1
player_1_wins = 0
player_2_wins = 0
game_count = 0
draws = 0

# resets the game
def new_game():
    global board, turns_left
    board = list(range(0,10))
    turns_left = 9

# asks for input
def update_board():
    ans = input(f"Player {player}, please choose a position from 1-9:")
    if int(ans.isdigit()) and int(ans) in range(1,10):
        if board[int(ans)] == "X" or board[int(ans)] == "O":
            print("This spot is filled, please pick another number")
            display_board()
            print(" ")
        else:
            position = int(ans)
            update_position(position)
            display_board()
    else: 
        print("Please input a valid number from 1-9")
        print(" ")

# updates board and changes turn
def update_position(position):
    global player_1_turn,player,turns_left
    if player_1_turn:
        board[position] = "X"
        player_1_turn = False
        player = player + 1
        turns_left = turns_left -1
    else:
        board[position] = "O"
        player_1_turn = True
        player = player - 1
        turns_left = turns_left -1

# show current board
def display_board():
    print(str(board[1]) + "|" + str(board[2]) + "|" + str(board[3]))
    print("-" + " " + "-" + " " + "-")
    print(str(board[4]) + "|" + str(board[5]) + "|" + str(board[6]))
    print("-" + " " + "-" + " " + "-")
    print(str(board[7]) + "|" + str(board[8]) + "|" + str(board[9]))
    print(" ")

# start the game
def start_game():
    print("Let's play sum tic tac toe")
    new_game()

def check_won():
    return (board[1] == board[2] == board[3]) or (board[4] == board[5] == board[6]) or (board[7] == board[8] == board[9]) or (board[1] == board[4] == board[7]) or (board[2] == board[5] == board[8]) or (board[3] == board[6] == board[9]) or (board[1] == board[5] == board[9]) or (board[3] == board[5] == board[7])

def has_won():
    global player_1_wins,player_2_wins
    if check_won():
        if player_1_turn:
            # because we reverse the roles after each input
            print("Congrats Player 2!")
            player_2_wins += 1
            return True
        else:
            print("Congrats Player 1!")
            player_1_wins += 1
            return True

def play_again():
    if game_count != 0:
        print("Play again?")
        y = 0
        while y == 0:
            x = input("Y/N").lower()
            if x == "y":
                print (f"Game {game_count}.\n Player 1 win count: {player_1_wins} | Player 2 win count: {player_2_wins} | Draws: {draws}")
                print(" ")
                return True
            elif x == "n":
                print("Thanks for playing!")
                break
            else:
                print("Invalid response, please type Y/N only")
                print(" ")


def game():
    global game_count,draws
    while not has_won():
        if turns_left >0:
            update_board()
        else:
            print("It's a draw~")
            game_count = game_count +1
            draws = draws +1 
            print (f"Game {game_count}.\n Player 1 win count: {player_1_wins} | Player 2 win count: {player_2_wins} | Draws: {draws}")
            print(" ")
            break
    else:
        game_count = game_count +1
        print (f"Game {game_count}.\n Player 1 win count: {player_1_wins} | Player 2 win count: {player_2_wins} | Draws: {draws}")
        print(" ")

# game starts here
start_game()
game()
while play_again():
    start_game()
    game()





