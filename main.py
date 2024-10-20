from copy import deepcopy

board = [
    ["_", "_", "_"],
    ["_", "_", "_"],
    ["_", "_", "_"]
]

win_patterns = [
    [
        [1, 1, 1],
        [0, 0, 0],
        [0, 0, 0]
    ],
    [
        [0, 0, 0],
        [1, 1, 1],
        [0, 0, 0]
    ],
    [
        [0, 0, 0],
        [0, 0, 0],
        [1, 1, 1]
    ],
    [
        [1, 0, 0],
        [1, 0, 0],
        [1, 0, 0]
    ],
    [
        [0, 1, 0],
        [0, 1, 0],
        [0, 1, 0]
    ],
    [
        [0, 0, 1],
        [0, 0, 1],
        [0, 0, 1]
    ],
    [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ],
    [
        [0, 0, 1],
        [0, 1, 0],
        [1, 0, 0]
    ]
]

is_cross = False

def show_board(): print("\n".join([" ".join([e for e in row]) for row in board]))

def take_coordinates(s : str):
    s = s.split()
    if len(s) != 2: return None, None
    try:
        x, y, = int(s[0]), int(s[1])
    except:
        return None, None
    if x > 3 or x < 1 or y > 3 or y < 1 or board[x - 1][y - 1] != "_":
        return None, None
    return x, y

def check_game_end_condition():
    global board, is_cross
    current_symbol = "X" if is_cross else "O"
    game_state = []
    for row in range(3):
        game_state.append([])
        for col in range(3):
            #print(board[row][col], " == ", current_symbol, " = ", board[row][col] == current_symbol)
            game_state[-1].append(int(board[row][col] == current_symbol))
    flag = False
    for wp in win_patterns:
        multiplied = deepcopy(game_state)
        for row in range(3):
            for col in range(3):
                multiplied[row][col] *= wp[row][col]
        #print(game_state, " * ", wp, " == ", multiplied)
        if wp == multiplied:
            flag = True
            break

    return flag