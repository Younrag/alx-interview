#!/usr/bin/python3
"""
Change comes from within
"""

def make_change(coins, total):
  """
  Calculates the minimum number of coins needed to make a certain amount of money.
  """
  if total == 0:
        return 0

    remainder = total
    coins_needed = 0

    sorted_coins_list = sorted(coins, reverse=True)
    list_len = len(coins)
    coin_index = 0

    while remainder > 0 and coin_index < list_len:
        if remainder - sorted_coins_list[coin_index] >= 0:
            remainder -= sorted_coins_list[coin_index]
            coins_needed += 1
        else:
            coin_index += 1

    return coins_needed
