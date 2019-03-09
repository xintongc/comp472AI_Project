import sys

board_visual = [['12', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
                ['11', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
                ['10', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
                ['09', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
                ['08', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
                ['07', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
                ['06', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
                ['05', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
                ['04', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
                ['03', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
                ['02', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
                ['01', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
                ['  ', 'A ', 'B ', 'C ', 'D ', 'E ', 'F ', 'G ', 'H ']]

board_card = [['12', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
              ['11', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
              ['10', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
              ['09', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
              ['08', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
              ['07', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
              ['06', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
              ['05', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
              ['04', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
              ['03', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
              ['02', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
              ['01', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
              ['  ', 'A ', 'B ', 'C ', 'D ', 'E ', 'F ', 'G ', 'H ']]


class Game:
    def __init__(self, turn):
        self.turn = turn
        self.step_counter = 0
        self.card_counter = 0
        self.board = np.empty((12, 8), Half)  # initial state
        self.board_visual = np.empty((12, 8), str)  # initial state
        self.card_type_list = self.initialize_cardtype()
        self.card_deck = []

        self.current_turn_win = False  # flag for win for current player
        self.current_makes_illegal = False  # flag for whether current player makes the state illegal
        self.other_could_win = False  # flag for checking if the card current player played will make the other win

    def initialize_cardtype(self):
        h1 = Half("R", "X")
        h2 = Half("R", "O")

        h3 = Half("W", "X")
        h4 = Half("W", "O")

        c1 = Card(1, copy.deepcopy(h1), copy.deepcopy(h4))
        c1.half1.position = "l"  # left
        c1.half2.position = "r"  # right

        c2 = Card(2, copy.deepcopy(h1), copy.deepcopy(h4))
        c2.half1.position = "t"  # top
        c2.half2.position = "b"  # bottom

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
            card = copy.deepcopy(self.card_type_list[card_type_index])
            card.set_cardId(len(self.card_deck) + 1)
            self.play_card(card, coordinate)

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
        print("The game board is \n")
        print(self.board_visual)
        print("The card deck is \n")
        print(self.card_deck)

    #
    # def is_state_valid(self, row1, column1, row2, column2):
    #     global board_visual
    #     self.reset_flags()
    #     if row1 == 0 or row2 == 0 or column1 == 0 or column2 == 0:  # check if half2 could be fit into the board, if yes, set both halfs coordinate
    #         return False
    #     if board_visual[12-row1][column1] != '  ' or board_visual[12-row2][column2] != '  ':# check if both cells are occupied
    #         return False
    #     if board_visual[12-row1-1][column1] == '  ' or board_visual[12-row2-1][column2] == '  ':# check if both cells are occupied
    #         return False
    #     else:
    #         return False

    def check_if_win(self, role, card):
        half1_color = card.get_half1_color()
        half1_dot = card.get_half1_dot()
        half1_coordinate = card.get_half1_coordinate()
        half2_color = card.get_half2_color()
        half2_dot = card.get_half2_dot()
        half2_coordinate = card.get_half2_coordinate()
        if role == "color":
            half1_color_map = self.check(half1_color, half1_coordinate)
            if half1_color_map.__sizeof__() > 1:
                print("--------win with four ", half1_color, " in line")
                return True
            half2_color_map = self.check(half2_color, half2_coordinate)
            if half2_color_map.__sizeof__() > 1:
                print("--------win with four ", half2_color, " in line")
                return True
        if role == "dot":
            half1_dot_map = self.check(half1_dot, half1_coordinate)
            if half1_dot_map.__sizeof__() > 1:
                print("--------win with four ", half1_dot, " in line")
                return True
            half2_dot_map = self.check(half2_dot, half2_coordinate)
            if half2_dot_map.__sizeof__() > 1:
                print("--------win with four ", half2_dot, " in line")
                return True
        return False

    def check(self, role_token, coordinate):
        direction_map = {}
        t = self.check_in_direction_with_distance("t", role_token, coordinate, 1)
        b = self.check_in_direction_with_distance("b", role_token, coordinate, 1)
        if t + b >= 3:
            direction_map["t"] = t
            direction_map["b"] = b
            return direction_map

        tr = self.check_in_direction_with_distance("tr", role_token, coordinate, 1)
        bl = self.check_in_direction_with_distance("bl", role_token, coordinate, 1)
        if tr + bl >= 3:
            direction_map["tr"] = tr
            direction_map["bl"] = bl
            return direction_map

        r = self.check_in_direction_with_distance("r", role_token, coordinate, 1)
        l = self.check_in_direction_with_distance("l", role_token, coordinate, 1)
        if r + l >= 3:
            direction_map["r"] = r
            direction_map["l"] = l
            return direction_map

        rb = self.check_in_direction_with_distance("rb", role_token, coordinate, 1)
        lt = self.check_in_direction_with_distance("lt", role_token, coordinate, 1)
        if lt + rb >= 3:
            direction_map["rb"] = rb
            direction_map["lt"] = lt
            return direction_map

    def check_in_direction_with_distance(self, direction, role_token, coordinate, distance):
        num_in_line = 0
        while distance < 4:
            try:
                if direction == "t":
                    if self.board[12 - coordinate[0] + distance][coordinate[1]].match_with_role_token(role_token):
                        num_in_line += 1
                    else:
                        break
                if direction == "tr":
                    if self.board[12 - coordinate[0] + distance][coordinate[1] + distance].match_with_role_token(
                            role_token):
                        num_in_line += 1
                    else:
                        break
                if direction == "r":
                    if self.board[12 - coordinate[0]][coordinate[1] + distance].match_with_role_token(role_token):
                        num_in_line += 1
                    else:
                        break
                if direction == "rb":
                    if self.board[12 - coordinate[0] - distance][coordinate[1] + distance].match_with_role_token(
                            role_token):
                        num_in_line += 1
                    else:
                        break
                if direction == "b":
                    if self.board[12 - coordinate[0] - distance][coordinate[1]].match_with_role_token(role_token):
                        num_in_line += 1
                    else:
                        break
                if direction == "bl":
                    if self.board[12 - coordinate[0] - distance][coordinate[1] - distance].match_with_role_token(
                            role_token):
                        num_in_line += 1
                    else:
                        break
                if direction == "l":
                    if self.board[12 - coordinate[0]][coordinate[1] - distance].match_with_role_token(role_token):
                        num_in_line += 1
                    else:
                        break
                if direction == "lt":
                    if self.board[12 - coordinate[0] + distance][coordinate[1] - distance].match_with_role_token(
                            role_token):
                        num_in_line += 1
                    else:
                        break
                distance += 1
            except IndexError:  # means this card is at very bottom
                num_in_line += 0
                break
        return num_in_line

    # dummy function to help understand the game board


#     def myfunc(self):
#         board = np.empty(12, 8)
#         board[12-2][0] = "WO" #indicate A 2 --> coordinate [2,0]
#         board[12-6][4] = "RX" # meaning place card position 8 on [row = 6, column=4]
#         print(board)
#
#
# p1 = Game("John")
#
# p1.myfunc()


def command_line_parser(cmd):
    inputs = str(cmd).split(' ')
    card_type = inputs[0]
    card_column = parse_colunm(inputs[1])
    card_row = parse_row(inputs[2])
    return [card_type, card_column, card_row]


def print_board():
    for item in board_visual:
        print(item)


def toggle_player(player):
    if player == '1':
        return '2'
    else:
        return '1'


def second_half_name(card_typeid):
    if card_typeid == 1 or card_typeid == 4:
        return "WO"
    if card_typeid == 2 or card_typeid == 3:
        return "RX"
    if card_typeid == 6 or card_typeid == 7:
        return "RO"
    if card_typeid == 5 or card_typeid == 8:
        return "WX"


def first_half_name(card_typeid):
    if card_typeid == 2 or card_typeid == 3:
        return "WO"
    if card_typeid == 1 or card_typeid == 4:
        return "RX"
    if card_typeid == 5 or card_typeid == 8:
        return "RO"
    if card_typeid == 6 or card_typeid == 7:
        return "WX"


def second_half_row(card_typeid, row_num):
    if card_typeid == 1 or card_typeid == 3 or card_typeid == 5 or card_typeid == 7:
        return row_num
    row_num += 1
    if row_num == 13:
        return 0
    else:
        return row_num


def second_half_column(card_typeid, column_num):
    if card_typeid == 1 or card_typeid == 3 or card_typeid == 5 or card_typeid == 7:
        column_num += 1
    if column_num == 9:
        return 0
    else:
        return column_num


def place_half(role, type_str, row_num, column_num):
    global board_visual, game_over
    board_visual[12 - row_num][column_num] = type_str
    if check_if_win(role, type_str, row_num, column_num):
        print_board()
        sys.exit([0])


def incre_card_id():
    global card_id
    global board_card
    card_id = card_id + 1
    card_id_str = str(card_id)
    if (len(card_id_str) < 2):
        card_id_str = '0' + card_id_str
    return card_id_str


def put_board_card(card_num, row_num1, column_num1, row_num2, column_num2):
    board_card[12 - row_num1][column_num1] = card_num
    board_card[12 - row_num2][column_num2] = card_num
    dict_row[
        card_num] = row_num2  # create 2 dictionary, we can find the other halfs position according to card_id, used for recycle
    dict_column[card_num] = column2


def print_board_card():
    print()
    for item in board_card:
        print(item)


def recycle_card(row_num, column_num, row_num2, column_num2):
    global board_visual
    global board_card
    board_visual[12 - row_num][column_num] = '  '  # set the recycled card coordinate empty
    board_visual[12 - row_num2][column_num2] = '  '
    board_card[12 - row_num][column_num] = '  '
    board_card[12 - row_num2][column_num2] = '  '


def get_type(half_type, row1, column1, row2,
             column2):  # get the type according to the relative position of the other half
    if row1 == row2 and half_type == "RX":
        return 1
    if row1 == row2 and half_type == "WO":
        return 3
    if row1 == row2 and half_type == "RO":
        return 5
    if row1 == row2 and half_type == "WX":
        return 7
    if column1 == column2 and half_type == "RX":
        return 4
    if column1 == column2 and half_type == "WO":
        return 2
    if column1 == column2 and half_type == "RO":
        return 8
    if column1 == column2 and half_type == "WX":
        return 6


def is_card_type_valid(num):
    if not is_int(num):
        return False
    elif int(num) < 1 or int(num) > 8:
        return False
    else:
        return True


def is_color_dot_valid(t):
    if t == 'c' or t == 'd':
        return True
    else:
        return False


def is_state_valid(row1, column1, row2, column2):
    global board_visual
    if row1 == 0 or row2 == 0 or column1 == 0 or column2 == 0:  # check if half2 could be fit into the board, if yes, set both halfs coordinate
        return False
    if board_visual[12 - row1][column1] != '  ' or board_visual[12 - row2][
        column2] != '  ':  # check if both cells are occupied
        return False
    if abs(row1 - row2) == 1:
        if board_visual[12 - row1 + 1][column1] == '  ':
            return False
        else:
            return True
    if abs(column1 - column2) == 1:
        if board_visual[12 - row1 + 1][column1] == '  ' or board_visual[12 - row2 + 1][
            column2] == '  ':  # check if both cells are occupied
            return False
        else:
            return True
    else:
        return True


def is_recycle_state_valid(rotated, row1, column1, row2, column2):
    if not rotated:
        if row1 == toked_row and column1 == toked_column:
            return False

    global board_visual
    if row1 == 0 or row2 == 0 or column1 == 0 or column2 == 0:  # check if half2 could be fit into the board, if yes, set both halfs coordinate
        return False
    if board_visual[12 - row1][column1] != '  ' or board_visual[12 - row2][
        column2] != '  ':  # check if both cells are occupied
        return False
    if abs(row1 - row2) == 1:
        if board_visual[12 - row1 + 1][column1] == '  ':
            return False
        else:
            return True
    if abs(column1 - column2) == 1:
        if board_visual[12 - row1 + 1][column1] == '  ' or board_visual[12 - row2 + 1][
            column2] == '  ':  # check if both cells are occupied
            return False
        else:
            return True
    else:
        return True


def is_recycle_valid(recycle_card_id, row1, column1):
    if row1 == recent_row and column1 == recent_column:
        print("This card just been moved/placed")
        return False

    if board_visual[12 - row1][column1] == '  ':
        return False
    row2 = dict_row[recycle_card_id]
    column2 = dict_column[recycle_card_id]
    if board_card[12 - row1][column1] != board_card[12 - row2][column2]:
        return False
    try:
        if abs(row1 - row2) == 1:
            if board_visual[12 - row1 - 1][column1] != '  ' and board_visual[12 - row2 - 1][
                column2] != '  ':  # check if both cells are occupied
                return False
            else:
                return True
        if abs(column1 - column2) == 1:
            if board_visual[12 - row1 - 1][column1] != '  ' or board_visual[12 - row2 - 1][
                column2] != '  ':  # check if both cells are occupied
                return False
            else:
                return True
    except IndexError:  # means this card is at very bottom
        return True
        return False


def is_int(n):
    try:
        int(n)
        return True
    except ValueError:
        return False


def parse_row(card_row):
    if not is_int(card_row):
        return 0
    else:
        row = int(card_row)
        if row < 1 or row > 12:
            return 0
        else:
            return int(card_row)


def print_card_type():
    print()
    print("1        2       3       4       5       6       7       8")
    print("RX WO    RX      WO RX   WO      RO WX   RO      WX RO   WX")
    print("         WO              RX              WX              RO")
    print()


def parse_colunm(card_column):
    if card_column == "A":
        return 1
    elif card_column == "B":
        return 2
    elif card_column == "C":
        return 3
    elif card_column == "D":
        return 4
    elif card_column == "E":
        return 5
    elif card_column == "F":
        return 6
    elif card_column == "G":
        return 7
    elif card_column == "H":
        return 8
    else:
        return 0


def check_if_win(role, type_str, row_num, column_num):
    half_color = type_str[0]
    half_dot = type_str[1]
    half_coordinate = [row_num, column_num]
    if role == "color":
        half1_color_map = check(half_color, half_coordinate)
        if bool(half1_color_map):
            print("--------win with four ", half_color, " in line")
            return True
    if role == "dot":
        half1_dot_map = check(half_dot, half_coordinate)
        if bool(half1_dot_map):
            print("--------win with four ", half_dot, " in line")
            return True
    return False


def check(role_token, coordinate):
    direction_map = {}
    t = check_in_direction_with_distance("t", role_token, coordinate, 1)
    b = check_in_direction_with_distance("b", role_token, coordinate, 1)
    if t + b >= 3:
        direction_map["t"] = t
        direction_map["b"] = b
        return direction_map

    tr = check_in_direction_with_distance("tr", role_token, coordinate, 1)
    bl = check_in_direction_with_distance("bl", role_token, coordinate, 1)
    if tr + bl >= 3:
        direction_map["tr"] = tr
        direction_map["bl"] = bl
        return direction_map

    r = check_in_direction_with_distance("r", role_token, coordinate, 1)
    l = check_in_direction_with_distance("l", role_token, coordinate, 1)
    if r + l >= 3:
        direction_map["r"] = r
        direction_map["l"] = l
        return direction_map

    rb = check_in_direction_with_distance("rb", role_token, coordinate, 1)
    lt = check_in_direction_with_distance("lt", role_token, coordinate, 1)
    if lt + rb >= 3:
        direction_map["rb"] = rb
        direction_map["lt"] = lt
        return direction_map


def check_in_direction_with_distance(direction, role_token, coordinate, distance):
    global board_card
    num_in_line = 0
    while distance < 4:
        try:
            if direction == "t":
                if role_token in board_visual[12 - coordinate[0] - distance][coordinate[1]]:
                    num_in_line += 1
                else:
                    break
            if direction == "tr":
                if role_token in board_visual[12 - coordinate[0] - distance][coordinate[1] + distance]:
                    num_in_line += 1
                else:
                    break
            if direction == "r":
                if role_token in board_visual[12 - coordinate[0]][coordinate[1] + distance]:
                    num_in_line += 1
                else:
                    break
            if direction == "rb":
                if role_token in board_visual[12 - coordinate[0] + distance][coordinate[1] + distance]:
                    num_in_line += 1
                else:
                    break
            if direction == "b":
                if role_token in board_visual[12 - coordinate[0] + distance][coordinate[1]]:
                    num_in_line += 1
                else:
                    break
            if direction == "bl":
                if role_token in board_visual[12 - coordinate[0] + distance][coordinate[1] - distance]:
                    num_in_line += 1
                else:
                    break
            if direction == "l":
                if role_token in board_visual[12 - coordinate[0]][coordinate[1] - distance]:
                    num_in_line += 1
                else:
                    break
            if direction == "lt":
                if role_token in board_visual[12 - coordinate[0] - distance][coordinate[1] - distance]:
                    num_in_line += 1
                else:
                    break
            distance += 1
        except IndexError:  # means this card is at very bottom
            # num_in_line += 0
            break
    return num_in_line


def card_type_coordinates_association_map():
    result = {}
    row1, column1 = 1, 1
    while column1 < 9:
        row1 = 1
        while row1 < 12:
            if board_card[12-row1][column1] == '  ':
                card_type = 1
                row2 = second_half_row(card_type, row1)
                column2 = second_half_column(card_type, column1)
                if board_card[12-row2][column2] == '  ':
                    if is_state_valid(row1, column1, row2, column2):
                        while card_type < 9:
                            cmd = str(card_type) + " " + str(column1) + " " + str(row1)
                            if not result.get(card_type):
                                result.__setitem__(card_type, [cmd])
                            else:
                                result.get(card_type).append(cmd)
                            card_type += 2
                card_type = 2
                row2 = second_half_row(card_type, row1)
                column2 = second_half_column(card_type, column1)
                if board_card[12 - row2][column2] == '  ':
                    if is_state_valid(row1, column1, row2, column2):
                        while card_type < 9:
                            cmd = str(card_type) + " " + str(column1) + " " + str(row1)
                            if not result.get(card_type):
                                result.__setitem__(card_type, [cmd])
                            else:
                                result.get(card_type).append(cmd)
                            card_type += 2
                break
            else:
                row1 += 1
        column1 += 1
    return result


def generate_tracking_file(map):
    with open('tracemm.txt', 'r+') as f:
        f.writelines(len(map.get('level3')))
        f.writelines(map.get('level1')[0])
        f.writelines('\n')
        for num in map.get('level2'):
            f.writelines(num)
        f.writelines('\n')
        f.close()


def run_min_max():
    return 'cmd'


def evaluate(role_select, cmd): #board has two additional card, try to place the third card with cmd
    global board_visual
    inputList = command_line_parser(cmd)
    card_type = int(inputList[0])
    row1 = inputList[2]
    row2 = second_half_row(card_type, row1)
    column1 = inputList[1]
    column2 = second_half_column(card_type, column1)

    factor_one = 1
    factor_two = 5
    factor_three = 20
    factor_four = 1000
    factor_half1 = 10
    factor_half2 = 2
    factor_empty_cell = 2

    en_r = 0
    en_x = 0
    en_w = 0
    en_o = 0
    en_color = 0
    en_dot = 0

    if card_type == 1 or card_type == 4:
        depth_arr_r = depth('R', row1, column1)
        empty_r = empty_cell('R', row1, column1, depth_arr_r) * factor_empty_cell
        depth_arr_d = depth('X', row1, column1)
        empty_d = empty_cell('X', row1, column1, depth_arr_d) * factor_empty_cell
        depth_arr_w = depth('W', row2, column2)
        empty_w = empty_cell('W', row2, column2, depth_arr_w) * factor_empty_cell
        depth_arr_o = depth('O', row2, column2)
        empty_o = empty_cell('O', row2, column2, depth_arr_o) * factor_empty_cell
    if card_type == 2 or card_type == 3:
        depth_arr_r = depth('R', row2, column2)
        empty_r = empty_cell('R', row2, column2, depth_arr_r) * factor_empty_cell
        depth_arr_d = depth('X', row2, column2)
        empty_d = empty_cell('X', row2, column2, depth_arr_d) * factor_empty_cell
        depth_arr_w = depth('W', row1, column1)
        empty_w = empty_cell('W', row1, column1, depth_arr_w) * factor_empty_cell
        depth_arr_o = depth('O', row1, column1)
        empty_o = empty_cell('O', row1, column1, depth_arr_o) * factor_empty_cell
    if card_type == 5 or card_type == 8:
        depth_arr_r = depth('R', row1, column1)
        empty_r = empty_cell('R', row1, column1, depth_arr_r) * factor_empty_cell
        depth_arr_d = depth('X', row2, column2)
        empty_d = empty_cell('X', row2, column2, depth_arr_d) * factor_empty_cell
        depth_arr_w = depth('W', row2, column2)
        empty_w = empty_cell('W', row2, column2, depth_arr_w) * factor_empty_cell
        depth_arr_o = depth('O', row1, column1)
        empty_o = empty_cell('O', row1, column1, depth_arr_o) * factor_empty_cell
    if card_type == 6 or card_type == 7:
        depth_arr_r = depth('R', row2, column2)
        empty_r = empty_cell('R', row2, column2, depth_arr_r) * factor_empty_cell
        depth_arr_d = depth('X', row1, column1)
        empty_d = empty_cell('X', row1, column1, depth_arr_d) * factor_empty_cell
        depth_arr_w = depth('W', row1, column1)
        empty_w = empty_cell('W', row1, column1, depth_arr_w) * factor_empty_cell
        depth_arr_o = depth('O', row2, column2)
        empty_o = empty_cell('O', row2, column2, depth_arr_o) * factor_empty_cell

    score_r = [depth_arr_r[0] + depth_arr_r[1], depth_arr_r[2] + depth_arr_r[3], depth_arr_r[4] + depth_arr_r[5],
               depth_arr_r[6] + depth_arr_r[7]]
    score_d = [depth_arr_d[0] + depth_arr_d[1], depth_arr_d[2] + depth_arr_d[3], depth_arr_d[4] + depth_arr_d[5],
               depth_arr_d[6] + depth_arr_d[7]]
    score_w = [depth_arr_w[0] + depth_arr_w[1], depth_arr_w[2] + depth_arr_w[3], depth_arr_w[4] + depth_arr_w[5],
               depth_arr_w[6] + depth_arr_w[7]]
    score_o = [depth_arr_o[0] + depth_arr_o[1], depth_arr_o[2] + depth_arr_o[3], depth_arr_o[4] + depth_arr_o[5],
               depth_arr_o[6] + depth_arr_o[7]]

    for score in score_r:
        if score == 1:
            en_r += factor_one
        if score == 2:
            en_r += factor_two
        if score == 3:
            en_r += factor_three
        if score == 4:
            en_r += factor_four * factor_four
            break

    for score in score_d:
        if score == 1:
            en_x += factor_one
        if score == 2:
            en_x += factor_two
        if score == 3:
            en_x += factor_three
        if score == 4:
            en_x += factor_four * factor_four
            break

    for score in score_w:
        if score == 1:
            en_w += factor_one
        if score == 2:
            en_w += factor_two
        if score == 3:
            en_w += factor_three
        if score == 4:
            en_w += factor_four * factor_four
            break

    for score in score_o:
        if score == 1:
            en_o += factor_one
        if score == 2:
            en_o += factor_two
        if score == 3:
            en_o += factor_three
        if score == 4:
            en_o += factor_four * factor_four
            break

    if card_type == 1 or card_type == 4:
        en_color = (en_r + empty_r) * factor_half1 + (en_w + empty_w) * factor_half2
        en_dot = (en_x + empty_d) * factor_half1 + (en_o + empty_o) * factor_half2

    if card_type == 2 or card_type == 3:
        en_color = (en_w + empty_w) * factor_half1 + (en_r + empty_r) * factor_half2
        en_dot = (en_o + empty_o) * factor_half1 + (en_x + empty_d) * factor_half2

    if card_type == 5 or card_type == 8:
        en_color = (en_r + empty_r) * factor_half1 + (en_w + empty_w) * factor_half2
        en_dot = (en_o + empty_o) * factor_half1 + (en_x + empty_d) * factor_half2

    if card_type == 6 or card_type == 7:
        en_color = (en_w + empty_w) * factor_half1 + (en_o + empty_o) * factor_half2
        en_dot = (en_x + empty_d) * factor_half1 + (en_r + empty_r) * factor_half2

    if role_select == "color":
        return en_color - en_dot
    else:
        return en_dot - en_color


def depth(role_token, row, column):
    global board_visual
    coordinate = [row, column]
    t = check_in_direction_in_virtual_board("t", role_token, coordinate)
    b = check_in_direction_in_virtual_board("b", role_token, coordinate)
    tr = check_in_direction_in_virtual_board("tr", role_token, coordinate)
    bl = check_in_direction_in_virtual_board("bl", role_token, coordinate)
    r = check_in_direction_in_virtual_board("r", role_token, coordinate)
    l = check_in_direction_in_virtual_board("l", role_token, coordinate)
    rb = check_in_direction_in_virtual_board("rb", role_token, coordinate)
    lt = check_in_direction_in_virtual_board("lt", role_token, coordinate)
    return [t,  b, tr,  bl, r,  l, rb,  lt]


def empty_cell(role_token, row, column, depth_num):
    global board_visual
    coordinate = [row, column]
    number = 0;
    try:
        if board_visual[12 - coordinate[0] - depth_num[0]][coordinate[1]] == ' ':
            ++number
    except IndexError:
    try:
        if board_visual[12 - coordinate[0] - depth_num[2]][coordinate[1] + depth_num[2]] == ' ':
            ++number
    except IndexError:
    try:
        if board_visual[12 - coordinate[0]][coordinate[1] + - depth_num[4]] == ' ':
            ++number
    except IndexError:
    try:
        if board_visual[12 - coordinate[0] + depth_num[6]][coordinate[1] + depth_num[6]] == ' ':
            ++number
    except IndexError:
    try:
        if board_visual[12 - coordinate[0] + depth_num[1]][coordinate[1]] == ' ':
        ++number
    except IndexError:
    try:
        if board_visual[12 - coordinate[0] + depth_num[3]][coordinate[1] - depth_num[3]] == ' ':
        ++number
    except IndexError:
    try:
        if board_visual[12 - coordinate[0]][coordinate[1] - depth_num[5]] == ' ':
        ++number
    except IndexError:
    try:
        if board_visual[12 - coordinate[0] - depth_num[7]][coordinate[1] - depth_num[7]] == ' ':
            ++number
    except IndexError:
    return number


def check_in_direction_in_virtual_board(direction, role_token, coordinate):
    global board_visual
    num_in_line = 0
    distance = 1
    while distance <= 4:
        try:
            if direction == "t":
                if role_token in board_visual[12 - coordinate[0] - distance][coordinate[1]]:
                    num_in_line += 1
                else:
                    break
            if direction == "tr":
                if role_token in board_visual[12 - coordinate[0] - distance][coordinate[1] + distance]:
                    num_in_line += 1
                else:
                    break
            if direction == "r":
                if role_token in board_visual[12 - coordinate[0]][coordinate[1] + distance]:
                    num_in_line += 1
                else:
                    break
            if direction == "rb":
                if role_token in board_visual[12 - coordinate[0] + distance][coordinate[1] + distance]:
                    num_in_line += 1
                else:
                    break
            if direction == "b":
                if role_token in board_visual[12 - coordinate[0] + distance][coordinate[1]]:
                    num_in_line += 1
                else:
                    break
            if direction == "bl":
                if role_token in board_visual[12 - coordinate[0] + distance][coordinate[1] - distance]:
                    num_in_line += 1
                else:
                    break
            if direction == "l":
                if role_token in board_visual[12 - coordinate[0]][coordinate[1] - distance]:
                    num_in_line += 1
                else:
                    break
            if direction == "lt":
                if role_token in board_visual[12 - coordinate[0] - distance][coordinate[1] - distance]:
                    num_in_line += 1
                else:
                    break
            distance += 1
        except IndexError:  # means this card is at very bottom
            # num_in_line += 0
            break
    return num_in_line


step_counter = 0
valid_card_position = False
playerId = '2'
card_id = 0
dict_row = {}
dict_column = {}
dict_card_type = {}
role_one = ""
role_two = ""
recent_row = 100
recent_column = 100
toked_row = 100
toked_column = 100
# recycle_id = board_card[12 - recycle_row][recycle_column]
recycle_step = 2

role_select = input("Player1: Please choose a role to play (c for color and d for dot):")
while not is_color_dot_valid(role_select):
    print("Your input is invalid, please input again:")
    role_select = input("Player1: Please choose a role to play (c for color and d for dot):")

player_one = role_select

if player_one.__eq__("c"):
    role_one = "color"
else:
    role_one = "dot"
print("Player 1, you are playing: " + role_one)
if role_one.__eq__("color"):
    role_two = "dot"
else:
    role_two = "color"
print("Your counterpart(Player 2), will be playing: " + role_two)

while step_counter <= 60:
    while card_id <= recycle_step:
        playerId = toggle_player(playerId)
        if playerId == 1:
            role = role_one
        else:
            role = role_two
        print_card_type()
        print_board()

        inputText = input("Player " + playerId + ": Select a card and place it. (cardType, col, row):")
        inputList = command_line_parser(inputText)
        card_type = int(inputList[0])
        row1 = inputList[2]
        row2 = second_half_row(card_type, row1)
        column1 = inputList[1]
        column2 = second_half_column(card_type, column1)

        while not is_card_type_valid(card_type) or not is_state_valid(row1, column1, row2, column2):
            print("Your input is invalid, please input again:")
            inputText = input("Player " + playerId + ": Select a card and place it. (cardType, col, row):")
            inputList = command_line_parser(inputText)
            card_type = int(inputList[0])
            row1 = inputList[2]
            row2 = second_half_row(card_type, row1)
            column1 = inputList[1]
            column2 = second_half_column(card_type, column1)

        half_name1 = first_half_name(card_type)
        half_name2 = second_half_name(card_type)
        card_num = incre_card_id()

        dict_card_type[card_num] = card_type

        place_half(role, half_name1, row1, column1)
        place_half(role, half_name2, row2, column2)
        recent_row = row1
        recent_column = column1
        print("Last Card placed on col = " + str(recent_column) + " row = " + str(recent_row))

        put_board_card(card_num, row1, column1, row2, column2)
        print_board()
        print_board_card()
        step_counter = step_counter + 1
    while card_id > recycle_step:
        playerId = toggle_player(playerId)
        if playerId == 1:
            role = role_one
        else:
            role = role_two
        print_card_type()
        inputList = command_line_parser(
            "X " + input("Player " + playerId + ": Please type the recycle card column and row(col row):"))
        row1 = inputList[2]
        column1 = inputList[1]
        recycle_card_id = board_card[12 - row1][column1]
        while not is_recycle_valid(recycle_card_id, row1, column1):
            print("Player " + playerId + ":your input is invalid, please input again.")
            inputList = command_line_parser(
                "X " + input("Player " + playerId + ": Please type the recycle card column and row(col row):"))
            row1 = inputList[2]
            column1 = inputList[1]
            recycle_card_id = board_card[12 - row1][column1]

        toked_row = row1
        toked_column = column1
        row2 = dict_row[recycle_card_id]
        column2 = dict_column[recycle_card_id]
        half_name1 = board_visual[12 - row1][column1]
        half_name2 = board_visual[12 - row2][column2]
        recycle_card(row1, column1, row2, column2)
        print_board()

        inputList = command_line_parser(
            input("Player " + playerId + ": Select a card type for recycle card and place it. (cardType, col, row):"))
        card_type = int(inputList[0])
        row1 = inputList[2]
        row2 = second_half_row(card_type, row1)
        column1 = inputList[1]
        column2 = second_half_column(card_type, column1)

        isRecycleInputValid = False

        while not isRecycleInputValid:
            recycled_card_type = dict_card_type[recycle_card_id]
            if card_type == recycled_card_type:
                rotated = False
            else:
                rotated = True

            if not is_card_type_valid(card_type) or not is_recycle_state_valid(rotated, row1, column1, row2, column2):
                print("Player " + playerId + ": your input is invalid, please input again.")
                inputList = command_line_parser(
                    input(
                        "Player " + playerId + ": Select a card type for recycle card and place it. (cardType, col, row):"))
                card_type = int(inputList[0])
                row1 = inputList[2]
                row2 = second_half_row(card_type, row1)
                column1 = inputList[1]
                column2 = second_half_column(card_type, column1)
            else:
                isRecycleInputValid = True

        # while not is_state_valid(row1, column1, row2, column2):
        #     print("Player " + playerId + ":your input is invalid, please input again.")
        #     row1 = parse_row(input("Player " + playerId + ": Please type the row you want to put the recycle card:"))
        #     column = input("Player " + playerId + ": Please type the column you want to put the recycle card:")
        #     column1 = parse_colunm(column)
        #     row2 = second_half_row(card_type, row1)
        #     column2 = second_half_column(card_type, column1)

        half_name1 = first_half_name(card_type)
        half_name2 = second_half_name(card_type)
        place_half(role, half_name1, row1, column1)
        place_half(role, half_name2, row2, column2)

        dict_card_type[recycle_card_id] = card_type

        recent_row = row1
        recent_column = column1
        print_board()
        put_board_card(recycle_card_id, row1, column1, row2, column2)
        print_board_card()
