from Game import *

role_select = input("Please choose a role to play (c for color and d for dot)\n")

player_one = str(role_select)

if player_one.__eq__("c"):
    role_one = "color"
else:
    role_one = "dot"
print("Now you are player 1, you are playing: " + role_one)
if role_one.__eq__("color"):
    role_two = "dot"
else:
    role_two = "color"
print("Your counterpart(Player 2), will be playing: " + role_two)

g = Game(role_one)
current_player = "Player 1"

print("Game initialized, player 1 will have the first move\n")


print("The game board configuration is:\n", g.board)

while g.counter <= 60:
    if current_player.__eq__("Player 1"):
        print(current_player)

    else:
        print(current_player)

