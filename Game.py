import sys
import random

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


def place_temp_half(type_str, row_num, column_num):
    global board_visual
    board_visual[12 - row_num][column_num] = type_str


def remove_temp_card(row_num1, column_num1, row_num2, column_num2):
    global board_visual
    board_visual[12 - row_num1][column_num1] = '  '  # set the recycled card coordinate empty
    board_visual[12 - row_num2][column_num2] = '  '


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


def card_type_coordinates_association_dict():
    result = {}
    row1, column1 = 1, 1
    while column1 < 9:
        row1 = 1
        while row1 < 12:
            if board_visual[12 - row1][column1] == '  ':
                card_type = 1
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
                card_type = 2
                row2 = second_half_row(card_type, row1)
                column2 = second_half_column(card_type, column1)
                if board_visual[12 - row2][column2] == '  ':
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


def find_recyclable_card_nums():
    global board_card
    result = []
    row1, column1 = 12, 1
    while column1 < 9:
        row1 = 12
        while row1 > 0:
            if board_card[12 - row1][column1] != '  ':
                card_num = board_card[12 - row1][column1]
                if card_num not in result:
                    row2 = dict_row[card_num]
                    column2 = dict_column[card_num]
                    if row1 != row2 and column1 != column2:
                        if row1 != recent_row and column1 != recent_column:
                            if is_recycle_valid(card_num, row1, column2):
                                result.append([card_num, row1, column1, row2, column2])
                        else:
                            continue
                    else:
                        continue
            else:
                row1 -= 1
        column1 += 1
    return result


def generate_tracking_file(dict):
    with open('tracemm.txt', 'a') as f:
        f.writelines(dict.get('e_counter'))
        f.writelines(dict.get('level1')[0])
        f.writelines('\n')
        for num in dict.get('level2'):
            f.writelines(num)
        f.writelines('\n')
        f.close()


def run_min_max():
    global board_visual, isFileGenEnabled
    e_counter = 0
    minmax_trace = {'level1': [], 'level2': [], 'level3': [], "e_counter": e_counter}
    dict_level_1 = card_type_coordinates_association_dict()
    final_max_value = float(-10000000.0)
    final_cmd = ''
    for card_type_1, cmds_1 in dict_level_1:
        for cmd_1 in cmds_1:
            inputList_1 = command_line_parser(cmd_1)
            row1_1 = inputList_1[2]
            row2_1 = second_half_row(card_type_1, row1_1)
            column1_1 = inputList_1[1]
            column2_1 = second_half_column(card_type_1, column1_1)
            half_name1_1 = first_half_name(card_type_1)
            half_name2_1 = second_half_name(card_type_1)
            place_temp_half(half_name1_1, row1_1, column1_1)
            place_temp_half(half_name2_1, row2_1, column2_1)

            dict_level_2 = card_type_coordinates_association_dict()
            min_value = float(10000000.0)
            for card_type_2, cmds_2 in dict_level_2:
                for cmd_2 in cmds_2:
                    inputList_2 = command_line_parser(cmd_2)
                    row1_2 = inputList_2[2]
                    row2_2 = second_half_row(card_type_2, row1_2)
                    column1_2 = inputList_2[1]
                    column2_2 = second_half_column(card_type_2, column1_2)
                    half_name1_2 = first_half_name(card_type_2)
                    half_name2_2 = second_half_name(card_type_2)
                    place_temp_half(half_name1_2, row1_2, column1_2)
                    place_temp_half(half_name2_2, row2_2, column2_2)

                    dict_level_3 = card_type_coordinates_association_dict()
                    max_value = float(-10000000.0)
                    for card_type_3, cmds_3 in dict_level_3:
                        for cmd_3 in cmds_3:
                            e = float("{:.1f}".format(evaluate(board_visual, cmd_3)))
                            e_counter += 1
                            if e > max_value:
                                max_value = e
                    minmax_trace.get('level3').append(max_value)
                    remove_temp_card(row1_2, column1_2, row2_2, column2_2)
                    if max_value < min_value:
                        min_value = max_value
            minmax_trace.get('level2').append(min_value)
            remove_temp_card(row1_1, column1_1, row2_1, column2_1)
            if final_max_value < min_value:
                final_max_value = min_value
                final_cmd = cmd_1
    minmax_trace.get('level1').append(final_max_value)
    minmax_trace.get('e_counter').append(e_counter)

    if isFileGenEnabled:
        generate_tracking_file(minmax_trace)

    return final_cmd


def evaluate(board, cmd):  # board has two additional card, try to place the third card with cmd
    return 0


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
isFileGenEnabled = False




print("AI is deciding it plays the as 1st Player or 2nd Player:....")
ai_player_num = random.randint(1, 3)
human_player_num = 0
if ai_player_num == 1:
    human_player_num = 2
else:
    human_player_num = 1
print("AI chooses to be Player " + ai_player_num)
print('Human is Player ' + human_player_num)


ai_player_role = ''
human_player_role = ''
if ai_player_num == 1:
    print("AI is deciding which role to play (color or dot):......")
    i = random.randint(1, 3)
    if i == 1:
        ai_player_role = 'color'
        human_player_row = 'dot'
        print('Player1 plays ' + ai_player_role + " Player2 plays " + human_player_row)
    else:
        ai_player_role = 'dot'
        human_player_row = 'color'
        print('Player1 plays ' + ai_player_role + " Player2 plays " + human_player_row)
else:
    role_select = input("Player1: Please choose a role to play (c for color and d for dot):")
    while not is_color_dot_valid(role_select):
        print("Your input is invalid, please input again:")
        role_select = input("Player1: Please choose a role to play (c for color and d for dot):")
    if role_select == 'c':
        ai_player_role = 'dot'
        human_player_row = 'color'
        print('Player1 plays ' + human_player_row + " Player2 plays " + ai_player_role)
    else:
        ai_player_role = 'color'
        human_player_row = 'dot'
        print('Player1 plays ' + human_player_row + " Player2 plays " + ai_player_role)

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
        print("Last Card placed on col = " + str(recent_column) + " row = " + str(recent_row))
        print_board()
        put_board_card(recycle_card_id, row1, column1, row2, column2)
        print_board_card()
