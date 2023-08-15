#!/usr/bin/python3
"""Rotate 2D Matrix in-place 90-degrees clockwise.
"""


def rotate_2d_matrix(matrix: list[list]) -> None:
    """Rotate an n x n 2D matrix of by 90 degrees, in-in place
       and Return nothing
    """
    # first verify that it's a square matrix and determine its size:
    try:
        n = len(matrix)  # n == size_of_matrix
        for i in range(n):
            assert type(matrix[i]) == list and len(matrix[i]) == n
    except Exception:
        print("Matrix must be an n x n matrix.")
        return

    # Number of layers
    number_of_layers = n // 2
    max_index = n - 1  # 0-basis

    # now loop over all layers:
    for layer in range(number_of_layers):
        # print(f"\nlayer: {layer}")
        max_offset = max_index - 2 * layer
        # now loop over all offsets, rotating element at 'offset' position
        for offset in range(max_offset):
            temp = matrix[layer][offset + layer]
            matrix[layer][offset + layer] = \
                matrix[max_index - layer - offset][layer]
            matrix[max_index - layer - offset][layer] = \
                matrix[max_index - layer][max_index - layer - offset]
            matrix[max_index - layer][max_index - layer - offset] = \
                matrix[offset + layer][max_index - layer]
            matrix[offset + layer][max_index - layer] = temp

    return
