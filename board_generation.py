"""The board generation module"""
import time


def linear_generator(
    seed: int = 14,
    increment: int = 1012,
    multiply: int = 251,
    modulus: int = 8192,
    length: int = 8
) -> list[int]:
    """
    A simple linear RNG algorithm

    Args:
        seed: int - the seed
        increment: int
        multiply: int
        modulus: int
        length: int

    Returns:
        list[int] - a semi-random list of ints
    """
    result: list[int] = []
    random_val = seed
    for _ in range(length):
        random_val = (multiply * random_val + increment) % modulus
        result.append(random_val)

    return result


def generate_line(seed: int, length: int = 9) -> str:
    """
    Generate a line for the board

    Args:
        seed: int - the seed for the line
        length: int - the length of the line

    Returns:
        str - the line
    """
    line = linear_generator(seed=seed, modulus=1024, length=length)
    result = ""
    for i in line:
        if i > 870:
            result += str(i % 10)
        elif i > 600:
            result += " "
        else:
            result += "*"
    return result


def generate_board(seed: int, lines: int = 9) -> list[str]:
    """
    Generate the board

    Args:
        lines: int - the board size
        seed: int - the board seed

    Returns:
        list[str] - a list of strings (the board)
    """
    return [
        generate_line(
            seed=seed + i * 1000,
            length=lines
        ) for i in range(lines)
    ]
