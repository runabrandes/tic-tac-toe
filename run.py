import random
import time

# Title for game
print(
    r"""
  _____ _        _____            _____
 |_   _(_) ___  |_   _|_ _  ___  |_   _|__   ___
   | | | |/ __|   | |/ _` |/ __|   | |/ _ \ / _ \
   | | | | (__    | | (_| | (__    | | (_) |  __/
   |_| |_|\___|   |_|\__,_|\___|   |_|\___/ \___|

"""
)


# Greeting message to user

print("_________________________________\n")
print("Welcome to this Tic Tac Toe game!")
print("_________________________________\n")


def username_input():
    """
    Function to ask for username
    """
    while True:
        username = input("Please enter your name: \n").capitalize()
        if username == "":
            print("Input invalid.... Please enter a username!")
        elif not username.isalpha():
            print("Username can't contain numbers, please use letters only!")
        else:
            return username


time.sleep(1.0)


def game_rules():
    """
    Outlining the rules to the user
    """
    print(f"\nHello, {user}!\n")
    time.sleep(1.0)
    print("This Tic Tac Toe game is played by putting down X's and O's.\n")
    print(f"You will be PLAYER X, {user}!\n")
    print("Player O is a computer and will be your opponent.\n")
    time.sleep(5)
    print("You need to place the X symbol in an available game field (1-9)\n")
    print("The first user to have three X's or O's in a row wins!\n")
    print("This can be either horizontal, vertical or diagonal.\n")
    print("**The layout of the board is 1,2,3 in the top row,\n")
    print("4,5,6 in the middle and 7,8,9 in the bottom row.**\n")
    time.sleep(7)
    print("LET'S BEGIN!\n\n")


# Creating the tic tac toe board

board_positions = {
    "1": "-",
    "2": "-",
    "3": "-",
    "4": "-",
    "5": "-",
    "6": "-",
    "7": "-",
    "8": "-",
    "9": "-",
}


def print_game_board(board):
    """
    Function to print the board game and make it visible to user.
    Using dictionary keys and values from "board_positions".
    """
    print("")
    print(board["1"] + " | " + board["2"] + " | " + board["3"])
    print("--+---+--")
    print(board["4"] + " | " + board["5"] + " | " + board["6"])
    print("--+---+--")
    print(board["7"] + " | " + board["8"] + " | " + board["9"])
    print("")


def winning_combinations(board, recent_player):
    """
    Function to announce winner if correct combination made
    """
    # top row
    if (
        board["1"] == recent_player
        and board["2"] == recent_player
        and board["3"] == recent_player
    ):
        print(f"{recent_player} wins this round of Tic Tac Toe!")
        return True
    # middle row
    if (
        board["4"] == recent_player
        and board["5"] == recent_player
        and board["6"] == recent_player
    ):
        print(f"{recent_player} wins this round of Tic Tac Toe!")
        return True
    # bottom row
    if (
        board["7"] == recent_player
        and board["8"] == recent_player
        and board["9"] == recent_player
    ):
        print(f"{recent_player} wins this round of Tic Tac Toe!")
        return True
    # left column
    if (
        board["1"] == recent_player
        and board["4"] == recent_player
        and board["7"] == recent_player
    ):
        print(f"{recent_player} wins this round of Tic Tac Toe!")
        return True
    # middle column
    if (
        board["2"] == recent_player
        and board["5"] == recent_player
        and board["8"] == recent_player
    ):
        print(f"{recent_player} wins this round of Tic Tac Toe!")
        return True
    # right column
    if (
        board["3"] == recent_player
        and board["6"] == recent_player
        and board["9"] == recent_player
    ):
        print(f"{recent_player} wins this round of Tic Tac Toe!")
        return True
    # diagonal 1,5,9
    if (
        board["1"] == recent_player
        and board["5"] == recent_player
        and board["9"] == recent_player
    ):
        print(f"{recent_player} wins this round of Tic Tac Toe!")
        return True
    # diagonal 3,5,7
    if (
        board["3"] == recent_player
        and board["5"] == recent_player
        and board["7"] == recent_player
    ):
        print(f"{recent_player} wins this round of Tic Tac Toe!")
        return True

    return False


def check_if_occupied(board, recentTurn):
    """
    Function to check if the field the user chooses is still available
    """
    if board[recentTurn] != "-":
        return False
    return True


def board_full(board):
    """
    Function to check if the game board is full
    """
    for field in board:
        if board[field] == "-":
            return False
    return True


def reset_board(board):
    """
    Function to empty every field in board
    """
    for key in board:
        board[key] = "-"


user = username_input()
player = "X"
check_for_win = False


def run_game():
    """
    Main function to make the game run
    """
    global check_for_win
    global player
    global board_positions
    global user

    while check_for_win is False:
        if player == "X":
            while True:
                time.sleep(0.2)
                user_selection = input(
                    f"Your turn, {user}! Please enter a board position: \n"
                )
                if user_selection == "":
                    print("Input invalid.. Please enter a number between 1-9!")
                elif not user_selection.isnumeric():
                    print("The selection cannot contain letters!")
                elif not int(user_selection) in range(1, 10):
                    print("Please enter a number between 1 and 9!\n")
                else:
                    break

            if check_if_occupied(board_positions, user_selection) is False:
                print("This board position has already been chosen.\n")
                continue

            board_positions[user_selection] = player

        elif player == "O":
            print("Computer's move..!")
            # makes random selection for player O
            while player == "O":
                time.sleep(0.5)
                random_selection = str(random.randint(1, 9))
                if board_positions[random_selection] == "-":
                    board_positions[random_selection] = "O"
                    break
        time.sleep(1.5)
        print_game_board(board_positions)

        # game stops if check_for_win returns "winning_combinations is true"
        check_for_win = winning_combinations(board_positions, player)

        if board_full(board_positions) is True and check_for_win is False:
            print("This round is a TIE! Better luck next time..!\n")
            play_again()
            break

        if board_full(board_positions) is False and check_for_win is True:
            play_again()
            break

        if board_full(board_positions) is True and check_for_win is True:
            play_again()
            break

        # checks if player is X or O and swaps accordingly
        if player == "X":
            player = "O"
        elif player == "O":
            player = "X"


def play_again():
    """
    Function to ask user if they would like to restart the game
    """
    global player
    global check_for_win

    while True:
        try:
            print("Are you up for another round of Tic Tac Toe?")
            user_reply = input("Type 'y' for yes or 'n' for no!: \n").lower()
        except ValueError:
            print("Invalid input... Please try again!\n")
            continue
        if user_reply != "y" and user_reply != "n":
            print("Invalid input... Please use y for yes or n for no!\n")
            continue
        elif user_reply == "y":
            player = "X"
            reset_board(board_positions)
            check_for_win = False
            run_game()
        elif user_reply == "n":
            print("Thanks for playing! See you next time")
            break
        return


game_rules()
run_game()
