#!/usr/bin/python3
"""a function to ascertain the minimum number of coins required to reach a specified total amount"""


def makeChange(coins, total):
    """this function will accept a collection of coins and utilize it to compute the total amount of change needed"""
    if total <= 0:
        return 0

    else:
        coin = sorted(coins)
        coin.reverse()
        cntr = 0
        for i in coin:
            while(total >= i):
                cntr += 1
                total -= i
        if total == 0:
            return cntr
        return -1
