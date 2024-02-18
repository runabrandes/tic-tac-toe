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

