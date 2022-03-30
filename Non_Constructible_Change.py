"""
  Given an array of positive integers representing the values of coins in your
  possession, write a function that returns the minimum amount of change (the
  minimum sum of money) that you  create. The given coins can have
  any positive integer value and aren't necessarily unique (i.e., you can have
  multiple coins of the same value).
"""

# O(nlogn) time | O(1) space - where n is the number of coins
def non_constructible_change(coins):
    coins.sort()
    min_change = 0
    for coin in coins:
        if coin > min_change + 1:
            return min_change + 1
        min_change += coin
    return min_change + 1


print(non_constructible_change([5, 7, 1, 1, 2, 3, 22]))
