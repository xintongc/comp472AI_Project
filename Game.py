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


def command_line_parser(cmd):
    try:
        inputs = str(cmd).split(' ')
        card_type = inputs[0]
        card_column = parse_colunm(inputs[1])
        card_row = parse_row(inputs[2])
        return [card_type, card_column, card_row]
    except IndexError:  # means this card is at very bottom
        command_line_parser('1 0 0')


def print_board():
    board_visual[11][0] = '01'
    board_visual[10][0] = '02'
    for item in board_visual:
        print(item)


def toggle_player(player):
    if player == '1':
        return '2'
    else:
        return '1'


def second_half_name(card_typeid):
    if card_typeid == 1 or card_typeid == 4 or card_typeid == '01' or card_typeid == '04':
        return "WO"
    if card_typeid == 2 or card_typeid == 3 or card_typeid == '02' or card_typeid == '03':
        return "RX"
    if card_typeid == 6 or card_typeid == 7 or card_typeid == '06' or card_typeid == '07':
        return "RO"
    if card_typeid == 5 or card_typeid == 8 or card_typeid == '05' or card_typeid == '08':
        return "WX"


def first_half_name(card_typeid):
    if card_typeid == 2 or card_typeid == 3 or card_typeid == '02' or card_typeid == '03':
        return "WO"
    if card_typeid == 1 or card_typeid == 4 or card_typeid == '01' or card_typeid == '04':
        return "RX"
    if card_typeid == 5 or card_typeid == 8 or card_typeid == '05' or card_typeid == '08':
        return "RO"
    if card_typeid == 6 or card_typeid == 7 or card_typeid == '06' or card_typeid == '07':
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
        print(str(role) + " win the game by placing " + str(type_str) + " on row = " + str(row_num) + " col = " + str(
            column_num))
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
    dict_column[card_num] = column_num2


def print_board_card():
    print()
    for item in board_card:
        print(item)


def recycle_card(row_num, column_num, row_num2, column_num2):
    global board_visual
    global board_card
    board_visual[12 - row_num][column_num] = '  '  # set the recycled card coordinate empty
    board_visual[12 - row_num2][column_num2] = '  '
    card_num_to_del = board_card[12 - row_num][column_num]
    del dict_row[card_num_to_del]
    del dict_column[card_num_to_del]
    board_card[12 - row_num][column_num] = '  '
    board_card[12 - row_num2][column_num2] = '  '


def place_temp_half(type_str, row_num, column_num):
    global board_visual
    board_visual[12 - row_num][column_num] = type_str


def remove_temp_card(row_num1, column_num1, row_num2, column_num2):
    global board_visual
    board_visual[12 - row_num1][column_num1] = '  '  # set the recycled card coordinate empty
    board_visual[12 - row_num2][column_num2] = '  '


def place_temp_card_to_board_card(card_num, row_num, column_num, row_num2, column_num2):
    board_card[12 - row_num][column_num] = card_num
    board_card[12 - row_num2][column_num2] = card_num


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
        print("Invalid Reason: This card just been moved/placed")
        return False

    if board_visual[12 - row1][column1] == '  ':
        print("Invalid Reason: The place has no card")
        return False
    row2 = dict_row[recycle_card_id]
    column2 = dict_column[recycle_card_id]
    if board_card[12 - row1][column1] != board_card[12 - row2][column2]:
        print("Invalid Reason: The two half don't belong to the same card")
        return False
    try:
        if abs(row1 - row2) == 1:
            if board_visual[12 - row1 - 1][column1] != '  ' and board_visual[12 - row2 - 1][
                column2] != '  ':  # check if both cells are occupied
                print("Invalid Reason: Vertical occupied")
                return False
            else:
                return True
        if abs(column1 - column2) == 1:
            if board_visual[12 - row1 - 1][column1] != '  ' or board_visual[12 - row2 - 1][
                column2] != '  ':  # check if both cells are occupied
                print("Invalid Reason: Horizontal Occupied")
                return False
            else:
                return True
    except IndexError:  # means this card is at very bottom
        return True


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
    if card_column == "A" or card_column == "1":
        return 1
    elif card_column == "B" or card_column == "2":
        return 2
    elif card_column == "C" or card_column == "3":
        return 3
    elif card_column == "D" or card_column == "4":
        return 4
    elif card_column == "E" or card_column == "5":
        return 5
    elif card_column == "F" or card_column == "6":
        return 6
    elif card_column == "G" or card_column == "7":
        return 7
    elif card_column == "H" or card_column == "8":
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
            if board_card[12 - row1][column1] == '  ':
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


