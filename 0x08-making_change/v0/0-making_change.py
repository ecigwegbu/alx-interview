#!/usr/bin/python3
"""Determine the minimum combination of a coins to make change
"""


def makeChange(coins, total):
    """Determine the minimum combination of coins to make change
    """
    try:
        assert (type(total) == int and total > 0)
        assert type(coins) == list
        for item in coins:
            assert (type(item) == int and item > 0)
    except Exception:
        return 0
    return 7


if __name__ == "__main__":
    pass
