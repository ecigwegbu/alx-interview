#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
from typing import List, Any
import math

rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix


def print_matrix(matrix: List[List[Any]]) -> None:
    """Print a matrix, one row per line"""
    row_number = 0
    if matrix and type(matrix) == list:
        n = len(matrix)
        for row in matrix:
            row_number += 1
            if row_number == 1:
                print("[{}".format(row), end="")
            else:
                print(",\n {}".format(row), end="")
        print("]")


def build_nxn_matrix(n) -> List[List]:
    """
       Build and return an nxn matrix.
       n must be a positive integer greter than zero
    """
    try:
        assert type(n) == int and n >= 0
    except Exception:
        print("Error: n must be a positive integer greater than zero.")
        exit(-2)
    matrix = [[]]
    m = 0
    for i in range(n):
        matrix.append([])
        for j in range(n):
            m = m + 1
            # print(f"i: {i}, j: {j}, m: {m}")
            matrix[i].append(m)
    matrix.pop()
    return matrix


if __name__ == "__main__":
    # matrix = [[1, 2, 3],
    #          [4, 5, 6],
    #          [7, 8, 9]]
    try:
        from sys import argv
        n = int(argv[1])
        assert n > 0
    except Exception:
        print("Usage: {} <n: int>".format(argv[0]))
        exit(-1)

    # build an nxn matrix
    matrix = build_nxn_matrix(n)

    # print the matrix ("Original Matrix"):
    if matrix:
        print("\nOriginal Matrix:\n")
        print_matrix(matrix)

    rotate_2d_matrix(matrix)  # Take your rotatio code for a spin :)

    # print the result ("Rotated Matrix"):
    if matrix:
        print("\nRotated Matrix:\n")
        print_matrix(matrix)
