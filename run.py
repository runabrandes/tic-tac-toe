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
    else:
        #break
        return username

"""
Outlining the rules to the user
"""
print("This Tic Tac Toe game is played by putting down X's and O's.\n")
print("Users take turns putting down their symbol in one of the board fields (1-9)\n")
print("The first user to have three X's or O's in a row wins!\n")
print("This can be either horizontal, vertical or diagonal.\n")
print("LET'S BEGIN!\n\n")

"""
Creating a tic tac toe board.
"""

boardPositions = {
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
}

"""
Function to print the board game and make it visible to user.
Using dictionary keys and values from "boardPositions".
"""

def printGameBoard(board):
    print("--+---+--")
    print(board['1'] + ' | ' + board['2'] + ' | ' + board['3'])
    print("--+---+--")
    print(board['4'] + ' | ' + board['5'] + ' | ' + board['6'])
    print("--+---+--")
    print(board['7'] + ' | ' + board['8'] + ' | ' + board['9'])
    print("--+---+--")


player1 == "X"
player2 == "O"

#def userMoveInput():
    


#def winningCombinations():
#012,036,048,147,246,345,258,678

username_input()
printGameBoard(boardPositions)