def find_recyclable_card_nums():
    global board_card
    result = []
    row1, column1 = 12, 1
    while column1 < 9:
        row1 = 12
        while row1 > 0:
            if board_visual[12 - row1][column1] != '  ':
                card_num = board_card[12 - row1][column1]
                if card_num not in result:
                    row2 = dict_row[card_num]
                    column2 = dict_column[card_num]
                    if row1 != row2 or column1 != column2:
                        if is_recycle_valid(card_num, row1, column2):
                            result.append([card_num, row1, column1, row2, column2])
                            break
                        else:
                            row1 -= 1
                    else:
                        row1 -= 1
                else:
                    row1 -= 1
            else:
                row1 -= 1
        column1 += 1
    return result


def generate_tracking_file(dict):
    with open(file_name, 'a') as f:
        f.write(str(dict.get('e_counter')))
        f.write('\n')
        f.write(str(dict.get('level1')[0]))
        f.write('\n')
        f.write('\n')
        for num in dict.get('level2'):
            f.write(str(num))
            f.write('\n')
        f.write('\n')
        f.close()


def run_min_max(role):
    global isFileGenEnabled
    e_counter = 0
    minmax_trace = {'level1': [], 'level2': [], 'level3': []}
    dict_level_1 = card_type_coordinates_association_dict()
    final_max_value = float(-10000000.0)
    final_cmd = ''
    for card_type_1, cmds_1 in dict_level_1.items():
        for cmd_1 in cmds_1:
            e_value = evaluate(role, cmd_1)
            if e_value > 10000:
                return cmd_1
            if e_value < -10000:
                inputList = command_line_parser(cmd_1)
                card_type = int(inputList[0])
                if card_type <= 4:
                    card_type = str(card_type + 4)
                else:
                    card_type = str(card_type - 4)
                row1 = inputList[2]
                column1 = inputList[1]
                return card_type + ' ' + str(column1) + ' ' + str(row1)

    for card_type_1, cmds_1 in dict_level_1.items():
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
            for card_type_2, cmds_2 in dict_level_2.items():
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
                    for card_type_3, cmds_3 in dict_level_3.items():
                        for cmd_3 in cmds_3:
                            e = float("{:.1f}".format(evaluate(role, cmd_3)))
                            # print("Level3--MAX------------------@" + str(e) + " "+ cmd_3)
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
    minmax_trace.setdefault("e_counter", e_counter)

    if isFileGenEnabled:
        generate_tracking_file(minmax_trace)

    return final_cmd


