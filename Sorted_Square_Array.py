"""

  Write a function that takes in a non-empty array of integers that are sorted
  in ascending order and returns a new array of the same length with the squares
  of the original integers also sorted in ascending order.
"""


# O(nlogn) time | O(n) space - where n is the length of the input array
def sorted_square_array(array):
    lowest_index = 0
    highest_index = len(array) - 1
    square_array_index = highest_index
    square_array = [0 for _ in array]
    while lowest_index <= highest_index:
        if abs(array[lowest_index]) < abs(array[highest_index]):
            square_array[square_array_index] = array[highest_index] * array[highest_index]
            highest_index -= 1
        else:
            square_array[square_array_index] = array[lowest_index] * array[lowest_index]
            lowest_index += 1
        square_array_index -= 1
    return square_array


print(sorted_square_array([-5, -3, -1, 1, 1, 2, 3]))
