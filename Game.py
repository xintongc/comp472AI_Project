import numpy as np


class Game:
    def __init__(self, turn):
        self.turn = turn
        self.counter = 0
        self.board = np.empty((12, 8), Card) #initial state

    def play_card(self, role, card):
        print()

    def myfunc(self):
        print("Hello my name is " + self.turn)
        print(self.counter)
        print(self.board)
        self.board[12-2][0] = 3 #indicate A 2

        print("-----------------------")
        print(self.board)

    def validatestate(self):
        print("in validating state")

    def wincheck(self, card, position):
        print(card + position)

p1 = Game("John")

#p1.myfunc()

