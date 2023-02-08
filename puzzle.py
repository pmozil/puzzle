"""The puzzle module"""

COLOURED_BLOCKS = [
    [(i, 4) for i in range(5)] + [(4, i) for i in range(5, 9)],
    [(i, 3) for i in range(1, 6)] + [(5, i) for i in range(4, 8)],
    [(i, 2) for i in range(2, 7)] + [(6, i) for i in range(3, 7)],
    [(i, 1) for i in range(3, 8)] + [(7, i) for i in range(2, 6)],
    [(i, 0) for i in range(4, 9)] + [(8, i) for i in range(1, 5)],
]


def validate_board(board: list[str]) -> bool:
    """
    Validate the board by such rules:
        1) No line contains two identical integers
        2) No row contains two identical integers
        3) No block (as described in the task's statement)
            contains two identical integers

    Args:
        board: list[str] - the board

    Returns:
        bool - whether the board adheres to the rules
    >>> validate_board([\
    "**** ****",\
    "***1 ****",\
    "**  3****",\
    "* 4 1****",\
    "     9 5 ",\
    " 6  83  *",\
    "3   1  **",\
    "  8  2***",\
     "  2  ****"])
    False
    >>> validate_board([\
    "**** ****",\
    "***1 ****",\
    "**  3****",\
    "* 4 1****",\
    "     9 5 ",\
    " 6  83  *",\
    "3   7  **",\
    "  8  2***",\
     "  2  ****"])
    True
    """
    for block in COLOURED_BLOCKS:
        line = [board[i][j] for i, j in block]
        ints = list(filter(lambda x: ord("0") <= ord(x) <= ord("9"), line))
        if len(ints) > len(set(ints)):
            return False

    for line in board:
        ints = list(filter(lambda x: ord("0") <= ord(x) <= ord("9"), line))
        if len(ints) > len(set(ints)):
            return False

    for i in range(len(board)):
        line = [row[i] for row in board]
        ints = list(filter(lambda x: ord("0") <= ord(x) <= ord("9"), line))
        if len(ints) > len(set(ints)):
            return False

    return True