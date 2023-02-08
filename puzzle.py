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
    """
    ...
