import random

"""
Greeting message to user 
"""
print("_________________________________\n")
print("Welcome to this Tic Tac Toe game!")
print("_________________________________\n")

"""
Function to ask for username
"""

def username_input():
    while True:
        username = input("Please enter your name: \n")
        if username == "":
            print ("Input invalid.... Please enter a username!")
        elif not username.isalpha():
            print("The username cannot contain numbers, please use letters only!")
        else:
            return username
        

"""
Outlining the rules to the user
"""
def gameRules():
    print(f"\nHello, {user}!\n")
    print("This Tic Tac Toe game is played by putting down X's and O's.\n")
    print(f"You will be PLAYER X, {user}!\n")
    print("Player O is a computer and will be your opponent.\n")
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
    #left column
    if board['1'] == recentPlayer and board['4'] == recentPlayer and board['7'] == recentPlayer:
        print(f'{recentPlayer} wins this round of Tic Tac Toe!')
        return True
    #middle column
    if board['2'] == recentPlayer and board['5'] == recentPlayer and board['8'] == recentPlayer:
        print(f'{recentPlayer} wins this round of Tic Tac Toe!')
        return True
    #right column
    if board['3'] == recentPlayer and board['6'] == recentPlayer and board['9'] == recentPlayer:
        print(f'{recentPlayer} wins this round of Tic Tac Toe!')
        return True
    #diagonal 1,5,9
    if board['1'] == recentPlayer and board['5'] == recentPlayer and board['9'] == recentPlayer:
        print(f'{recentPlayer} wins this round of Tic Tac Toe!')
        return True
    #diagonal 3,5,7
    if board['3'] == recentPlayer and board['5'] == recentPlayer and board['7'] == recentPlayer:
        print(f'{recentPlayer} wins this round of Tic Tac Toe!')
        return True

    return False


"""
Function to check if the field the user chooses is still available
"""
def checkIfOccupied(board, recentTurn):
    if board[recentTurn] != '-':
        return False
    return True

"""
Function to check if the game board is full
"""
def boardFull(board):
    for field in board:
        if board[field] == '-':
            return False
    return True

"""
Function to empty every field in board
"""
def resetBoard(board):
    for key in board:
        board[key] = '-'


user = username_input()
player = "X"
checkForWin = False

def runGame():
    global checkForWin
    global player
    global boardPositions
    
    while checkForWin == False:
        if player == "X":
            while True:
                userSelection = input(f'Your turn {player}! Please enter a board position: \n')
                if userSelection == "":
                    print ("Input invalid.... Please enter a number between 1-9!")
                elif not userSelection.isnumeric():
                    print("The selection cannot contain letters, please use numbers 1-9 only!")
                elif not int(userSelection) in range(1,10):
                    print("Please enter a number between 1 and 9!\n")
                else:
                    break

            if checkIfOccupied(boardPositions, userSelection) == False:
                print('This board position has already been chosen.\n')
                continue

            boardPositions[userSelection] = player

        elif player == 'O':
            #makes random selection for player O
            while player == 'O':
                print("Computer's move..! \n")
                randomSelection = str(random.randint(1, 9))
                if boardPositions[randomSelection] == '-':
                    boardPositions[randomSelection] = 'O'
                    break
        
        printGameBoard(boardPositions)

        #game will stop if checkForWin returns true based on winningCombinations
        checkForWin = winningCombinations(boardPositions, player)

        if boardFull(boardPositions) == True and checkForWin == False:
            print('This round is a TIE! Better luck next time..!\n')
            playAgain()
            break

        if boardFull(boardPositions) == False and checkForWin == True:
            playAgain()
            break

        if boardFull(boardPositions) == True and checkForWin == True:
            playAgain()
            break

        #swapping X and O - checks if player is X or O and swaps accordingly after checkForWin ran
        if player == 'X':
            player = 'O'
        elif player == 'O':
            player = 'X'
            

"""
Function to ask user if they would like to restart the game
"""
def playAgain():
    global player
    global checkForWin
    
    while True:
        try:
            print("Are you up for another round of Tic Tac Toe?")
            userReply = input("Type 'y' for yes or 'n' for no!: \n")
        except ValueError:
            print("Invalid input... Please try again!\n")
            continue
        if userReply != "y" and userReply != "n":
            print("Invalid input... Please try again using y for yes or n for no!")
            continue
        elif userReply == "y":
            player ="X"
            resetBoard(boardPositions)
            checkForWin = False
            runGame()
        elif userReply == "n":
            print("Thanks for playing! See you next time")
            break
        return

gameRules()
runGame() 