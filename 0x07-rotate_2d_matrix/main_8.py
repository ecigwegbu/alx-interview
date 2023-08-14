#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [[1, 2, 3, 4, 5, 6, 7, 8],
              [9, 10, 11, 12, 13, 14, 15, 16],
              [17, 18, 19, 20, 21, 22, 23, 24],
              [25, 26, 27, 28, 29, 30, 31, 32],
              [33, 34, 45, 36, 37, 38, 39, 40],
              [41, 42, 43, 44, 45, 46, 47, 48],
              [49, 50, 51, 52, 53, 54, 55, 56],
              [57, 58, 59, 60, 61, 62, 63, 64]]
    rotate_2d_matrix(matrix)
    print(matrix)
