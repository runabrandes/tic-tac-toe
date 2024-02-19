import random

"""
Greeting message to user 
"""
print("_________________________________\n")
print("Welcome to this Tic Tac Toe game!")
print("_________________________________\n")

def username_input():
    username = input("Please enter your name: \n")
    if username == "":
        print ("Input invalid.... Please enter a username!")
    elif not username.isalpha():
        print("The username cannot contain numbers, please use letters only!")
    #else:

    return username

"""
Outlining the rules to the user
"""
def gameRules():
    print(f"\nHello {user}!\n")
    print("This Tic Tac Toe game is played by putting down X's and O's.\n")
    print("Users take turns putting down their symbol in one of the board fields (1-9)\n")
    print("The first user to have three X's or O's in a row wins!\n")
    print("This can be either horizontal, vertical or diagonal.\n")
    print("**The layout of the board is 1,2,3 in the top row,\n")
    print("4,5,6 in the middle and 7,8,9 in the bottom row.**\n")
    print("LET'S BEGIN!\n\n")

"""
Creating a tic tac toe board.
"""

boardPositions = {
    '1': '-',
    '2': '-',
    '3': '-',
    '4': '-',
    '5': '-',
    '6': '-',
    '7': '-',
    '8': '-',
    '9': '-',
}

"""
Function to print the board game and make it visible to user.
Using dictionary keys and values from "boardPositions".
"""

def printGameBoard(board):
    print(board['1'] + ' | ' + board['2'] + ' | ' + board['3'])
    print("--+---+--")
    print(board['4'] + ' | ' + board['5'] + ' | ' + board['6'])
    print("--+---+--")
    print(board['7'] + ' | ' + board['8'] + ' | ' + board['9'])

#012,036,048,147,246,345,258,678
def winningCombinations(board, recentPlayer):
    #top row
    if board['1'] == recentPlayer and board['2'] == recentPlayer and board['3'] == recentPlayer:
        print(f'{recentPlayer} wins this round of Tic Tac Toe!')
        return True
    #middle row
    if board['4'] == recentPlayer and board['5'] == recentPlayer and board['6'] == recentPlayer:
        print(f'{recentPlayer} wins this round of Tic Tac Toe!')
        return True
    #bottom row
    if board['7'] == recentPlayer and board['8'] == recentPlayer and board['9'] == recentPlayer:
        print(f'{recentPlayer} wins this round of Tic Tac Toe!')
        return True

    return False


checkForWin = False


user = username_input()

gameRules()

player = "X"

while checkForWin == False:
    userSelection = input(f'Your turn! Please enter a board position:')
    boardPositions[userSelection] = player
    printGameBoard(boardPositions)
    winningCombinations(boardPositions, player)

#def playerInput():



printGameBoard(boardPositions)
