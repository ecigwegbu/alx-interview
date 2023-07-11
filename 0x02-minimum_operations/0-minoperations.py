#!/usr/bin/python3
"""
0. Minimum Operations
In a text file, there is a single character H. Your text editor can execute
only two operations in this file: Copy All and Paste. Given a number n, write
a method that calculates the fewest number of operations needed to result in
exactly n H characters in the file.

Prototype: def minOperations(n)
Returns an integer
If n is impossible to achieve, return 0
Example:

n = 9

H => Copy All => Paste => HH => Paste =>HHH => Copy All => Paste => HHHHHH
=> Paste => HHHHHHHHH

Number of operations: 6
"""


def minOperations(n: int) -> int:
    """ Determine the minimum number of operations to create n times char
    H in a file, starting with a single H, and given that only copy ALL
    and paste are the only allowed operations."""

    # Initialise operation: copy all
    n = n           # target number of characters in the file
    opcount = 1     # number of operations so far
    clipboard = 1   # number of characters in the clipboard
    file = 1        # number of characters in the file

    #  while True  # loop until a breakout due to target reached
    while (n % (file + clipboard) != 0) and (file < clipboard):
        # paste
        file += clipboard
        opcount += 1
    if (file < clipboard):
        # paste and copy all
        file += clipboard
        clipboard = file
        opcount += 2

    return opcount
