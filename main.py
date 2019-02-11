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

while g.counter <= 60 and g.current_turn_win is False:
    if current_player.__eq__("Player 1"):
        player_one_move = input("Player 1: Please give your move:\n")
        g.command_line_parser(player_one_move)
        if g.current_turn_win:
            print(current_player + " wins. Game Over!")
            break
        current_player = "Player 2"

    else:
        player_two_move = input("Player 2: Please give your move:\n")
        g.command_line_parser(player_two_move)
        if g.current_turn_win:
            print(current_player + " wins. Game Over!")
            break
        current_player = "Player 1"

if g.counter == 60:
    print("Over 60 moves. Tie!")