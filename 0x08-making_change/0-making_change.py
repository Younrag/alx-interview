#!/usr/bin/python3
"""
Change comes from within
"""

def make_change(coins, total):
  """
  Calculates the minimum number of coins needed to make a certain amount of money.
  """

  sorted_coins = sorted(coins, reverse=True)

  coins_needed = 0
  remainder = total

  for coin in sorted_coins:
    while remainder >= coin:
      remainder -= coin
      coins_needed += 1

  if remainder > 0:
    return -1

  return coins_needed
