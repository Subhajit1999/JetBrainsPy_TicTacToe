# write your code here
user_input = list("_________")
temp_list = []
# global vars
x_turn = True
x_wins = False
o_wins = False
status_codes = ["X wins", "O wins", "Impossible", "Game not finished", "Draw"]

def print_table(user_input):
    mod_input = [" " if item == "_" else item for item in user_input]
    print("---------")
    count = 0
    str_ = ""
    for i in range(3):
        str_ = str_ + "| "
        for j in range(3):
            str_ = str_ + mod_input[count] + " "
            count = count + 1
        if count == 9:
            str_ = str_ + "|"
        else:
            str_ = str_ + "|\n"
    print(str_)
    print("---------")

def take_user_move():
    global x_turn
    user_move = input("Enter the coordinates: >")
    return user_move

def cell_not_occupied(coordinate):
    list_crdnt = [int(i) for i in coordinate.split(" ")]
    global user_input, x_turn, temp_list
    indx = 0
    if list_crdnt[1] == 1:  # 3rd row
        indx = 4 + list_crdnt[0] + list_crdnt[1]
    elif list_crdnt[1] == 2:  # 2nd row
        indx = list_crdnt[0] + list_crdnt[1]
    else:  # 1st row
        indx = abs(4 - (list_crdnt[0] + list_crdnt[1]))

    not_occupied = False
    for i in range(len(user_input)):  # whether cell occupied
        if (i == indx) and (user_input[i] == "_"):
            not_occupied = True
            break

    if not_occupied:  # modify list data
        temp_list = user_input.copy()
        user_input = []
        for count, item in enumerate(temp_list):
            if count == indx:
                if x_turn:
                    user_input.append("X")
                else:
                    user_input.append("O")
            else:
                user_input.append(item)
    return not_occupied

def validate_user_move(move):
    if not (move.replace(" ", "").isnumeric()):  # 1st validation
        print("You should enter numbers!")
        return False
    else:  # 2nd validation
        user_move = move.split(" ")
        for item in user_move:
            if not (1 <= int(item) <= 3):
                print("Coordinates should be from 1 to 3!")
                return False
        if not cell_not_occupied(move):  # 3rd validation
            print("This cell is occupied! Choose another one!")
            return False
    return True

def count_player_moves(user_input):
    win_moves = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    global x_wins, o_wins
    blank_cell = 0
    for sub in win_moves:
        x_count = 0
        o_count = 0
        for i in sub:
            if user_input[i] == 'X':
                x_count = x_count + 1
            elif user_input[i] == 'O':
                o_count = o_count + 1
            else:
                blank_cell = blank_cell + 1
        if x_count == 3:
            x_wins = True
        elif o_count == 3:
            o_wins = True
    return blank_cell

def get_game_status(user_input):
    # it's result time
    blank_cell = count_player_moves(user_input)
    global x_wins, o_wins, status_codes
    if x_wins or o_wins:
        if x_wins and o_wins:
            return status_codes[2]
        elif x_wins:
            return status_codes[0]
        elif o_wins:
            return status_codes[1]
    else:
        if blank_cell>0:
            total_x = 0
            total_o = 0
            for i in user_input:
                if i == "X":
                    total_x = total_x + 1
                elif i == "O":
                    total_o = total_o + 1
            if abs(total_x-total_o)>1:
                return status_codes[2]
            else:
                return status_codes[3]
        else:
            return status_codes[4]

# main program execution starts from here
print_table(user_input)
while True:
    # global status_codes, user_input
    user_move = take_user_move()
    move_validated = validate_user_move(user_move)
    if move_validated:  # if 
        print_table(user_input)
        x_turn = not x_turn
        status = get_game_status(user_input)
        if (status == status_codes[0]) or (status == status_codes[1]) or (status == status_codes[4]):
            print(status)
            break
