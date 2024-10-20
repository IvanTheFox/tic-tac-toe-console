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
