import numpy as np
from Card import *
from Half import *
import copy


class Game:
    def __init__(self, turn):
        self.turn = turn
        self.step_counter = 0
        self.card_counter = 0
        self.board = np.empty((12, 8), Half) #initial state
        self.card_type_list = self.initialize_cardtype()
        self.card_deck = []

        self.current_turn_win = False #flag for win for current player
        self.current_makes_illegal = False #flag for whether current player makes the state illegal
        self.other_could_win = False #flag for checking if the card current player played will make the other win

    def initialize_cardtype(self):
        h1 = Half("R", "X")
        h2 = Half("R", "O")

        h3 = Half("W", "X")
        h4 = Half("W", "O")

        c1 = Card(1, copy.deepcopy(h1), copy.deepcopy(h4))
        c1.half1.position = "l"  # left
        c1.half2.position = "r" #right

        c2 = Card(2, copy.deepcopy(h1), copy.deepcopy(h4))
        c2.half1.position = "t" #top
        c2.half2.position = "b" #bottom

        c3 = Card(3, copy.deepcopy(h1), copy.deepcopy(h4))
        c3.half2.position = "l"  # left
        c3.half1.position = "r"  # right

        c4 = Card(4, copy.deepcopy(h1), copy.deepcopy(h4))
        c4.half2.position = "t"  # top
        c4.half1.position = "b"  # bottom

        c5 = Card(5, copy.deepcopy(h2), copy.deepcopy(h3))
        c5.half1.position = "l"  # left
        c5.half2.position = "r"  # right

        c6 = Card(6, copy.deepcopy(h2), copy.deepcopy(h3))
        c6.half1.position = "t"  # top
        c6.half2.position = "b"  # bottom

        c7 = Card(7, copy.deepcopy(h2), copy.deepcopy(h3))
        c7.half2.position = "l"  # left
        c7.half1.position = "r"  # right

        c8 = Card(8, copy.deepcopy(h2), copy.deepcopy(h3))
        c8.half2.position = "t"  # top
        c8.half1.position = "b"  # bottom

        card_type_list = [c1, c2, c3, c4, c5, c6, c7, c8]
        return card_type_list



    def command_line_parser(self, cmd):
        inputs = str(cmd).split(' ')
        move_type = inputs[0]
        card_type_index = inputs[1] - 1;
        card_column = inputs[2]
        card_row = inputs[3]
        if card_column == "A":
            x = 0
        elif card_column == "B":
            x = 1
        elif card_column == "C":
            x = 2
        elif card_column == "D":
            x = 3
        elif card_column == "E":
            x = 4
        elif card_column == "F":
            x = 5
        elif card_column == "G":
            x = 6
        else:
            x = 7
        coordinate = [card_row, x]
        if move_type == 0:
            self.play_card(copy.deepcopy(self.card_type_list[card_type_index]), coordinate)


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

    def current_role(self):
        if self.turn == "color":
            return "color"
        else:
            return "dot"

    def reset_flags(self):
        self.current_turn_win = False;  # flag for win for current player
        self.current_makes_illegal = False;  # flag for whether current player makes the state illegal
        self.other_could_win = False;  # flag for checking if the card current player played will make the other win

    def print_current_game_board_state(self):
        board = np.empty((12, 8), str)
        print(board)

    def play_card(self, card, coordinate):
        self.reset_flags()
        if self.card_counter >= 24:  # check whether 24 cards have been played
            self.current_makes_illegal = True
            return
        half2_coordinate = card.set_half_coordinate(card.card_type, coordinate)
        if not half2_coordinate:  # check if half2 could be fit into the board, if yes, set both halfs coordinate
            self.current_makes_illegal = True
            return
        if self.board[12-coordinate[0]][coordinate[1]] is not None \
                or self.board[12-half2_coordinate[0]][half2_coordinate[1]] is not None:  # check if both cells are occupied
            self.current_makes_illegal = True
            return
        self.board[12 - coordinate[0]][coordinate[1]] = card.half1 # set board reference to half
        self.board[12 - half2_coordinate[0]][half2_coordinate[1]] = card.half2
        if not self.validate_state(card):
            return
        self.other_could_win = self.check_if_win(self.other_role(), card)
        self.current_turn_win = self.check_if_win(self.current_role(), card)
        if self.current_turn_win is False and self.other_could_win is True:
            self.board[12 - coordinate[0]][coordinate[1]] = None  # set board reference to None
            self.board[12 - half2_coordinate[0]][half2_coordinate[1]] = None
            self.current_makes_illegal = True
            return
        self.card_deck.append(card)  #finally, we played the card, and put it in card deck
        self.print_current_game_board_state()  #display the board and card deck to console


    def validate_state(self, card):
        half1_coordinate = card.get_half1_coordinate()
        half2_coordinate = card.get_half2_coordinate()
        try:
            if self.board[12-half1_coordinate[0]-1][half1_coordinate[1]] is None:
                self.current_makes_illegal = True
                return False
            if self.board[12-half2_coordinate[0]-1][half2_coordinate[1]] is None:
                self.current_makes_illegal = True
                return False
        except IndexError: #means this card is at very bottom
            return True

    def check_if_win(self, role, card):
        return True

    #dummy function to help understand the game board
    def myfunc(self):
        self.board[12-2][0] = 3 #indicate A 2 --> coordinate [2,0]
        self.board[12-6][4] = self.card_type_list[7] # meaning place card position 8 on [row = 6, column=4]
        print("-----------------------")

p1 = Game("John")

#p1.myfunc()

