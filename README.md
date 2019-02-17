# comp472AI_Project

## How to run the program 
1. open Linux terminal and go the directory where you save the Game.py file
2. run ```python Game.py```, when your program starts, just follow the game instruction to input



## Helpful tips - Game board settings
1. Card Type is 1-8, coresponding to the description in the project,
your input coordinate[row, column] is always assigned with left or bottom half
2. Row should be chosen from 1-12, and column should be chosen from A-H
3. Some moves will result invalid states, thus the program will prevent you 
from place the card in such place. Some invalid states we implemented to prevent:
    1). Can't overlap cards 2). Can't make any half of the card dangling 3).Can't move the card 
    that other player just played 4). Can't place the card back to its place with exactly the same
    coordinate. 5). removing the card can't make other card dangling
4. Currently no UI for this game. But we have two visual board for helping player
interact with the board game. One will display the card pattern(color or dot), the other one will
display the card id which help user visualize which two cells a card occupies