def run_min_max_recycle(role):
    global isFileGenEnabled, toked_column, toked_row
    e_counter = 0
    minmax_trace = {'level1': [], 'level2': [], 'level3': []}
    final_max_value = float(-10000000.0)
    final_cmd = ''
    selected_card = ''

    cards_remove_level_1 = find_recyclable_card_nums()
    for card_1 in cards_remove_level_1:
        recycle_card_num_1 = card_1[0]
        first_half_name_recycle_1 = board_visual[12 - card_1[1]][card_1[2]]
        second_half_name_recycle_1 = board_visual[12 - card_1[3]][card_1[4]]
        if card_1[1] != recent_row and card_1[2] != recent_column:
            recycle_card(card_1[1], card_1[2], card_1[3], card_1[4])
            toked_row = card_1[1]
            toked_column = card_1[2]
            toked_card_type = dict_card_type[recycle_card_num_1]
            dict_level_1 = card_type_coordinates_association_dict()
            for card_type_1, cmds_1 in dict_level_1.items():
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
                    put_board_card(recycle_card_num_1, row1_1, column1_1, row2_1, column2_1)

                    min_value = float(10000000.0)
                    cards_remove_level_2 = find_recyclable_card_nums()
                    for card_2 in cards_remove_level_2:
                        recycle_card_num_2 = card_2[0]
                        first_half_name_recycle_2 = board_visual[12 - card_2[1]][card_2[2]]
                        second_half_name_recycle_2 = board_visual[12 - card_2[3]][card_2[4]]
                        recycle_card(card_2[1], card_2[2], card_2[3], card_2[4])
                        dict_level_2 = card_type_coordinates_association_dict()
                        for card_type_2, cmds_2 in dict_level_2.items():
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
                                put_board_card(recycle_card_num_2, row1_2, column1_2, row2_2, column2_2)

                                max_value = float(-10000000.0)
                                cards_remove_level_3 = find_recyclable_card_nums()
                                for card_3 in cards_remove_level_3:
                                    recycle_card_num_3 = card_3[0]
                                    first_half_name_recycle_3 = board_visual[12 - card_3[1]][card_3[2]]
                                    second_half_name_recycle_3 = board_visual[12 - card_3[3]][card_3[4]]
                                    recycle_card(card_3[1], card_3[2], card_3[3], card_3[4])
                                    dict_level_3 = card_type_coordinates_association_dict()
                                    for card_type_3, cmds_3 in dict_level_3.items():
                                        for cmd_3 in cmds_3:
                                            e = float("{:.1f}".format(evaluate(role, cmd_3)))
                                            e_counter += 1
                                            if e > max_value:
                                                max_value = e
                                                # print("Level3--MAX------------------" + str(max_value) + cmd_3)
                                    place_temp_half(first_half_name_recycle_3, card_3[1], card_3[2])
                                    place_temp_half(second_half_name_recycle_3, card_3[3], card_3[4])
                                    put_board_card(recycle_card_num_3, card_3[1], card_3[2], card_3[3], card_3[4])

                                # minmax_trace.get('level3').append(max_value)
                                recycle_card(row1_2, column1_2, row2_2, column2_2)

                                if max_value < min_value:
                                    min_value = max_value
                                    # print("-----Level2---MIN-----------------" + str(min_value) + cmd_2)

                        place_temp_half(first_half_name_recycle_2, card_2[1], card_2[2])
                        place_temp_half(second_half_name_recycle_2, card_2[3], card_2[4])
                        put_board_card(recycle_card_num_2, card_2[1], card_2[2], card_2[3], card_2[4])

                    minmax_trace.get('level2').append(min_value)
                    recycle_card(row1_1, column1_1, row2_1, column2_1)

                    if final_max_value < min_value:
                        rotated = False
                        if toked_card_type != card_type_1:
                            rotated = True
                        if is_recycle_state_valid(rotated, row1_1, column1_1, row2_1, column2_1):
                            final_max_value = min_value
                            final_cmd = cmd_1
                            selected_card = card_1
                            print("--------Level1------Selecting Level 1 MAX--------------" + str(
                                final_max_value) + " " + cmd_1)
            # if selected_card == '':
            #     final_max_value = 0
            #     selected_card = card_1
            #     final_cmd = cmd_1
            place_temp_half(first_half_name_recycle_1, card_1[1], card_1[2])
            place_temp_half(second_half_name_recycle_1, card_1[3], card_1[4])
            put_board_card(recycle_card_num_1, card_1[1], card_1[2], card_1[3], card_1[4])
    minmax_trace.get('level1').append(final_max_value)
    minmax_trace.setdefault("e_counter", e_counter)

    if isFileGenEnabled:
        generate_tracking_file(minmax_trace)

    toked_row = 100
    toked_column = 100

    return [selected_card, final_cmd]


