#!/usr/bin/python3
"""N Queens Challenge. Position N Non-attack'n queens on an NxN Chess Board"""
from sys import argv


def nqueens():
    """Solve the N-queens puzzle"""

    # setup model
    if len(argv) < 2:
        print("Usage: nqueens N")
        exit(1)

    # setup model
    try:
        n = int(argv[1])
    except Exception:
        print("N must be a number")
        exit(1)

    # setup model
    try:
        assert n >= 4
    except Exception:
        print("N must be at least 4")
        exit(1)

    # BEGIN
    def opt_posn(pos, filled):
        for i in range(len(filled)):
            if pos == filled[i][1] or \
                pos + len(filled) - i == filled[i][1] \
                or pos - len(filled) + i == \
                    filled[i][1]:
                return False
        return True

    def place_queen(n, index, filled, result):
        if index == n:
            result.append(filled)
            return
        for i in range(n):
            if opt_posn(i, filled):
                place_queen(n, index + 1, filled +
                            [[index, i]], result)

    result = []
    place_queen(n, 0, [], result)

    for res in result:
        print(res)


if __name__ == "__main__":
    nqueens()
