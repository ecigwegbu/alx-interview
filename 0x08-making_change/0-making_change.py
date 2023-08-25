#!/usr/bin/python3
"""Determine the minimum combination of a coins to make change
"""


def makeChange(coins, total):
    """Determine the minimum combination of coins to make change
    """
    # QC the input data
    try:
        assert (type(total) == int and total > 0)
        assert type(coins) == list
        for item in coins:
            assert (type(item) == int and item > 0)
    except Exception:
        return 0

    # setup  a dynamic programming array:
    array = [float('inf')] * (total + 1)
    array[0] = 0

    # Compute the array
    for coin in coins:
        for x in range(coin, total + 1):
            array[x] = min(array[x], array[x - coin] + 1)

    # Test for impossible case -> return -1
    # return -1 if array[total] == float('inf') else array[total]

    if array[total] == float('inf'):
        result = -1  # impossible case
    else:
        result = array[total]
    return result


if __name__ == "__main__":
    pass