def evaluate(role_select, cmd):  # board has two additional card, try to place the third card with cmd
    global board_visual
    inputList = command_line_parser(cmd)
    card_type = int(inputList[0])
    row1 = inputList[2]
    row2 = second_half_row(card_type, row1)
    column1 = inputList[1]
    column2 = second_half_column(card_type, column1)
    half_name1 = first_half_name(card_type)
    half_name2 = second_half_name(card_type)

    place_temp_half(half_name1, row1, column1)
    place_temp_half(half_name2, row2, column2)

    factor_one = 5
    factor_two = 20
    factor_three = 100
    factor_four = 10000
    factor_half1 = 10
    factor_half2 = 3
    factor_empty_cell = 3

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

    score_r = [depth_arr_r[0] + depth_arr_r[1] * 1.3, depth_arr_r[2] + depth_arr_r[3], depth_arr_r[4] * 1.3
               + depth_arr_r[5] * 1.3, depth_arr_r[6] + depth_arr_r[7]]
    score_d = [depth_arr_d[0] + depth_arr_d[1] * 1.3, depth_arr_d[2] + depth_arr_d[3], depth_arr_d[4] * 1.3
               + depth_arr_d[5] * 1.3, depth_arr_d[6] + depth_arr_d[7]]
    score_w = [depth_arr_w[0] + depth_arr_w[1] * 1.3, depth_arr_w[2] + depth_arr_w[3], depth_arr_w[4] * 1.3
               + depth_arr_w[5] * 1.3, depth_arr_w[6] + depth_arr_w[7]]
    score_o = [depth_arr_o[0] + depth_arr_o[1] * 1.3, depth_arr_o[2] + depth_arr_o[3], depth_arr_o[4] * 1.3
               + depth_arr_o[5] * 1.3, depth_arr_o[6] + depth_arr_o[7]]

    # [t, b, tr, bl, r, l, rb, lt]

    for score in score_r:
        if score < 2:
            en_r += factor_one * score
        elif score < 3:
            en_r += factor_two * score
        elif score < 4:
            en_r += factor_three * score
        elif score < 5:
            en_r += factor_four * score
            break

    for score in score_d:
        if score < 2:
            en_x += factor_one * score
        elif score < 3:
            en_x += factor_two * score
        elif score < 4:
            en_x += factor_three * score
        elif score < 5:
            en_x += factor_four * score

            break

    for score in score_w:
        if score < 2:
            en_w += factor_one * score
        elif score < 3:
            en_w += factor_two * score
        elif score < 4:
            en_w += factor_three * score
        elif score < 5:
            en_w += factor_four * score
            break

    for score in score_o:
        if score < 2:
            en_o += factor_one * score
        elif score < 3:
            en_o += factor_two * score
        elif score < 4:
            en_o += factor_three * score
        elif score < 5:
            en_o += factor_four * score
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

    remove_temp_card(row1, column1, row2, column2)

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
    number = 0
    try:
        if board_visual[12 - coordinate[0] - depth_num[0]][coordinate[1]] == '  ':
            number += 1
    except IndexError:
        number += 0
    try:
        if board_visual[12 - coordinate[0] - depth_num[2]][coordinate[1] + depth_num[2]] == '  ':
            number += 1
    except IndexError:
        number += 0
    try:
        if board_visual[12 - coordinate[0]][coordinate[1] + - depth_num[4]] == '  ':
            number += 1
    except IndexError:
        number += 0
    try:
        if board_visual[12 - coordinate[0] + depth_num[6]][coordinate[1] + depth_num[6]] == '  ':
            number += 1
    except IndexError:
        number += 0
    try:
        if board_visual[12 - coordinate[0] + depth_num[1]][coordinate[1]] == '  ':
            number += 1
    except IndexError:
        number += 0
    try:
        if board_visual[12 - coordinate[0] + depth_num[3]][coordinate[1] - depth_num[3]] == '  ':
            number += 1
    except IndexError:
        number += 0
    try:
        if board_visual[12 - coordinate[0]][coordinate[1] - depth_num[5]] == '  ':
            number += 1
    except IndexError:
        number += 0
    try:
        if board_visual[12 - coordinate[0] - depth_num[7]][coordinate[1] - depth_num[7]] == '  ':
            number += 1
    except IndexError:
        number += 0
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
recycle_step = 4
isFileGenEnabled = False
file_name = 'minmaxtrace1.txt'

