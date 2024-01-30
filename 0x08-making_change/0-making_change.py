#!/usr/bin/python3
"""
determines fewest number of coins needed to meet a given
amount total when given a pile of coins of different values
"""


def makeChange(coins, total):
    """
    Calculates the fewest number of coins needed to meet a given
    amount total.

    Parameters:
    - coins (list): A list of coin values available.
    - total (int): The target total amount to reach.

    Returns:
    - int: The fewest number of coins needed. Returns -1 if it's not possible
           to make the exact total with the given coins.
    """
    if total <= 0:
        return 0
    rem = total
    coins_count = 0
    coin_idx = 0
    sorted_coins = sorted(coins, reverse=True)
    n = len(coins)
    while rem > 0:
        if coin_idx >= n:
            return -1
        if rem - sorted_coins[coin_idx] >= 0:
            rem -= sorted_coins[coin_idx]
            coins_count += 1
        else:
            coin_idx += 1
    return coins_count
