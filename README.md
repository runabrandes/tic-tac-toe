# PORTFOLIO PROJECT 3

# Tic Tac Toe

Tic Tac Toe is a game in which two players take turns in drawing either an 'O' or an 'X' in one square of a grid
consisting of nine squares. The winner is the first player to get three of the same symbols in a row.
This can be up, down, across or diagonally.
If neither player gets three symbols into a row but the game board is full, the game ends in a tie.
In this game the user is player X and plays against a computer, player O.

![Final project image](assets/images/AmIResponsive.png) [Am I Responsive](https://amiresponsive.co.uk/)

#

## PROJECT IDEA

My initial idea for this project was to build a simple and easy to undertsnad Tic Tac Toe game that the user can play against a computer.

The features I wanted the game to have are:

- Game navigations and controls are easy to understand
- Name input to make the experience more personal
- Rules explained so they are easy to follow
- Game gives feedback dependig on user input
- Computer opponent which the user plays against

#

## Flowchart

Insert when ready

#

## UX/UI

- The game is simple to understand and fun for users of different age groups
- The game is explained so the user can play the game without any troubles
- The game has been designed so it is easy to play

#

## USER STORIES

1. As a user, I want to be able to add my name to the game
2. As a user, I want to be able decide where to place my symbol
3. As a user, I want to be able to have a visual output of the game
4. As a user, I want to be able to see the computer's choices on the game board
5. As a user, I want to be able to see who has won the game
6. As a user, I want to be able to play the game again once the game is complete

#

## FEATURES

The game has got following features:
### Header

* The game has a header which was made in an ASCII generator

![Game_Header](assets/images/game_title.png)

### Name Prompt

* The user gets prompted to input their name so the programme can use it throughou the game

![Name_Prompt](assets/images/name_prompt.png)

### Game Rules

* After inputting a name, the programme displays the game rules
* These are programmed to pop up bit by bit to make sure the user reads them thoroughly

![Game_Rules](assets/images/rules.png)

### User Input

* Afther the rules have been displayed the user is asked to input their game field selection

![User_Input](assets/images/field_selection.png)

### Computer

* The computer is the user's opponent and randomly selects available game fields

![Computer_Input](assets/images/computer_move.png)

### Game Board

* The programme prints a game board after every input to make the available fields and previous selections visible to the user

![board](assets/images/board.png)

### Play Again Option

* The user gets the option to play again after the game has finished

![play_again](assets/images/another_round.png)

### Goodbye Message

* If the user decides they do not want to play another round, a Goodbye message is displayed

![goodbye](assets/images/goodbye.png)

## Future Feature

* An idea for a future feature would be to let the user decide if they want to play against a computer or let Player O be a friend instead and turn the game into a 2 player game on selection

#

# TESTING

## User story testing

1. As a user, I want to be able to add my name to the game

 | **Feature** | **Action** | **Expected Result** | **Actual Result** |
 | ------------- | ------------ | --------------------- | ------------------- |
 | Enter  username | Input username when prompted | Username will be displayed in a welcome message and during the game | Works as expected |

2. As a user, I want to be able decide where to place my symbol

 | **Feature** | **Action** | **Expected Result** | **Actual Result** |
 |-------------|------------|---------------------|-------------------|
 | Select game field | Place symbol on board | The user is able to place the X symbol on the game board | Works as expected |

3. As a user, I want to be able to have a visual output of the game

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Display game board | Symbols placed will appear on board | The symbols placed on the board by user will be visible  | Works as expected |

4. As a user, I want to be able to see the computer's choices on the game board

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Display computer turns | Displays symbol placed by computer on game board | Display computer's symbol on board | Works as expected |


5. As a user, I want to be able to see who has won the game

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Final Result | The user or the computer has placed 3 symbols in a row | Displays a message with the winner of the game | Works as expected |

6. As a user, I want to be able to play the game again once the game is complete

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Final Result | The user has the option of restarting a new game once the game has ended | Displays a message of do you want to play again (y for yes and n for no)| Works as expected |

#

## Validation

### PEP8 Online Validation

PEP8 online was used to check the code for PEP8 requirements.