file = input("Do you want to print trace file? (y/n)")
try:
    if file == 'y':
        isFileGenEnabled = True
except Exception:
    isFileGenEnabled = False

ai_player_num = int(input("AI is playing as (1 -> 1st Player, 2 -> 2nd Player)"))
human_player_num = 0
if ai_player_num == 1:
    human_player_num = 2
else:
    human_player_num = 1

ai_player_num = str(ai_player_num)
human_player_num = str(human_player_num)
print("AI chooses to be Player " + ai_player_num)
print('Human is Player ' + human_player_num)

ai_player_role = input("AI will play (c for color, d for dot?")
human_player_role = ''
if ai_player_role == 'c':
    ai_player_role = 'color'
    human_player_role = 'dot'
    print('AI plays ' + ai_player_role + " HUMAN plays " + human_player_role)
else:
    ai_player_role = 'dot'
    human_player_role = 'color'
    print('AI plays ' + ai_player_role + " HUMAN plays " + human_player_role)


print_board()

while step_counter <= 39:
    while card_id <= recycle_step:
        print("This is the step: " + str(step_counter))
        playerId = toggle_player(playerId)

        print_card_type()

        if playerId == human_player_num:
            role = human_player_role
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

        if playerId == ai_player_num:
            role = ai_player_role
            cmd = run_min_max(role)
            inputList = command_line_parser(cmd)
            card_type = int(inputList[0])
            row1 = inputList[2]
            row2 = second_half_row(card_type, row1)
            column1 = inputList[1]
            column2 = second_half_column(card_type, column1)

        half_name1 = first_half_name(card_type)
        half_name2 = second_half_name(card_type)
        card_num = incre_card_id()

        dict_card_type[card_num] = card_type

        print("Last Card with " + str(card_type) + " placed on col = " + str(column1) + " row = " + str(row1))
        place_half(role, half_name1, row1, column1)
        place_half(role, half_name2, row2, column2)
        recent_row = row1
        recent_column = column1


        put_board_card(card_num, row1, column1, row2, column2)
        print_board_card()
        print_board()
        step_counter = step_counter + 1
    while card_id > recycle_step:
        print("This is the step: " + str(step_counter))
        playerId = toggle_player(playerId)

        print_card_type()

        if playerId == human_player_num:
            role = human_player_role
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
                input(
                    "Player " + playerId + ": Select a card type for recycle card and place it. (cardType, col, row):"))
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

                if not is_card_type_valid(card_type) or not is_recycle_state_valid(rotated, row1, column1, row2,
                                                                                   column2):
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
        if playerId == ai_player_num:
            role = ai_player_role

            recycle_and_cmd = run_min_max_recycle(role)
            card_to_recycle = recycle_and_cmd[0]
            recycle_card_id = card_to_recycle[0]

            recycle_card(card_to_recycle[1], card_to_recycle[2], card_to_recycle[3], card_to_recycle[4])

            cmd = recycle_and_cmd[1]

            inputList = command_line_parser(cmd)
            card_type = int(inputList[0])
            row1 = inputList[2]
            row2 = second_half_row(card_type, row1)
            column1 = inputList[1]
            column2 = second_half_column(card_type, column1)

        half_name1 = first_half_name(card_type)
        half_name2 = second_half_name(card_type)

        print(
            "Last Card with " + str(card_type) + " placed on col = " + str(column1) + " row = " + str(row1))
        place_half(role, half_name1, row1, column1)
        place_half(role, half_name2, row2, column2)
        put_board_card(recycle_card_id, row1, column1, row2, column2)

        dict_card_type[recycle_card_id] = card_type

        recent_row = row1
        recent_column = column1

        print_board_card()
        print_board()
        step_counter = step_counter + 1
