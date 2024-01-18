#!/usr/bin/python3
"""0-minoperations"""


def minOperations(n):
    """
    minOperations
    Gets fewest number of operations needed to result in exactly n H characters
    """
    # all outputs should be at least 2 char: (min, Copy All => Paste)
    if (n < 2):
        return 0
    os, rt = 0, 2
    while rt <= n:
        # if n evenly divides by root
        if n % rt == 0:
            # total even-divisions by root = total operations
            os += rt
            # set n to the remainder
            n = n / rt
            # reduce root to find remaining smaller vals that evenly-divide n
            rt -= 1
        # increment root until it evenly-divides n
        rt += 1
    return os
