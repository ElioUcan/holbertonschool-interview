#!/usr/bin/python3
"""
Module for makeChange function.
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    Args:
        coins (list): List of values of coins in possession.
        total (int): Target total value.

    Returns:
        int: Fewest number of coins needed to meet total.
             0 if total is 0 or less.
             -1 if total cannot be met by any combination of coins.
    """
    if total <= 0:
        return 0
    if not coins:
        return -1

    coins.sort(reverse=True)
    count = 0

    for coin in coins:
        if total <= 0:
            break
        count += total // coin
        total %= coin

    return count if total == 0 else -1
