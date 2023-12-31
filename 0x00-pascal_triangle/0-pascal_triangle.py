#!/usr/bin/python3
# Pascal"s Triangle
"""Pascal"s Triangle Challenge"""


def pascal_triangle(n):
    """a function def pascal_triangle(n): that returns a list of lists of
    integers representing the Pascal’s triangle of n:

    Returns an empty list if n <= 0
    You can assume n will be always an integer
    n is the number of rows, numbered 0 to (n-1)

    For improved usability, the code attempts to converst any argument
    to an integer, but ideally the argument should strictly be an integer.
    """

    try:
        n = int(float(n))
    except ValueError as e:
        print("Error: Argument must be convertible to a valid integer")
        exit(98)

    if n <= 0:
        return []

    triangle = []  # list of rows. Each row is also a []

    # i and j are the row and column indexes, numbered starting from 0
    for i in range(n):
        # print("i:", i)
        triangle.append([])  # initialise the first list in the triangle
        # claculate row items for a given row i:
        for j in range(i + 1):
            # print("i: ", i, "j: ", j)
            if j == 0 or j == i:
                triangle[i].append(1)
            else:
                triangle[i].append(triangle[i - 1][j] + triangle[i - 1][j - 1])
            # print("[i, j]:", triangle[i][j])
    return triangle


if __name__ == '__main__':
    from sys import argv
    if len(argv) < 2:
        print("Usage: {} <integer>".format(argv[0]))
        exit(98)
    print(pascal_triangle(argv[1]))
