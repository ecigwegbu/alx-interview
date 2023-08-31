#!/usr/bin/python3
"""Island perimeter coding challenge
"""


def island_perimeter(grid):
    """Determine the perimeter of an island made up of square pieces of land
    Only one island; no lakes; if data is invalid, return 0.
    """
    # Check for edge cases:
    try:
        assert grid and type(grid) == list
        for row in grid:
            assert type(row) == list
            for cell in row:
                assert cell == 0 or cell == 1
    except Exception:
        #  raise
        return 0

    # Establish grid dimensions
    rows = len(grid)
    cols = len(grid[0])

    # Initialize the perimeter
    result = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Inspect the 4 sides
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    i2, j2 = i + dx, j + dy
                    # Check neighbour, add 1 if necessary
                    if i2 < 0 or i2 >= rows or j2 < 0 or \
                            j2 >= cols or grid[i2][j2] == 0:
                        result += 1

    return result


if __name__ == "__main__":
    pass
