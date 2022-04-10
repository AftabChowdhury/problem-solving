"""

  Write a function that takes in an array of at least three integers and,
  without sorting the input array, returns a sorted array of the three largest
  integers in the input array.
"""


# O(n) time | O(n) space
def findThreeLargestNumbers(array):
    # Write your code here.
    array.sort()
    if len(array) == 3:
        return array
    number = 0
    three_largest_numbers = []
    for i in range(len(array) - 1, 0, -1):
        if number < 3:
            three_largest_numbers.append(array[i])
            number += 1
        else:
            three_largest_numbers.sort()
            return three_largest_numbers


# print(findThreeLargestNumbers([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]))
print(findThreeLargestNumbers([7, 8, 55]))
