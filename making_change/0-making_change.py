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

    g = coins[0]
    for c in coins[1:]:
        while c:
            g, c = c, g % c
    if total % g != 0:
        return -1

    if total in coins:
        return 1

    inf = total + 1
    dp = [inf] * (total + 1)
    dp[0] = 0
    coins = sorted(set(coins))

    for i in range(1, total + 1):
        for coin in coins:
            if coin > i:
                break
            c = dp[i - coin] + 1
            if c < dp[i]:
                dp[i] = c

    return dp[total] if dp[total] != inf else -1
