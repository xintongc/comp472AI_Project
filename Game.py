import numpy as np
from Card import *


class Game:
    def __init__(self, turn):
        self.turn = turn
        self.counter = 0
        self.board = np.empty((12, 8), Card) #initial state

        self.current_turn_win = False #flag for win for current player
        self.current_makes_illegal = False #flag for whether current player makes the state illegal
        self.other_could_win = False #flag for checking if the card current player played will make the other win

    def command_line_parser(self, cmd):
        print(str(cmd))

    def toggle_turn(self):
        if self.turn == "color":
            self.turn = "dot"
        else:
            self.turn = "color"

    def other_role(self):
        if self.turn == "color":
            return "dot"
        else:
            return "color"

    def reset_flags(self):
        self.current_turn_win = False;  # flag for win for current player
        self.current_makes_illegal = False;  # flag for whether current player makes the state illegal
        self.other_could_win = False;  # flag for checking if the card current player played will make the other win

    def play_card(self, card, position):
        #when card is played, we need to check if it results a valid state(an illegal state, or make others win)
        #if valid, check if the current turn could win
        self.validate_state(self, self.other_role(), card, position)
        self.check_if_win(self.turn, card, position)
        if(self.current_turn_win == True):
            print("current player win. Game over")

    def validate_state(self, other_role, card, position):
        #check if results an illegals state -> set the flag
            #this should immediately give player feedback and let the Player play again
        #check if this could makes the other player win --> set the flag
            #this is ok if the cuurent player still could win
        print("in validating state")

    def check_if_win(self, role, card, position):
        # algorithm to detect whether given card in
        print(card + position)

    def myfunc(self):
        print("Hello my name is " + self.turn)
        print(self.counter)
        print(self.board)
        self.board[12-2][0] = 3 #indicate A 2
        print("-----------------------")
        print(self.board)

p1 = Game("John")

#p1.myfunc()

