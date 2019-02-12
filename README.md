# comp472AI_Project

#Very Important to read
1. Card Type is 1-8, coresponding to the description in the project
Half1 is always assigned with RED, no matter it has X or O. positions are "r l t p", which seems
useless right now, but we will keep it at this moment
2. Agree on the coordinate passed in is for Half1 in each type of card
used set_half_coordinate(coordinate) to set coordinate for Half1 and calculate 
and return coordinate for Half2. This is used for locating the coordinate on 
board
3. Pay attention to coordinate. [y, x] or say, [row, column] = [from bottom to up, and from left to right]
row from 1-12 and column from 0-7. [3, 4] means row 3, column 4. This makes it easy to read 
numpy array
4. each placeholder in 2d array in numpy has a type of Half.
each index could directly refer to the half it has. if it doesn't
have a half, it should be "None" 